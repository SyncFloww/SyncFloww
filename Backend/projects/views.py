from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import Project
from .serializers import ProjectSerializer, ProjectCreateSerializer


_project_example = {
    'id': 1,
    'title': 'Summer Campaign 2024',
    'description': 'Social media campaign for Q3 product launch.',
    'thumbnail_url': 'https://cdn.example.com/thumb.jpg',
    'project_type': 'production_package',
    'generations_count': 5,
    'status': 'in_progress',
    'created_at': '2024-06-01T09:00:00Z',
    'updated_at': '2024-06-15T12:00:00Z',
}

_project_create_example = {
    'title': 'New Idea Project',
    'description': 'Initial idea for a brand awareness campaign.',
    'thumbnail_url': '',
    'project_type': 'idea',
    'generations_count': 0,
    'status': 'draft',
}


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user projects.

    Provides full CRUD operations. All endpoints require authentication.
    Projects are automatically scoped to the authenticated user.

    **Project types:** `idea`, `script`, `production_package`

    **Statuses:** `draft`, `in_progress`, `completed`

    **Filtering:** `?status=draft&project_type=idea`

    **Search:** `?search=campaign`

    **Ordering:** `?ordering=-created_at`
    """
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['status', 'project_type']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at', 'title']
    ordering = ['-created_at']

    swagger_tags = ['Projects']

    def get_serializer_class(self):
        """Use ProjectCreateSerializer for create, ProjectSerializer for all others."""
        if self.action == 'create':
            return ProjectCreateSerializer
        return ProjectSerializer

    def get_queryset(self):
        """Filter projects to only show the authenticated user's own projects."""
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Automatically assign the authenticated user as the project owner."""
        serializer.save(user=self.request.user)

    @swagger_auto_schema(
        operation_summary='List projects',
        operation_description=(
            'Returns a paginated list of **all projects belonging to the authenticated user**.\n\n'
            'Use query params to filter, search, or order results:\n'
            '- `status` — filter by `draft`, `in_progress`, or `completed`\n'
            '- `project_type` — filter by `idea`, `script`, or `production_package`\n'
            '- `search` — full-text search across title and description\n'
            '- `ordering` — sort by `created_at`, `updated_at`, or `title` (prefix `-` for descending)'
        ),
        tags=['Projects'],
        responses={
            200: openapi.Response(
                'Paginated list of projects',
                examples={'application/json': {
                    'count': 1, 'next': None, 'previous': None,
                    'results': [_project_example],
                }},
            )
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Create a project',
        operation_description='Creates a new project for the authenticated user.',
        tags=['Projects'],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['title', 'project_type'],
            properties={
                'title': openapi.Schema(type=openapi.TYPE_STRING, example='New Idea Project'),
                'description': openapi.Schema(type=openapi.TYPE_STRING, example='A fresh idea.'),
                'thumbnail_url': openapi.Schema(type=openapi.TYPE_STRING, example=''),
                'project_type': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=['idea', 'script', 'production_package'],
                    example='idea',
                ),
                'generations_count': openapi.Schema(type=openapi.TYPE_INTEGER, example=0),
                'status': openapi.Schema(
                    type=openapi.TYPE_STRING,
                    enum=['draft', 'in_progress', 'completed'],
                    example='draft',
                ),
            },
        ),
        responses={
            201: openapi.Response('Project created', examples={'application/json': _project_example}),
            400: openapi.Response('Validation error'),
        },
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Retrieve a project',
        operation_description='Returns the full details of a single project by `id`.',
        tags=['Projects'],
        responses={
            200: openapi.Response('Project details', examples={'application/json': _project_example}),
            404: openapi.Response('Not found'),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Update a project (full)',
        operation_description='Replaces all fields of a project. Use PATCH for partial updates.',
        tags=['Projects'],
        responses={
            200: openapi.Response('Updated project', examples={'application/json': _project_example}),
            400: openapi.Response('Validation error'),
            404: openapi.Response('Not found'),
        },
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Partially update a project',
        operation_description='Updates only the provided fields of a project.',
        tags=['Projects'],
        responses={
            200: openapi.Response('Updated project', examples={'application/json': _project_example}),
            400: openapi.Response('Validation error'),
            404: openapi.Response('Not found'),
        },
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Delete a project',
        operation_description='Permanently deletes a project. This action cannot be undone.',
        tags=['Projects'],
        responses={
            204: openapi.Response('Project deleted'),
            404: openapi.Response('Not found'),
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
