from django.shortcuts import render
from rest_framework import viewsets

from product.serializer import ProductSerializer

from product.models import ProductModel
class ProductViewSet(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=ProductModel.objects.all()