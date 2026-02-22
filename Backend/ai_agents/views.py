from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from .models import AIAgent, AgentTask
from .serializers import AIAgentSerializer, AgentTaskSerializer


_agent_example = {
    'id': 1,
    'name': 'Content Writer',
    'task_type': 'content_writing',
    'description': 'Generates social media captions and blog posts.',
    'is_active': True,
}

_task_example = {
    'id': 42,
    'agent': 1,
    'input_data': {'topic': 'AI trends 2024', 'tone': 'professional'},
    'status': 'pending',
    'output_data': None,
    'created_at': '2024-06-01T09:00:00Z',
}


class AIAgentViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Browse and execute AI agents.

    Agents are pre-configured automation workers. Use the **execute** action
    to create a task for a specific agent type and return a task ID for polling.
    """
    queryset = AIAgent.objects.filter(is_active=True)
    serializer_class = AIAgentSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tags = ['AI Agents']

    @swagger_auto_schema(
        operation_summary='List available AI agents',
        operation_description='Returns all active AI agents available on the platform.',
        tags=['AI Agents'],
        responses={
            200: openapi.Response(
                'List of AI agents',
                examples={'application/json': [_agent_example]},
            )
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Retrieve an AI agent',
        operation_description='Returns details of a single AI agent by `id`.',
        tags=['AI Agents'],
        responses={
            200: openapi.Response('Agent details', examples={'application/json': _agent_example}),
            404: openapi.Response('Not found'),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Execute an AI agent task',
        operation_description=(
            'Creates and queues a new task for the agent matching `type`.\n\n'
            'The task is processed asynchronously. '
            'Poll `GET /api/ai/tasks/{id}/` to check progress.\n\n'
            '**Common agent types:** `content_writing`, `image_generation`, `caption_generator`'
        ),
        tags=['AI Agents'],
        manual_parameters=[
            openapi.Parameter(
                'type',
                openapi.IN_PATH,
                description='Agent task type identifier',
                type=openapi.TYPE_STRING,
                example='content_writing',
            )
        ],
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            description='Arbitrary input data consumed by the agent. Shape depends on agent type.',
            example={
                'topic': 'AI trends 2024',
                'tone': 'professional',
                'max_words': 200,
            },
        ),
        responses={
            202: openapi.Response(
                'Task accepted and queued',
                examples={'application/json': _task_example},
            ),
            404: openapi.Response(
                'No active agent found for this type',
                examples={'application/json': {'error': 'Agent not found for this type'}},
            ),
        },
    )
    @action(detail=False, methods=['post'], url_path='(?P<type>[^/.]+)/execute')
    def execute(self, request, type=None):
        """Dispatch a task to the matching agent type."""
        agent = AIAgent.objects.filter(task_type=type, is_active=True).first()
        if not agent:
            return Response(
                {'error': 'Agent not found for this type'},
                status=status.HTTP_404_NOT_FOUND,
            )
        task = AgentTask.objects.create(
            agent=agent,
            input_data=request.data,
            status='pending',
        )
        # Uncomment when Celery is configured:
        # run_agent.delay(task.id)
        return Response(AgentTaskSerializer(task).data, status=status.HTTP_202_ACCEPTED)


class AgentTaskViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View and monitor AI agent tasks.

    Tasks are created by calling the **execute** action on an AI agent.
    Poll this endpoint to check task status and retrieve output when complete.
    """
    serializer_class = AgentTaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    swagger_tags = ['AI Agents']

    def get_queryset(self):
        return AgentTask.objects.all()

    @swagger_auto_schema(
        operation_summary='List agent tasks',
        operation_description='Returns all agent tasks. Filter by status using `?status=pending|running|completed|failed`.',
        tags=['AI Agents'],
        manual_parameters=[
            openapi.Parameter(
                'status',
                openapi.IN_QUERY,
                description='Filter tasks by status',
                type=openapi.TYPE_STRING,
                enum=['pending', 'running', 'completed', 'failed'],
                required=False,
            )
        ],
        responses={
            200: openapi.Response(
                'List of tasks',
                examples={'application/json': [_task_example]},
            )
        },
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary='Retrieve task details',
        operation_description=(
            'Returns the current status and output of a specific agent task.\n\n'
            '**Task statuses:** `pending` → `running` → `completed` | `failed`'
        ),
        tags=['AI Agents'],
        responses={
            200: openapi.Response(
                'Task details',
                examples={'application/json': {
                    **_task_example,
                    'status': 'completed',
                    'output_data': {
                        'result': 'Here is your AI-generated content...',
                    },
                }},
            ),
            404: openapi.Response('Task not found'),
        },
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
