

from django.urls import include, path
from rest_framework import routers
from orders.views import OrderViewSet

route = routers.DefaultRouter()
route.register(r"orders",OrderViewSet)
urlpatterns = [
    path('', include(route.urls)),
]
