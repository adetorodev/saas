from django.core.management.commands import BaseCommand

class Command(BaseCommand):

    def handle(self, *args: Any, **options: Any):
        print("Hello world")