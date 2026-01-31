from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    RegisterView,
    LoginView,
    LogoutView,
    CurrentUserView,
    GoogleOAuthView,
    FacebookOAuthView,
    AppleOAuthView,
    ProfileViewSet,
    PasswordResetView,
)

router = DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile')

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', CurrentUserView.as_view(), name='current_user'),
    path('auth/password-reset/', PasswordResetView.as_view(), name='password_reset'),
    
    # Social authentication endpoints
    path('auth/google/', GoogleOAuthView.as_view(), name='google_oauth'),
    path('auth/facebook/', FacebookOAuthView.as_view(), name='facebook_oauth'),
    path('auth/apple/', AppleOAuthView.as_view(), name='apple_oauth'),
    
    # Profile endpoints
    path('', include(router.urls)),
]
