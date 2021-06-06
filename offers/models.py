from django.db import models


class Offers(models.Model):
    image = models.ImageField(upload_to="media/")
