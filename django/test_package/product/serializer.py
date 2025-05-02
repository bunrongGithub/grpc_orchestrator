from rest_framework import serializers

from stock.serializer import StockSerializer
from stock.models import StockModel
from product.models import ProductModel


class ProductSerializer(serializers.ModelSerializer):
    stock = serializers.SerializerMethodField()
    class Meta:
        model = ProductModel
        fields = ["id", "name", "price", "description", "stock_id","stock"]

    def get_stock(self, obj):
        qs = StockModel.objects.get(id=obj.stock_id)
        return StockSerializer(qs).data