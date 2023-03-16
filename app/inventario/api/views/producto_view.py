from typing import Dict

from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status, serializers
from rest_framework.decorators import action
from rest_framework.response import Response

from app.inventario.models import Proveedor, Sede

from ..serializers import ProductoCreateSerializer, ProductoListarSerializer, UploadExcelSerializer
from ...models import Producto


class ProductoViewSet(viewsets.ModelViewSet):
    serializer_class = {
        'list': ProductoListarSerializer,
        'create': ProductoCreateSerializer,
        'default': ProductoListarSerializer
    }
    queryset = None

    view_permissions = {
        'create,destroy,update,retrieve,uploadExcel': {'admin': True, 'contador': True},
        'list': {'admin': True, 'contador': True}
    }

    def get_queryset(self):
        if self.queryset is None:
            return self.serializer_class.get('default').Meta.model.objects.all()
        return self.queryset

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.serializer_class.get('default'))

    def destroy(self, request, pk):
        estado = int(request.query_params.get("accion"))
        producto = get_object_or_404(Producto, pk=pk)
        producto.estado = estado
        producto.save()
        return Response({"estado": estado}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def uploadExcel(self, request):
        productos = []
        for data in request.data:
            proveedor = get_object_or_404(Proveedor, pk=data['proveedor'])
            sede = get_object_or_404(Sede, pk=data['sede'])
            productos.append(Producto(
                proveedor=proveedor, sede=sede, nombre=data['nombre'],
                descripcion=data['descripcion'],cantidad=data['cantidad'],
                preciocompra=data['preciocompra'], precioventa=data['precioventa'],
                industria=data['industria'], garantia=data['garantia'], marca=data['marca']
                ))
        Producto.objects.bulk_create(productos)
        return Response({"massege": "enviado"})
