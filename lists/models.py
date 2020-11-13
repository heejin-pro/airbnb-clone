from django.db import models
from core import models as core_models


class List(core_models.TimeStampedModel):

    """ List Model Definitions """

    name = models.CharField(max_length=80)
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    rooms = models.ForeignKey("rooms.Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
