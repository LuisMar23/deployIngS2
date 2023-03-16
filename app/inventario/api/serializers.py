from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from ..models import Sede, Producto, Proveedor


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = "__all__"


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sede
        fields = "__all__"


class ProductoCreateSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required=False)
    class Meta:
        model = Producto
        fields = '__all__'

class ProductoListarSerializer(serializers.ModelSerializer):
    sede = serializers.StringRelatedField()
    proveedor = serializers.StringRelatedField()
    class Meta:
        model = Producto
        exclude = ('usuario',)

class UploadExcelSerializer(serializers.ListField):
    class Meta:
        model=Producto
        fields='__all__'