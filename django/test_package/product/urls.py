from django.urls import include, path
from rest_framework import routers
from product.views import ProductViewSet
route = routers.DefaultRouter()
route.register(r"products",ProductViewSet)
urlpatterns = [
    path('', include(route.urls)),
]
