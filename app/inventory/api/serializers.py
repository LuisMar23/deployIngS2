from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from ..models import BranchOffice, Product, Supplier


class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = "__all__"


class SedeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
        fields = "__all__"


class ProductoCreateSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required=False)
    class Meta:
        model = Product
        fields = '__all__'

class ProductoListarSerializer(serializers.ModelSerializer):
    sede = serializers.StringRelatedField()
    proveedor = serializers.StringRelatedField()
    class Meta:
        model = Product
        exclude = ('users',)

class UploadExcelSerializer(serializers.ListField):
    class Meta:
        model=Product
        fields='__all__'
