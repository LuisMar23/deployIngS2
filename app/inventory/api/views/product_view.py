from django.shortcuts import get_object_or_404
from django.db import transaction

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request

from app.inventory.models import Supplier, BranchOffice

from ..serializers import ProductListSerializer, ProductSerializer
from ...models import Product


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = {
        'uploadExcel': ProductListSerializer,
        'default': ProductSerializer
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
        producto = get_object_or_404(Product, pk=pk)
        producto.is_active = estado
        producto.save()
        return Response({"estado": estado}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    @transaction.atomic()
    def uploadExcel(self, request: Request) -> Response:
        try:
            products_list_serializer = self.get_serializer_class()(data=request.data)
            products_list_serializer.is_valid(raise_exception=True)
            products_list_serializer.save()
        except Exception as e:
            transaction.set_rollback(True)
            return Response({"error": f"{e}"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "Products created successfully"}, status=status.HTTP_200_OK)
