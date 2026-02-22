from rest_framework import status, viewsets, mixins, permissions
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from social_django.utils import psa
import requests

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Profile
from .serializers import (
    UserSerializer,
    UserRegistrationSerializer,
    UserLoginSerializer,
    ProfileSerializer,
    SocialAuthSerializer,
    PasswordResetSerializer,
)

User = get_user_model()

# ─── Shared response schemas ─────────────────────────────────────────────────

_token_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'user': openapi.Schema(type=openapi.TYPE_OBJECT, description='User object'),
        'tokens': openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'access': openapi.Schema(type=openapi.TYPE_STRING, description='JWT access token'),
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, description='JWT refresh token'),
            },
        ),
    },
    example={
        'user': {
            'id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
            'email': 'user@example.com',
            'full_name': 'Jane Doe',
            'avatar_url': 'https://example.com/avatar.jpg',
            'email_confirmed': True,
            'created_at': '2024-01-15T10:30:00Z',
        },
        'tokens': {
            'access': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
            'refresh': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
        },
    },
)

_error_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={'error': openapi.Schema(type=openapi.TYPE_STRING)},
    example={'error': 'Invalid credentials'},
)

_access_token_body = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['access_token'],
    properties={
        'access_token': openapi.Schema(
            type=openapi.TYPE_STRING,
            description='OAuth access token obtained from the provider',
            example='ya29.a0AfH6SMBx...',
        )
    },
)


# ─── Auth Views ──────────────────────────────────────────────────────────────

