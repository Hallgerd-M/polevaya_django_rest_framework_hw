from django.core.management import call_command
from django.core.management.base import BaseCommand


class PamentsCommand(BaseCommand):
    help = "Add payments"

    def handle(self, *args, **kwargs):
        call_command("load_data", "payments_fixture.json")
        self.stdout.write(self.style.SUCCESS("Data from fixture successfully loaded"))
