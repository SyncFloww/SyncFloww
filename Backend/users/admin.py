from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'full_name', 'created_at']
    search_fields = ['full_name', 'user__email']
    readonly_fields = ['id', 'created_at', 'updated_at']
