from django.contrib.auth.models import User, AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    pin = models.CharField(max_length=6)

    def __str__(self):
        return self.user
