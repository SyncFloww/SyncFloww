from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    
    # API Routes
    path('api/users/', include('users.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/social/', include('social.urls')),      # Custom social endpoints
    path('api/brands/', include('social.urls')),      # Brands handled by social app too, roughly
    path('api/ai/', include('ai_agents.urls')),
]
