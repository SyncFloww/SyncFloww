from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Brand, SocialAccount
from .serializers import BrandSerializer, SocialAccountSerializer

class BrandViewSet(viewsets.ModelViewSet):
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Brand.objects.filter(user=self.request.user)

    @action(detail=True, methods=['get'], url_path='social-accounts')
    def social_accounts(self, request, pk=None):
        brand = self.get_object()
        accounts = SocialAccount.objects.filter(brand=brand)
        serializer = SocialAccountSerializer(accounts, many=True)
        return Response(serializer.data)


class SocialAccountViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]
    queryset = SocialAccount.objects.none() # Placeholder

    def get_queryset(self):
        return SocialAccount.objects.filter(user=self.request.user)

    @action(detail=False, methods=['post'], url_path='connect/(?P<platform>[^/.]+)')
    def connect(self, request, platform=None):
        # Placeholder for OAuth connect logic
        # In real app, this would redirect to OAuth provider or handle code exchange
        return Response({'status': 'initiated', 'platform': platform, 'url': 'http://mock-oauth-url.com'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['delete'])
    def disconnect(self, request, pk=None):
        try:
            account = self.get_queryset().get(pk=pk)
            account.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except SocialAccount.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
