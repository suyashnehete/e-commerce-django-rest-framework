from django.db import models

from core.models import User
from products.models import Product


class Cart(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    count = models.IntegerField()
