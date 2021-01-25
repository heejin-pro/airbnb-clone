from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)  # auto_now_add : 모델이 생성된 날짜를 구함
    update = models.DateTimeField(auto_now=True)  # auto_now : 새로운 날짜로 업데이트
    objects = managers.CustomModelManager()

    class Meta:
        abstract = True  # Table을 만들지 않는 Model
