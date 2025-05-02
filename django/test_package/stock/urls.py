from rest_framework import routers

from stock.views import StockViewset


route = routers.DefaultRouter()
route.register(r"stock",viewset=StockViewset)


from django.urls import include, path, re_path
urlpatterns = [
    path("",include(route.urls))
]