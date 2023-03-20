from django.contrib.auth import authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework import serializers


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    pass


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(request=self.context['request'], **attrs)
        if not user:
            raise serializers.ValidationError('Invalid credentials')
        if not user.is_active:
            raise serializers.ValidationError('User is not active')
        return {'user': user}
