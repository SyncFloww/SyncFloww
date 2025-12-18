from rest_framework import serializers
from .models import Brand, SocialAccount

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'
        read_only_fields = ['user', 'created_at', 'updated_at']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)


class SocialAccountSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name', read_only=True)

    class Meta:
        model = SocialAccount
        fields = ['id', 'platform', 'username', 'display_name', 'profile_image_url', 'brand', 'brand_name', 'is_active', 'created_at']
        read_only_fields = ['id', 'user', 'platform', 'username', 'display_name', 'profile_image_url', 'is_active', 'created_at']
