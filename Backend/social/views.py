from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Brand, SocialAccount
from .serializers import BrandSerializer, SocialAccountSerializer


_brand_example = {
    'id': 1,
    'name': 'Acme Corp',
    'logo_url': 'https://cdn.example.com/acme-logo.png',
    'created_at': '2024-03-01T10:00:00Z',
}

_social_account_example = {
    'id': 1,
    'platform': 'instagram',
    'username': '@acme_official',
    'connected': True,
}


class BrandViewSet(viewsets.ModelViewSet):
    """
    Manage social media brands.

    A brand represents a social media identity (e.g. a business or persona)
    that has one or more connected social accounts.
    """
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tags = ['Brands']

    def get_queryset(self):
        return Brand.objects.filter(user=self.request.user)

    @swagger_auto_schema(
        operation_summary='List brands',
        operation_description='Returns all brands belonging to the authenticated user.',
        tags=['Brands'],
        responses={
            200: openapi.Response(
                'List of brands',
                examples={'application/json': [_brand_example]},
            )
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Create a brand',
        operation_description='Creates a new brand for the authenticated user.',
        tags=['Brands'],
        responses={
            201: openapi.Response('Brand created', examples={'application/json': _brand_example}),
            400: openapi.Response('Validation error'),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Retrieve a brand',
        operation_description='Returns details of a single brand by `id`.',
        tags=['Brands'],
        responses={
            200: openapi.Response('Brand details', examples={'application/json': _brand_example}),
            404: openapi.Response('Not found'),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Update a brand (full)',
        tags=['Brands'],
        responses={200: openapi.Response('Updated brand'), 400: openapi.Response('Validation error')},
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Partially update a brand',
        tags=['Brands'],
        responses={200: openapi.Response('Updated brand'), 400: openapi.Response('Validation error')},
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Delete a brand',
        tags=['Brands'],
        responses={204: openapi.Response('Brand deleted'), 404: openapi.Response('Not found')},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='List social accounts for a brand',
        operation_description='Returns all social platform accounts connected to the specified brand.',
        tags=['Social'],
        responses={
            200: openapi.Response(
                'List of connected social accounts',
                examples={'application/json': [_social_account_example]},
            ),
            404: openapi.Response('Brand not found'),
        },
    )
    @action(detail=True, methods=['get'], url_path='social-accounts')
    def social_accounts(self, request, pk=None):
        brand = self.get_object()
        accounts = SocialAccount.objects.filter(brand=brand)
        serializer = SocialAccountSerializer(accounts, many=True)
        return Response(serializer.data)


class SocialAccountViewSet(viewsets.GenericViewSet):
    """Manage social platform connections (OAuth connect/disconnect)."""
    permission_classes = [permissions.IsAuthenticated]
    queryset = SocialAccount.objects.none()

    def get_queryset(self):
        return SocialAccount.objects.filter(user=self.request.user)

    @swagger_auto_schema(
        operation_summary='Connect a social platform',
        operation_description=(
            'Initiates the OAuth connection flow for the specified `platform`.\n\n'
            '**Supported platforms:** `instagram`, `twitter`, `facebook`, `linkedin`, `tiktok`, `youtube`\n\n'
            'Returns a redirect URL to the OAuth provider. '
            'The frontend should redirect the user to that URL to complete authorisation.'
        ),
        tags=['Social'],
        manual_parameters=[
            openapi.Parameter(
                'platform',
                openapi.IN_PATH,
                description='Social platform to connect',
                type=openapi.TYPE_STRING,
                enum=['instagram', 'twitter', 'facebook', 'linkedin', 'tiktok', 'youtube'],
                example='instagram',
            )
        ],
        responses={
            200: openapi.Response(
                'OAuth flow initiated',
                examples={
                    'application/json': {
                        'status': 'initiated',
                        'platform': 'instagram',
                        'url': 'https://api.instagram.com/oauth/authorize?client_id=...',
                    }
                },
            ),
        },
    )
    @action(detail=False, methods=['post'], url_path='connect/(?P<platform>[^/.]+)')
    def connect(self, request, platform=None):
        """Initiate OAuth connection for a social platform."""
        return Response(
            {'status': 'initiated', 'platform': platform, 'url': 'http://mock-oauth-url.com'},
            status=status.HTTP_200_OK,
        )

    @swagger_auto_schema(
        operation_summary='Disconnect a social account',
        operation_description=(
            'Removes the connected social account identified by `id`. '
            'The user will need to reconnect via the OAuth flow to re-link.'
        ),
        tags=['Social'],
        responses={
            204: openapi.Response('Account disconnected'),
            404: openapi.Response('Social account not found'),
        },
    )
    @action(detail=True, methods=['delete'])
    def disconnect(self, request, pk=None):
        """Disconnect and delete a social account."""
        try:
            account = self.get_queryset().get(pk=pk)
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SocialAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
