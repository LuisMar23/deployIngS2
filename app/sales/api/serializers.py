from rest_framework import serializers

from app.sales.models import Sales, SaleDetail, IncomeDetail, Income


class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        exclude = ('date_created',)


class SaleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleDetail
        fields = '__all__'
