from django.shortcuts import render
from rest_framework import viewsets

from stock.models import StockModel
from stock.serializer import StockSerializer
class StockViewset(viewsets.ModelViewSet):
    serializer_class=StockSerializer
    queryset=StockModel.objects.all()