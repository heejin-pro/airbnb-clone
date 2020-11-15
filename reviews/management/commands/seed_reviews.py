import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models
from reviews import models as review_models


class Command(BaseCommand):

    help = "This Command is Create Many Sample Reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many reviews do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "accuracy": lambda x: random.randint(0, 5),
                "communication": lambda x: random.randint(0, 5),
                "cleanliness": lambda x: random.randint(0, 5),
                "location": lambda x: random.randint(0, 5),
                "check_in": lambda x: random.randint(0, 5),
                "value": lambda x: random.randint(0, 5),
                "user": lambda x: random.choice(users),
                "room": lambda x: random.choice(rooms),
            },
        )

        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Riviews created!"))
