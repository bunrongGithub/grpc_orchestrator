from django.core.management.base import BaseCommand
from grpc_orchestrator.service_base import run_participant_server
from orders.services.stock import StockService

class Command(BaseCommand):
    help = "Start the gRPC server"
    def handle(self, *args, **options):
        run_participant_server(service=StockService(),port=50052)
