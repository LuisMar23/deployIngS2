
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response


from ..serializers import SaleListSerializer, SaleDetailCreate


class SaleViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post']
    serializer_class = {    
        'list': SaleListSerializer,    
        'create': SaleDetailCreate,    
        'default': SaleListSerializer
        }
    view_permissions = {
        'create,list': {'admin': True, 'contador': True},
    }
    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            return self.serializer_class.get('default').Meta.model.objects.all()

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.serializer_class.get('default'))

    def create(self, request: Request, *args, **kwargs):
        sale_serializer = self.get_serializer_class()(data=request.data)
        sale_serializer.is_valid(raise_exception=True)
        sale_serializer.save()
        return Response({"message": "venta realizada con exito"})

