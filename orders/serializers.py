from rest_framework import serializers

from orders.models import Orders


class OrderSerializer(serializers.ModelSerializer):
    product_image = serializers.ImageField(source='product.image')
    product_name = serializers.CharField(source='product.name')

    class Meta:
        model = Orders
        fields = ['id', 'product', 'total_price', 'payment_method', 'delivery_status', 'ordered_date', 'delivery_date',
                  'address', 'product_image', 'product_name', 'quantity']
