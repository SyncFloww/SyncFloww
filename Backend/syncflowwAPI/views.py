"""
Root and health-check views for the SyncFloww API.
"""
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='get',
    operation_summary='API Root',
    operation_description=(
        'Returns basic service information. '
        'No authentication required.'
    ),
    tags=['General'],
    responses={
        200: openapi.Response(
            description='Service info',
            examples={
                'application/json': {
                    'status': 'ok',
                    'service': 'SyncFloww API',
                    'version': '1.0.0',
                    'docs': 'https://api.syncflow.com/swagger/',
                }
            },
        )
    },
)
@api_view(['GET'])
@permission_classes([AllowAny])
def home_view(request):
    """Return API service metadata."""
    return Response({
        'status': 'ok',
        'service': 'SyncFloww API',
        'version': '1.0.0',
        'docs': request.build_absolute_uri('/swagger/'),
    })


@swagger_auto_schema(
    method='get',
    operation_summary='Health Check',
    operation_description='Lightweight liveness probe. Returns HTTP 200 when the service is up.',
    tags=['General'],
    responses={
        200: openapi.Response(
            description='Service is healthy',
            examples={
                'application/json': {'status': 'healthy'}
            },
        )
    },
)
@api_view(['GET'])
@permission_classes([AllowAny])
def health_check(request):
    """Liveness probe endpoint."""
    return Response({'status': 'healthy'})
