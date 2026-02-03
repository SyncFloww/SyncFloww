from rest_framework import viewsets, permissions, filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Project
from .serializers import ProjectSerializer, ProjectCreateSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing user projects
    
    Provides CRUD operations for projects:
    - List all projects for authenticated user
    - Create new project
    - Retrieve project details
    - Update project
    - Delete project
    """
    queryset = Project.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['status', 'project_type']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at', 'updated_at', 'title']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        """Use different serializers for different actions"""
        if self.action == 'create':
            return ProjectCreateSerializer
        return ProjectSerializer
    
    def get_queryset(self):
        """Filter projects to only show user's own projects"""
        return self.queryset.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        """Set the user when creating a project"""
        serializer.save(user=self.request.user)
