from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet, SocialAccountViewSet

router = DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brand')
# Social endpoints are custom actions or handled by viewset.
# We map SocialAccountViewSet manually-ish or use router if it fits.
# The README paths were:
# /api/brands/ -> router
# /api/brands/{id}/social-accounts/ -> router action
# /api/social/connect/{platform}/ -> custom
# /api/social/{id}/disconnect/ -> custom

urlpatterns = [
    path('', include(router.urls)),
    path('social/connect/<str:platform>/', SocialAccountViewSet.as_view({'post': 'connect'}), name='social-connect'),
    path('social/<int:pk>/disconnect/', SocialAccountViewSet.as_view({'delete': 'disconnect'}), name='social-disconnect'),
]
