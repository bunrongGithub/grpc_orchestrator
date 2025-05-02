import uuid
from django.shortcuts import render
from requests import Response
from rest_framework import viewsets, status
from grpc_orchestrator.core.client.client import GrpcOrchestratorClient
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

    queryset = OrderModel.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "order_id"

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        order = OrderModel.objects.create(
            order_id=str(uuid.uuid4()), items=serializer.validated_data.get("items", [])
        )
        try:
            client = GrpcOrchestratorClient(orchestrator_host="localhost",orchestrator_port=50051) #Connect to base port 
            steps = [
                {
                    "port": 50053,
                    "rpc_method": "order_product",
                    "compensation_method": "order_product",
                    "timeout_seconds": 5,
                },
                {
                    "port": 50052,
                    "rpc_method": "check_stock",
                    "compensation_method": "check_stock",
                    "timeout_seconds": 5,
                },
            ]
            saga_response = client.start_transaction(
                transaction_id=order.order_id,
                steps=steps,
                # payload={"order_id": order.order_id, "items": order.items},
            )
            order.transaction_id=saga_response.get("sagaId","")
            if order.transaction_id:
                saga_response_status = client.get_transaction_status(transaction_id=order.transaction_id)
                print(saga_response)
            return Response(
                OrderSerializer(order).data,
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            print(e)
