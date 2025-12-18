from django.contrib import admin
from .models import AutomationRule

@admin.register(AutomationRule)
class AutomationRuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'automation_type', 'status', 'is_active']
    list_filter = ['automation_type', 'status', 'is_active']
    search_fields = ['name', 'user__email']
    readonly_fields = ['created_at', 'updated_at']
