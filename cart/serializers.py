from rest_framework import serializers

from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):
    product_price = serializers.IntegerField(source='product.price')
    product_name = serializers.CharField(source='product.name')
    product_image = serializers.ImageField(source='product.image')

    class Meta:
        model = Cart
        fields=['id', 'product', 'count', 'product_price', 'product_name', 'product_image']


