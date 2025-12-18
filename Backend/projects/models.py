from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class Project(models.Model):
    """User video project"""
    PROJECT_TYPES = [
        ('idea', 'Idea'),
        ('script', 'Script'),
        ('production_package', 'Production Package'),
    ]
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='projects'
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    thumbnail_url = models.URLField(blank=True, null=True)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPES)
    generations_count = models.IntegerField(default=1)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'projects'
        ordering = ['-created_at']
