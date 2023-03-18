from rest_framework import serializers

from app.sales.models import Sales, SaleDetail, IncomeDetail, Income
from app.inventory.api.serializers import ProductSerializer


class SaleSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Sales
        exclude = ('date_created',)



class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        exclude = ('sale',)


class SaleDetailListSerializer(serializers.ListSerializer):
    child = SaleDetailSerializer()


class SaleDetailCreate(serializers.Serializer):
    detail = SaleDetailListSerializer()
    sale = SaleSerializer()

    def create(self, validated_data):
        sale = Sales.objects.create(**validated_data.get('sale'))
        sale_detail = [SaleDetail(sale=sale, **item) for item in validated_data.get('detail')]
        SaleDetail.objects.bulk_create(sale_detail)
        return sale_detail
