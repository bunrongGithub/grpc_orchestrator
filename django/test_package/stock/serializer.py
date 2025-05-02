from rest_framework import serializers

from stock.models import StockModel
class StockSerializer(serializers.ModelSerializer):
    class Meta: 
        model=StockModel
        fields="__all__"