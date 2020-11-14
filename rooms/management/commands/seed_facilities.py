from django.core.management.base import BaseCommand
from rooms.models import Facility


class Command(BaseCommand):

    help = "This Command Create Sample Facilities"

    def handle(self, *args, **options):
        facilities = [
            "Private entrance",
            "Paid parking on premises",
            "Paid parking off premises",
            "Elevator",
            "Parking",
            "Gym",
        ]

        for i in facilities:
            Facility.objects.create(name=i)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} Facilities Created!"))
