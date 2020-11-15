import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models


class Command(BaseCommand):

    help = "This Command is Create Many Sample Rooms"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many rooms do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_user = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(
            room_models.Room,
            number,
            {
                "name": lambda x: seeder.faker.address(),
                "host": lambda x: random.choice(all_user),
                "room_type": lambda x: random.choice(room_types),
                "guests": lambda x: random.randint(0, 10),
                "price": lambda x: random.randint(0, 300),
                "beds": lambda x: random.randint(0, 5),
                "bedrooms": lambda x: random.randint(0, 5),
                "baths": lambda x: random.randint(0, 5),
            },
        )
        # 1. Room을 생성하고
        created_photos = seeder.execute()
        # 2 생성 후 가져온 Primary Key List를 깨끗히 정리
        created_clean = flatten(list(created_photos.values()))

        for pk in created_clean:
            room = room_models.Room.objects.get(pk=pk)
            # 3 사진 모델 생성
            for i in range(3, random.randint(10, 30)):
                room_models.Photo.objects.create(
                    caption=seeder.faker.sentence(),
                    room=room,
                    file=f"/room_photos/{random.randint(1,31)}.webp",
                )
            # 4 그 외에 ... Amenities, Facilities, House rules 추가
            amenities = room_models.Amenity.objects.all()
            for a in amenities:
                if random.randint(0, 15) % 2 == 0:
                    room.amenities.add(a)

            facilities = room_models.Facility.objects.all()
            for f in facilities:
                if random.randint(0, 15) % 2 == 0:
                    room.facilities.add(f)

            houseRules = room_models.HouseRule.objects.all()
            for h in houseRules:
                if random.randint(0, 15) % 2 == 0:
                    room.house_rules.add(h)

        self.stdout.write(self.style.SUCCESS(f"{number} Rooms created!"))
