from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404

from rest_framework.request import Request
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from app.users.api.serializers import UserListSerializer
from app.users.models import User
from ..serializers import CustomTokenObtainPairSerializer, LoginSerializer


class AuthenticationViewSet(viewsets.GenericViewSet, TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @action(detail=False, methods=['post'])
    def login(self, request: Request):
        login_serializer = LoginSerializer(data=request.data, context={'request': request})
        login_serializer.is_valid(raise_exception=True)
        token_serializer = self.serializer_class(data=request.data)
        token_serializer.is_valid(raise_exception=True)
        user = login_serializer.validated_data.get('user')
        return Response({
            "access": token_serializer.validated_data.get('access'),
            "refresh": token_serializer.validated_data.get('refresh'),
            "user": {
                "username": user.username,
                "usertype": user.usertype
            }

        })

    @action(detail=False, methods=['post'])
    def logout(self, request):
        user = get_object_or_404(User, pk=int(request.data.get('user', '')))
        RefreshToken.for_user(user=user)
        return Response({"message": "Sesion cerrada correctamente"}, status=status.HTTP_200_OK)
