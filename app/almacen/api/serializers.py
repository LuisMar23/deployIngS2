from rest_framework import serializers
from ..models import Egreso, DetalleEgreso
from app.inventory.api.serializers import ProductCreateSerializer

class EgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Egreso
        fields = "__all__"

class DetalleEgresoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetalleEgreso
        fields = "__all__"
