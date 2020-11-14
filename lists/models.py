from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """ List Model Definitions """

    name = models.CharField(max_length=80)
    user = models.ForeignKey(
        "users.User", related_name="lists", on_delete=models.CASCADE
    )
    rooms = models.ManyToManyField("rooms.Room", related_name="lists")

    def count_rooms(self):
        return self.rooms.count()

    count_rooms.short_description = "Number Of Rooms"

    def __str__(self):
        return self.name
