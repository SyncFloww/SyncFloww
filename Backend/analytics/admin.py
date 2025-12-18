from django.contrib import admin
from .models import AnalyticsData

@admin.register(AnalyticsData)
class AnalyticsDataAdmin(admin.ModelAdmin):
    list_display = ['social_account', 'date', 'followers', 'likes', 'impressions']
    list_filter = ['date', 'social_account__platform']
    search_fields = ['social_account__username']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'date'
