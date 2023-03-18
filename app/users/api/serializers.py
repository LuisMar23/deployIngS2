from rest_framework import serializers
from ..models import User


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'last_login', 'is_superuser',)
        # fields = ('username', 'password',)

class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'name', 'last_name', 'usertype')

    def create(self, validated_data):
        if validated_data.get('usertype') == 'admin':
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)
