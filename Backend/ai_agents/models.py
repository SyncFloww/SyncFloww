from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class LLMProvider(models.Model):
    """LLM API provider configuration"""
    PROVIDER_CLASSES = [
        ('openai', 'OpenAI'),
        ('anthropic', 'Anthropic'),
        ('google', 'Google'),
        ('cohere', 'Cohere'),
        ('mistral', 'Mistral'),
    ]

    name = models.CharField(max_length=255)
    provider_class = models.CharField(max_length=255, choices=PROVIDER_CLASSES)
    api_key = models.TextField(blank=True, null=True)  # Encrypt in production
    base_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AIs_llmprovider'
        verbose_name = 'LLM Provider'
        verbose_name_plural = 'LLM Providers'


class AIModel(models.Model):
    """AI model definition"""
    MODEL_TYPES = [
        ('chat', 'Chat'),
        ('completion', 'Completion'),
        ('embedding', 'Embedding'),
    ]

    name = models.CharField(max_length=255)
    model_id = models.CharField(max_length=255)  # e.g., 'gpt-4', 'claude-3'
    model_type = models.CharField(max_length=50, choices=MODEL_TYPES)
    description = models.TextField()
    context_window = models.IntegerField(blank=True, null=True)
    provider = models.ForeignKey(
        LLMProvider, 
        on_delete=models.CASCADE, 
        related_name='models'
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AIs_aimodel'
        verbose_name = 'AI Model'
        verbose_name_plural = 'AI Models'


class AIAgent(models.Model):
    """AI agent configuration for specific tasks"""
    TASK_TYPES = [
        ('improvement', 'Improvement Agent'),
        ('variation', 'Variation Agent'),
        ('script', 'Scriptwriting Agent'),
        ('caption', 'Caption Agent'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    task_type = models.CharField(max_length=100, choices=TASK_TYPES)
    model = models.ForeignKey(
        AIModel, 
        on_delete=models.CASCADE, 
        related_name='agents'
    )
    config = models.JSONField(default=dict)  # system_prompt, temperature, etc.
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AIs_aiagent'
        verbose_name = 'AI Agent'
        verbose_name_plural = 'AI Agents'


class AgentTask(models.Model):
    """Log of agent task executions"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('processing', 'Processing'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    agent = models.ForeignKey(
        AIAgent, 
        on_delete=models.CASCADE, 
        related_name='tasks'
    )
    input_data = models.JSONField()
    output_data = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    completed_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AIs_agenttask'
        verbose_name = 'Agent Task'
        verbose_name_plural = 'Agent Tasks'
        ordering = ['-created_at']


class AIConfiguration(models.Model):
    """User-specific AI configuration preferences"""
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='ai_configurations'
    )
    name = models.CharField(max_length=255)
    model_name = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=3, decimal_places=2, default=0.7)
    max_length = models.IntegerField(default=2000)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'AIs_aiconfiguration'
        verbose_name = 'AI Configuration'
        verbose_name_plural = 'AI Configurations'
