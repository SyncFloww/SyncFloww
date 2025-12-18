from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileViewSet

router = DefaultRouter()
# /users/me/ is handled by the action, but generic routing helps if we expand
# router.register(r'', ProfileViewSet, basename='user') 

urlpatterns = [
    # Explicit 'me' endpoint path if we want strictly /api/users/me/
    # But ViewsSet @action usually does /users/me/. 
    # Let's use the router for standard ViewSet pattern if possible, 
    # but ProfileViewSet is designed as singleton-like for 'me' mostly.
    
    path('me/', ProfileViewSet.as_view({'get': 'me', 'put': 'me'}), name='user-me'),
    path('me/brands/', ProfileViewSet.as_view({'get': 'brands'}), name='user-brands'), # Placeholder if we add brands action later
]
