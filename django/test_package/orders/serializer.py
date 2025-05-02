from rest_framework import serializers

from product.serializer import ProductSerializer
from product.models import ProductModel
from orders.models import OrderModel
class OrderSerializer(serializers.ModelSerializer):
    saga_status=serializers.SerializerMethodField()
    class Meta:
        model=OrderModel
        fields="__all__"
    read_only_fields = ["status","transaction_id","saga_status","order_id"]
    def get_saga_status(self,obj):
        if not obj.transaction_id:
            return None
        if hasattr(self.context['request'],"saga_status"):
            return self.context['request'].saga_status
        try:
            from grpc_orchestrator.core.client.client import GrpcOrchestratorClient
            client = GrpcOrchestratorClient(orchestrator_host="localhost")
            return client.get_transaction_status(obj.transaction_id)
        except: 
            return None