from rest_framework import serializers
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project model"""
    
    class Meta:
        model = Project
        fields = [
            'id', 
            'title', 
            'description', 
            'thumbnail_url', 
            'project_type', 
            'generations_count', 
            'status', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_project_type(self, value):
        """Validate project_type is one of the allowed choices"""
        valid_types = ['idea', 'script', 'production_package']
        if value not in valid_types:
            raise serializers.ValidationError(f"Invalid project type. Must be one of: {', '.join(valid_types)}")
        return value
    
    def validate_status(self, value):
        """Validate status is one of the allowed choices"""
        valid_statuses = ['draft', 'in_progress', 'completed']
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Invalid status. Must be one of: {', '.join(valid_statuses)}")
        return value


class ProjectCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating projects"""
    
    class Meta:
        model = Project
        fields = [
            'title', 
            'description', 
            'thumbnail_url', 
            'project_type', 
            'generations_count', 
            'status'
        ]
    
    def create(self, validated_data):
        # User will be set in the view
        return super().create(validated_data)
