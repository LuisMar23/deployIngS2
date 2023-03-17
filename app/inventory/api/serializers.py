from abc import ABC

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


class ProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductListSerializer(serializers.ListSerializer):
    child = ProductSerializer()

    def create(self, validated_data):
        return [Product(**item) for item in validated_data]
    # sede = serializers.StringRelatedField()
    # proveedor = serializers.StringRelatedField()
    #
    # class Meta:
    #     model = Product
    #     exclude = ('user',)


class UploadExcelSerializer(serializers.Serializer):
    data = ProductListSerializer()