class RegisterView(APIView):
    """User registration endpoint."""
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary='Register a new user',
        operation_description=(
            'Create a new account with email and password. '
            'Returns the created user object and a JWT token pair.'
        ),
        tags=['Auth'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password', 'password_confirm'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', example='user@example.com'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format='password', example='SecurePass123!'),
                'password_confirm': openapi.Schema(type=openapi.TYPE_STRING, format='password', example='SecurePass123!'),
                'full_name': openapi.Schema(type=openapi.TYPE_STRING, example='Jane Doe'),
            },
        ),
        responses={
            201: openapi.Response('User created successfully', schema=_token_response),
            400: openapi.Response('Validation error', schema=_error_response),
        },
    )
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """User login endpoint."""
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary='Log in with email and password',
        operation_description=(
            'Authenticate with email and password. '
            'Returns a JWT access token and refresh token.'
        ),
        tags=['Auth'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email', 'password'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', example='user@example.com'),
                'password': openapi.Schema(type=openapi.TYPE_STRING, format='password', example='SecurePass123!'),
            },
        ),
        responses={
            200: openapi.Response('Login successful', schema=_token_response),
            400: openapi.Response('Validation error'),
            401: openapi.Response('Invalid credentials', schema=_error_response),
        },
    )
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'user': UserSerializer(user).data,
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                })
            return Response(
                {'error': 'Invalid credentials'},
                status=status.HTTP_401_UNAUTHORIZED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    """User logout endpoint."""
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Log out (blacklist refresh token)',
        operation_description=(
            'Blacklists the provided refresh token so it can no longer be used. '
            'Requires a valid Bearer access token in the Authorization header.'
        ),
        tags=['Auth'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'refresh_token': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    description='The refresh token to invalidate',
                    example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
                ),
            },
        ),
        responses={
            200: openapi.Response(
                'Logged out successfully',
                examples={'application/json': {'message': 'Successfully logged out'}},
            ),
            400: openapi.Response('Error', schema=_error_response),
        },
    )
    def post(self, request):
        try:
            refresh_token = request.data.get('refresh_token')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
            return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CurrentUserView(APIView):
    """Get current authenticated user."""
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary='Get current user',
        operation_description='Returns the profile of the currently authenticated user.',
        tags=['Auth'],
        responses={
            200: openapi.Response('Current user data', schema=openapi.Schema(
                type=openapi.TYPE_OBJECT,
                example={
                    'id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
                    'email': 'user@example.com',
                    'full_name': 'Jane Doe',
                    'avatar_url': 'https://example.com/avatar.jpg',
                    'email_confirmed': True,
                    'created_at': '2024-01-15T10:30:00Z',
                },
            )),
            401: openapi.Response('Not authenticated'),
        },
    )
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class GoogleOAuthView(APIView):
    """Google OAuth authentication endpoint."""
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary='Sign in with Google',
        operation_description=(
            'Exchange a Google OAuth2 access token for SyncFloww JWT tokens. '
            'The frontend should obtain the Google access token via the Google Sign-In SDK '
            'and pass it here.'
        ),
        tags=['Social Auth'],
        request_body=_access_token_body,
        responses={
            200: openapi.Response('Authentication successful', schema=_token_response),
            400: openapi.Response('Invalid or missing token', schema=_error_response),
            500: openapi.Response('Server error', schema=_error_response),
        },
    )
    def post(self, request):
        access_token = request.data.get('access_token')
        if not access_token:
            return Response(
                {'error': 'Access token is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            google_response = requests.get(
                'https://www.googleapis.com/oauth2/v3/userinfo',
                headers={'Authorization': f'Bearer {access_token}'}
            )
            if google_response.status_code != 200:
                return Response(
                    {'error': 'Invalid Google token'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_info = google_response.json()
            email = user_info.get('email')
            if not email:
                return Response(
                    {'error': 'Email not provided by Google'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    'full_name': user_info.get('name', ''),
                    'avatar_url': user_info.get('picture', ''),
                    'provider': 'google',
                    'provider_id': user_info.get('sub'),
                    'email_confirmed': True,
                }
            )
            if not created:
                user.full_name = user_info.get('name', user.full_name)
                user.avatar_url = user_info.get('picture', user.avatar_url)
                user.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class FacebookOAuthView(APIView):
    """Facebook OAuth authentication endpoint."""
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary='Sign in with Facebook',
        operation_description=(
            'Exchange a Facebook OAuth2 access token for SyncFloww JWT tokens. '
            'The frontend should obtain the Facebook access token via the Facebook Login SDK '
            'and pass it here.'
        ),
        tags=['Social Auth'],
        request_body=_access_token_body,
        responses={
            200: openapi.Response('Authentication successful', schema=_token_response),
            400: openapi.Response('Invalid or missing token', schema=_error_response),
            500: openapi.Response('Server error', schema=_error_response),
        },
    )
    def post(self, request):
        access_token = request.data.get('access_token')
        if not access_token:
            return Response(
                {'error': 'Access token is required'},
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            fb_response = requests.get(
                f'https://graph.facebook.com/me?fields=id,name,email,picture&access_token={access_token}'
            )
            if fb_response.status_code != 200:
                return Response(
                    {'error': 'Invalid Facebook token'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user_info = fb_response.json()
            email = user_info.get('email')
            if not email:
                return Response(
                    {'error': 'Email not provided by Facebook'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    'full_name': user_info.get('name', ''),
                    'avatar_url': user_info.get('picture', {}).get('data', {}).get('url', ''),
                    'provider': 'facebook',
                    'provider_id': user_info.get('id'),
                    'email_confirmed': True,
                }
            )
            if not created:
                user.full_name = user_info.get('name', user.full_name)
                user.avatar_url = user_info.get('picture', {}).get('data', {}).get('url', user.avatar_url)
                user.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class AppleOAuthView(APIView):
    """Apple OAuth authentication endpoint."""
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary='Sign in with Apple',
        operation_description=(
            '⚠️ **Not yet implemented.** '
            'Apple Sign-In requires a signed JWT from the Apple Identity Token. '
            'Add Apple credentials to `.env` and complete the backend verification logic to enable this endpoint.'
        ),
        tags=['Social Auth'],
        request_body=_access_token_body,
        responses={
            501: openapi.Response('Not implemented', schema=_error_response),
        },
    )
    def post(self, request):
        return Response(
            {'error': 'Apple OAuth not fully implemented. Please add credentials and implementation.'},
            status=status.HTTP_501_NOT_IMPLEMENTED
        )


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    """Profile management viewset."""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    _profile_response = openapi.Response(
        'Profile data',
        examples={
            'application/json': {
                'id': 1,
                'user_id': '3fa85f64-5717-4562-b3fc-2c963f66afa6',
                'email': 'user@example.com',
                'full_name': 'Jane Doe',
                'avatar_url': 'https://cdn.example.com/avatar.jpg',
                'created_at': '2024-01-15T10:30:00Z',
                'updated_at': '2024-01-20T08:00:00Z',
            }
        },
    )

    @swagger_auto_schema(
        methods=['get'],
        operation_summary='Get my profile',
        operation_description='Returns the profile of the currently authenticated user.',
        tags=['Profile'],
        responses={200: _profile_response},
    )
    @swagger_auto_schema(
        methods=['put', 'patch'],
        operation_summary='Update my profile',
        operation_description='Updates the authenticated user\'s profile. All fields are optional.',
        tags=['Profile'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'full_name': openapi.Schema(type=openapi.TYPE_STRING, example='Jane Doe'),
                'avatar_url': openapi.Schema(type=openapi.TYPE_STRING, example='https://cdn.example.com/avatar.jpg'),
            },
        ),
        responses={200: _profile_response},
    )
    @action(detail=False, methods=['get', 'put', 'patch'], url_path='me')
    def me(self, request):
        """Get or update current user's profile."""
        profile, created = Profile.objects.get_or_create(user=request.user)
        if request.method in ['PUT', 'PATCH']:
            serializer = self.get_serializer(profile, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            user = request.user
            if 'full_name' in request.data:
                user.full_name = request.data['full_name']
            if 'avatar_url' in request.data:
                user.avatar_url = request.data['avatar_url']
            user.save()
            return Response(serializer.data)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)


class PasswordResetView(APIView):
    """Password reset request endpoint."""
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary='Request a password reset email',
        operation_description=(
            'Sends a password reset email to the specified address **if an account exists**. '
            'For security, the response is identical whether or not the email is registered.'
        ),
        tags=['Auth'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['email'],
            properties={
                'email': openapi.Schema(type=openapi.TYPE_STRING, format='email', example='user@example.com'),
            },
        ),
        responses={
            200: openapi.Response(
                'Email sent (or account not found — same response for security)',
                examples={'application/json': {'message': 'Password reset email sent'}},
            ),
            400: openapi.Response('Validation error'),
        },
    )
    def post(self, request):
        from django.core.mail import send_mail
        from django.conf import settings as django_settings

        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            try:
                user = User.objects.get(email=email)
                send_mail(
                    'Password Reset Request',
                    f'Hello {user.full_name or user.email},\n\n'
                    'We received a request to reset your password. '
                    'Please use the link below to reset your password:\n\n'
                    '[Password reset link would go here]\n\n'
                    'If you did not request this, please ignore this email.',
                    django_settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
            except User.DoesNotExist:
                pass  # Do not reveal user existence
            return Response(
                {'message': 'Password reset email sent'},
                status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
