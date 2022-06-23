from django.db import models
from django.contrib.auth import get_user_model

from uuid import uuid4


User = get_user_model()

class Car(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    published = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avto = models.ForeignKey(Car, on_delete=models.CASCADE)
    booked_from = models.DateTimeField(auto_now=False)
    booked_to = models.DateTimeField(auto_now=False)