from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from ..serializers import SupplierSerializer
from ...models import Supplier


class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    queryset = SupplierSerializer.Meta.model.objects.all()
    view_permissions = {
        'create,list,destroy,update':{'admin': True, 'contador':True}
    }
    def list(self, request:Request):
        print(request.data)
        proveedor_serializer = SupplierSerializer(Supplier.objects.all(), many=True)
        return Response(proveedor_serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request,pk=None):
        estado = int(request.query_params.get('accion'))
        proveedor = get_object_or_404(Supplier, id=pk)
        proveedor.is_active = True if estado == 1 else False
        proveedor.save()
        return Response({'estado': estado}, status=status.HTTP_200_OK)
