from django.contrib import admin
from .models import LLMProvider, AIModel, AIAgent, AgentTask, AIConfiguration

@admin.register(LLMProvider)
class LLMProviderAdmin(admin.ModelAdmin):
    list_display = ['name', 'provider_class', 'is_active', 'created_at']
    list_filter = ['provider_class', 'is_active']
    search_fields = ['name']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(AIModel)
class AIModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'model_id', 'model_type', 'provider', 'is_active']
    list_filter = ['model_type', 'provider', 'is_active']
    search_fields = ['name', 'model_id']
    readonly_fields = ['created_at', 'updated_at']


@admin.register(AIAgent)
class AIAgentAdmin(admin.ModelAdmin):
    list_display = ['name', 'task_type', 'model', 'is_active', 'created_at']
    list_filter = ['task_type', 'is_active', 'model']
    search_fields = ['name', 'description']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        (None, {
            'fields': ('name', 'description', 'task_type', 'model', 'is_active')
        }),
        ('Configuration', {
            'fields': ('config',),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AgentTask)
class AgentTaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'agent', 'status', 'created_at', 'completed_at']
    list_filter = ['status', 'agent', 'created_at']
    search_fields = ['agent__name']
    readonly_fields = ['created_at', 'updated_at', 'completed_at']
    fieldsets = (
        (None, {
            'fields': ('agent', 'status')
        }),
        ('Data', {
            'fields': ('input_data', 'output_data'),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at', 'completed_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(AIConfiguration)
class AIConfigurationAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'model_name', 'temperature', 'is_active']
    list_filter = ['model_name', 'is_active']
    search_fields = ['name', 'user__email']
    readonly_fields = ['created_at', 'updated_at']
