import abc

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


class ProductCreateSerializer(serializers.ModelSerializer):
    imagen = Base64ImageField(required=False)

    class Meta:
        model = Product
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductListSerializer(serializers.ListSerializer):
    child = ProductSerializer()

    def create(self, validated_data):
        products = [Product(**item) for item in validated_data]
        Product.objects.bulk_create(products)
        return products

class UploadExcelSerializer(serializers.Serializer):
    data = ProductListSerializer()
