from rest_framework import serializers
from .models import AIAgent, AgentTask

class AIAgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AIAgent
        fields = ['id', 'name', 'description', 'task_type', 'is_active']

class AgentTaskSerializer(serializers.ModelSerializer):
    agent_name = serializers.CharField(source='agent.name', read_only=True)
    
    class Meta:
        model = AgentTask
        fields = '__all__'
        read_only_fields = ['status', 'completed_at', 'output_data', 'created_at']
