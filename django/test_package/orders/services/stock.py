from grpc_orchestrator.service_base import GrpcSagaTransactionParticipantBase
class StockService(GrpcSagaTransactionParticipantBase):
    def execute(self, request, context):
        return super().execute(request, context)
    def compensate(self, request, context):
        return super().compensate(request, context)