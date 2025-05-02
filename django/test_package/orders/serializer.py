from rest_framework import serializers

from product.serializer import ProductSerializer
from product.models import ProductModel
from orders.models import OrderModel
class OrderSerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model=OrderModel
        fields=["id","product_id","products"]

    def get_products(self,obj):
        instance = obj.product_id
        qs = ProductModel.objects.get(id=instance)
        return ProductSerializer(qs).data