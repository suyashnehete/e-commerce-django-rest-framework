from django.db import models

from category.models import Category
from core.models import User


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    stock = models.IntegerField()
    rating = models.FloatField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")
    sold_by = models.CharField(max_length=50)
    warranty_summary = models.CharField(max_length=30)
    covered_in_warranty = models.CharField(max_length=30)
    not_covered_in_warranty = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")


class ProductHighlights(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/")
    title = models.CharField(max_length=30)
    description = models.TextField()


class ProductReviews(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    description = models.TextField()


class ProductWishlist(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
