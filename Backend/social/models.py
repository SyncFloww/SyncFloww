from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Brand(models.Model):
    """Brand profile for multi-brand support"""
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='brands'
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    logo_url = models.URLField(blank=True, null=True)
    voice = models.CharField(max_length=100, blank=True, null=True)  # Brand voice/tone
    target_audience = models.TextField(blank=True, null=True)
    niche = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'brands_brand'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'


class SocialAccount(models.Model):
    """Connected social media accounts"""
    PLATFORMS = [
        ('tiktok', 'TikTok'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('twitter', 'Twitter/X'),
        ('facebook', 'Facebook'),
    ]

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='social_accounts'
    )
    brand = models.ForeignKey(
        Brand, 
        on_delete=models.CASCADE, 
        related_name='social_accounts',
        blank=True, 
        null=True
    )
    platform = models.CharField(max_length=50, choices=PLATFORMS)
    account_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255, blank=True, null=True)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    profile_image_url = models.URLField(blank=True, null=True)
    access_token = models.TextField(blank=True, null=True)  # Encrypt in production
    refresh_token = models.TextField(blank=True, null=True)  # Encrypt in production
    token_expires_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'social_socialaccount'
        verbose_name = 'Social Account'
        verbose_name_plural = 'Social Accounts'
        unique_together = ['user', 'platform', 'account_id']
