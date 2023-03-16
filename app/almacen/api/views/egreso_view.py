from django.shortcuts import get_object_or_404

from rest_framework import viewsets, status
from rest_framework.response import Response


from ...models.Egreso import Egreso
from ...models.DetalleEgreso import DetalleEgreso

from app.inventory.models import Product
from ..serializers import EgresoSerializer


class EgresoViewSet(viewsets.GenericViewSet):
    serializer_class = EgresoSerializer
    queryset = EgresoSerializer.Meta.model.objects.all()

    view_permissions = {
        'create': {'admin': True, 'contador': True, 'asesor': True}
    }

    def create(self, request) -> Response:
        egress = Egreso.objects.create()
        data = request.data['detalleEgreso']
        productos = []
        cantidad = []
        detalle_egresos = []
        for detalle in data:
            producto = get_object_or_404(Product, pk=int(detalle['producto']))
            unidades = int(detalle['stock'])
            if producto.stock > 0:
                producto.stock -= unidades
                detalle_egreso = DetalleEgreso(producto=producto, egreso=egress, cantidad=unidades)
                productos.append(producto)
                cantidad.append(unidades)
                detalle_egresos.append(detalle_egreso)
        Product.objects.bulk_update(productos, fields=['stock'])
        DetalleEgreso.objects.bulk_create(detalle_egresos)
        return Response({"accion": "Recibido"}, status=status.HTTP_200_OK)
