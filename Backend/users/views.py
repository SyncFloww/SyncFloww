from rest_framework import status, viewsets, mixins, permissions
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model
from social_django.utils import psa
import requests

from .models import Profile
from .serializers import (
    UserSerializer, 
    UserRegistrationSerializer, 
    UserLoginSerializer,
    ProfileSerializer,
    SocialAuthSerializer
)

User = get_user_model()


class RegisterView(APIView):
    """User registration endpoint"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # Generate JWT tokens
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
    """User login endpoint"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                # Generate JWT tokens
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
    """User logout endpoint"""
    permission_classes = [IsAuthenticated]
    
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
    """Get current authenticated user"""
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)


class GoogleOAuthView(APIView):
    """Google OAuth authentication endpoint"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        access_token = request.data.get('access_token')
        
        if not access_token:
            return Response(
                {'error': 'Access token is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Verify Google token and get user info
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
            
            # Get or create user
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
            
            # Update user info if not created
            if not created:
                user.full_name = user_info.get('name', user.full_name)
                user.avatar_url = user_info.get('picture', user.avatar_url)
                user.save()
            
            # Generate JWT tokens
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
    """Facebook OAuth authentication endpoint"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        access_token = request.data.get('access_token')
        
        if not access_token:
            return Response(
                {'error': 'Access token is required'}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            # Verify Facebook token and get user info
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
            
            # Get or create user
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
            
            # Update user info if not created
            if not created:
                user.full_name = user_info.get('name', user.full_name)
                user.avatar_url = user_info.get('picture', {}).get('data', {}).get('url', user.avatar_url)
                user.save()
            
            # Generate JWT tokens
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
    """Apple OAuth authentication endpoint"""
    permission_classes = [AllowAny]
    
    def post(self, request):
        # Apple OAuth requires more complex implementation with JWT verification
        # This is a placeholder that can be expanded based on Apple's requirements
        return Response(
            {'error': 'Apple OAuth not fully implemented. Please add credentials and implementation.'}, 
            status=status.HTTP_501_NOT_IMPLEMENTED
        )


class ProfileViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    """Profile management viewset"""
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    @action(detail=False, methods=['get', 'put', 'patch'], url_path='me')
    def me(self, request):
        """Get or update current user's profile"""
        profile, created = Profile.objects.get_or_create(user=request.user)
        
        if request.method in ['PUT', 'PATCH']:
            serializer = self.get_serializer(profile, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            # Also update user model
            user = request.user
            if 'full_name' in request.data:
                user.full_name = request.data['full_name']
            if 'avatar_url' in request.data:
                user.avatar_url = request.data['avatar_url']
            user.save()
            
            return Response(serializer.data)
            
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
