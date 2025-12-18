from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AIAgentViewSet, AgentTaskViewSet

router = DefaultRouter()
router.register(r'agents', AIAgentViewSet, basename='agent')
router.register(r'tasks', AgentTaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
]
