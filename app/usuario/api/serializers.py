from rest_framework import serializers
from ..models import Usuario


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ('password', 'last_login', 'is_superuser',)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ('username', 'password', 'nombre', 'apellido', 'usertype')

    def create(self, validated_data):
        if validated_data.get('usertype') == 'admin':
            return Usuario.objects.create_superuser(**validated_data)
        return Usuario.objects.create_user(**validated_data)
