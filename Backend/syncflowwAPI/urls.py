"""
URL configuration for syncflowwAPI project.

API is hosted at: https://api.syncflow.com
Swagger UI:       https://api.syncflow.com/swagger/
ReDoc UI:         https://api.syncflow.com/redoc/
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import home_view, health_check

# ─── Swagger Schema View ─────────────────────────────────────────────────────
schema_view = get_schema_view(
    openapi.Info(
        title='SyncFloww API',
        default_version='v1',
        description=(
            '## SyncFloww REST API\n\n'
            'This API powers the SyncFloww platform — manage users, projects, '
            'social brand accounts, and AI agents.\n\n'
            '### Authentication\n'
            'Most endpoints require a **JWT Bearer token**. '
            'Obtain a token via `POST /api/users/auth/login/` or '
            '`POST /api/users/auth/register/`, then click the '
            '**Authorize 🔒** button above and enter:\n\n'
            '```\nBearer <your_access_token>\n```\n\n'
            '### Base URL\n'
            '`https://api.syncflow.com`'
        ),
        terms_of_service='https://syncfloww.com/terms/',
        contact=openapi.Contact(
            name='SyncFloww Support',
            email='partnermarvel55@gmail.com',
            url='https://syncfloww.com',
        ),
        license=openapi.License(name='Proprietary'),
        x_logo={
            'url': 'https://syncfloww.com/logo.png',
            'altText': 'SyncFloww',
        },
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# ─── URL Patterns ─────────────────────────────────────────────────────────────
urlpatterns = [
    # ── Admin ────────────────────────────────────────────────────────────────
    path('admin/', admin.site.urls),

    # ── General ──────────────────────────────────────────────────────────────
    path('', home_view, name='home'),
    path('health/', health_check, name='health'),

    # ── Swagger / ReDoc ──────────────────────────────────────────────────────
    re_path(
        r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'swagger/',
        schema_view.with_ui('swagger', cache_timeout=0),
        name='schema-swagger-ui',
    ),
    path(
        'redoc/',
        schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc',
    ),

    # ── Users & Auth ─────────────────────────────────────────────────────────
    # Mounts at /api/users/ → covers /api/users/auth/* and /api/users/profile/*
    path('api/users/', include('users.urls')),

    # ── Projects ─────────────────────────────────────────────────────────────
    path('api/projects/', include('projects.urls')),

    # ── Social & Brands ──────────────────────────────────────────────────────
    # social.urls is mounted under both prefixes per the API spec
    path('api/social/', include('social.urls')),
    path('api/brands/', include('social.urls')),

    # ── AI Agents ────────────────────────────────────────────────────────────
    path('api/ai/', include('ai_agents.urls')),
]
