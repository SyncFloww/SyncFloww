from django.db import models
from social.models import SocialAccount


class AnalyticsData(models.Model):
    """Daily analytics snapshot for social accounts"""
    social_account = models.ForeignKey(
        SocialAccount, 
        on_delete=models.CASCADE, 
        related_name='analytics'
    )
    date = models.DateField()
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    shares = models.IntegerField(default=0)
    impressions = models.IntegerField(default=0)
    reach = models.IntegerField(default=0)
    profile_views = models.IntegerField(default=0)
    website_clicks = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'analytics_analyticsdata'
        verbose_name = 'Analytics Data'
        verbose_name_plural = 'Analytics Data'
        unique_together = ['social_account', 'date']
        ordering = ['-date']
