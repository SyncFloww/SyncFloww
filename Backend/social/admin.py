from django.contrib import admin
from .models import Brand, SocialAccount

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'niche', 'is_active', 'created_at']
    list_filter = ['is_active', 'niche']
    search_fields = ['name', 'user__email', 'niche']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(SocialAccount)
class SocialAccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'platform', 'user', 'brand', 'is_active']
    list_filter = ['platform', 'is_active']
    search_fields = ['username', 'display_name', 'user__email']
    readonly_fields = ['created_at', 'updated_at']
