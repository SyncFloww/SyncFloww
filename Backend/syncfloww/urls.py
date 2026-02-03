from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

def home(request):
    return JsonResponse({
        "status": "online",
        "message": "Welcome to SyncFloww API",
        "documentation": "/swagger/"
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path('', home),  # Root URL
    
    # API Routes
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/social/', include('social.urls')),      # Custom social endpoints
    path('api/brands/', include('social.urls')),      # Brands handled by social app too, roughly
    path('api/ai/', include('ai_agents.urls')),
]

# Swagger Configuration
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="SyncFloww API",
      default_version='v1',
      description="API documentation for SyncFloww",
      contact=openapi.Contact(email="contact@syncfloww.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
