from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create custom business permissions"

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS(
                "Permission seeding command is ready."
            )
        )