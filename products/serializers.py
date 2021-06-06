from rest_framework import serializers

from category.models import Category
from products.models import Product, ProductImage, ProductHighlights, ProductReviews


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField()

    class Meta:
        model = Product
        fields = "__all__"


class ProductWishlistSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='product.id')
    name = serializers.CharField(source='product.name')
    price = serializers.IntegerField(source='product.price')
    description = serializers.CharField(source='product.description')
    stock = serializers.IntegerField(source='product.stock')
    rating = serializers.FloatField(source='product.rating')
    category = serializers.CharField(source='product.category')
    image = serializers.ImageField(source='product.image')
    sold_by = serializers.CharField(source='product.sold_by')
    warranty_summary = serializers.CharField(source='product.warranty_summary')
    covered_in_warranty = serializers.CharField(source='product.covered_in_warranty')
    not_covered_in_warranty = serializers.CharField(source='product.not_covered_in_warranty')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description', 'stock', 'rating', 'category', 'image', 'sold_by',
                  'not_covered_in_warranty', 'covered_in_warranty', 'warranty_summary']


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductHighlightsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductHighlights
        fields = ['image', 'title', 'description']


class ProductReviewsSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.first_name")

    class Meta:
        model = ProductReviews
        fields = ['id', 'rating', 'user', 'description']
