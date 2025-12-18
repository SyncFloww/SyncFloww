from django.db import models
from django.contrib.auth import get_user_model
from social.models import SocialAccount

User = get_user_model()


class AutomationRule(models.Model):
    """Automation rules for social engagement"""
    AUTOMATION_TYPES = [
        ('auto_reply', 'Auto Reply'),
        ('scheduled_post', 'Scheduled Post'),
        ('engagement', 'Engagement'),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('paused', 'Paused'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='automation_rules'
    )
    social_account = models.ForeignKey(
        SocialAccount, 
        on_delete=models.CASCADE, 
        related_name='automation_rules'
    )
    name = models.CharField(max_length=255)
    automation_type = models.CharField(max_length=50, choices=AUTOMATION_TYPES)
    target = models.CharField(max_length=255)
    message = models.TextField()
    interval_minutes = models.IntegerField(default=60)
    daily_limit = models.IntegerField(default=100)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='active')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'automations_automationrule'
        verbose_name = 'Automation Rule'
        verbose_name_plural = 'Automation Rules'
