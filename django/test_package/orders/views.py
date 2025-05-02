from django.shortcuts import render
from rest_framework import viewsets

from orders.serializer import OrderSerializer
from orders.models import OrderModel
class OrderViewSet(viewsets.ModelViewSet):
    """
    1- User make order by including product_id
    2- Create Transaction to product service by including the product id
    3- if transaction (2) success, then to go step check stock by make transaction to the stock app
    4- if all transaction success, user should recieve product
    5- Otherwise, if which of transaction failed, Should cancel order
    """
    queryset=OrderModel.objects.all()
    serializer_class=OrderSerializer

