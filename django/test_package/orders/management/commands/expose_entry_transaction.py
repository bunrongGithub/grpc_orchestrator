
from django.core.management.base import BaseCommand
from grpc_orchestrator.core.orchestrator import serve
class Command(BaseCommand):
    def handle(self, *args, **options):
        serve()