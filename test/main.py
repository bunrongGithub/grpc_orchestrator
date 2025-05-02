from grpc_orchestrator import service_base


class ServiceOrder(service_base.GrpcSagaTransactionParticipantBase):
    def execute(self, request, context):
        return super().execute(request, context)

    def compensate(self, request, context):
        return super().compensate(request, context)


if __name__ == "__main__":
    service_base.run_participant_server(ServiceOrder(), 50052)


from grpc_orchestrator.core.client.client import GrpcOrchestratorClient

client = GrpcOrchestratorClient(orchestrator_host="localhost")
steps = [
    {
        "port": 50052,
        "rpc_method": "CleateOrder",
        "compensation_method": "RollbackOrder",
        "timeout_seconds": 5,
    },
    {
        "port": 50052,
        "rpc_method": "CheckoutOrder",
        "compensation_method": "CheckoutOrder",
        "timeout_seconds": 5,
    },
]
client.start_transaction(transaction_id="1234",steps=steps,payload={
    "id": "1",
    "name":"item1"
})
