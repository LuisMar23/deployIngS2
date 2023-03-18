from django.db import transaction

from rest_framework import viewsets
from rest_framework.request import Request

from ..serializers import SaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = {
        'list': SaleSerializer,
        'create': SaleSerializer,
        'default': SaleSerializer
    }

    queryset = None

    def get_queryset(self):
        if self.queryset is None:
            return self.serializer_class.get('default').Meta.model.objects.all()

    def get_serializer_class(self):
        return self.serializer_class.get(self.action, self.serializer_class.get('default'))

    def create(self, request, *args, **kwargs):
        pass

    def list(self, request, *args, **kwargs):
        pass

