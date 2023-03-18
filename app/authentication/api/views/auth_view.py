from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from app.users.api.serializers import UserListSerializer
from app.users.models import User
from ..serializers import CustomTokenObtainPairSerializer


class AuthenticationViewSet(viewsets.GenericViewSet, TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    @action(detail=False, methods=['post'])
    def login(self, request):
        user = authenticate(request=request, **request.data)
        if user is not None:
            token_serializer = self.serializer_class(data=request.data)
            token_serializer.is_valid(raise_exception=True)
            user_serializer = UserListSerializer(user)
            print(user_serializer.data)
            return Response({'message': 'user authenticated'})
        return Response({'message': 'credential invalids'})
        # try:
        #     login_serializer = self.serializer_class(data=request.data)
        #     login_serializer.is_valid(raise_exception=True)
        #     user_serializer = UserListSerializer(user)
        #     user_serializer.is_valid(raise_exception=True)
        #     return Response(
        #         {
        #             "access": login_serializer.validated_data.get('access'),
        #             "refresh": login_serializer.validated_data.get('refresh'),
        #             "message": "Usuario autenticado correctamente",
        #             "user": user_serializer.validated_data
        #         },
        #         status=status.HTTP_200_OK
        #     )
        # except:
        #     return Response({"message": "Credenciales invalidas"}, status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=False, methods=['post'])
    def logout(self, request):
        user = get_object_or_404(User, pk=int(request.data.get('user', '')))
        RefreshToken.for_user(user=user)
        return Response({"message": "Sesion cerrada correctamente"}, status=status.HTTP_200_OK)
