from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from ..serializers import UserCreateSerializer, UserListSerializer
from app.users.models import User


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = {
        'list': UserListSerializer,
        'create': UserCreateSerializer,
        'default': UserListSerializer
    }

    queryset = None

    view_permissions = {
        'list,create,retrieve,update,destroy': {'admin': True, 'contador': False, 'asesor': False}
    }

    def get_queryset(self):
        if self.queryset is None:
            return self.serializer_class.get('default').Meta.model.objects.exclude(usertype='anon')
        return self.queryset

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.serializer_class.get('default'))


    def destroy(self, request, pk):
        estado = int(request.query_params.get("accion"))
        usuario = get_object_or_404(User, pk=pk)
        usuario.is_active = estado
        usuario.save()
        return Response({"estado": estado})
