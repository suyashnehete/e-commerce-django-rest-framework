from django.db import models

from core.models import User
from products.models import Product


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    total_price = models.IntegerField()
    payment_method = models.CharField(max_length=30)
    delivery_status = models.CharField(max_length=20, choices=(
        ("Ordered", "Ordered"), ("Processing Order", "Processing Order"), ("Out For Delivery", "Out For Delivery"),
        ("Delivered", "Delivered"), ("Canceled", "Canceled")), default="Ordered")
    ordered_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateTimeField()
    address = models.TextField()
    quantity = models.IntegerField()

