from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'project_type', 'status', 'generations_count', 'created_at']
    list_filter = ['project_type', 'status', 'created_at']
    search_fields = ['title', 'description', 'user__email']
    readonly_fields = ['id', 'created_at', 'updated_at']
    
    fieldsets = (
        (None, {'fields': ('user', 'title', 'description')}),
        ('Project Details', {'fields': ('project_type', 'status', 'generations_count', 'thumbnail_url')}),
        ('Timestamps', {'fields': ('created_at', 'updated_at')}),
    )
