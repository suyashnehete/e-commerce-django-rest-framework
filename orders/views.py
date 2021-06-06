from datetime import timedelta

from django.utils import timezone
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from orders.models import Orders
from orders.serializers import OrderSerializer
from products.models import Product


class OrderView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        order = Orders.objects.get(id=id)
        order_serializer = OrderSerializer(order)
        return Response(status=200, data=order_serializer.data)


class OrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        order = Orders.objects.filter(user=request.user)
        order_serializer = OrderSerializer(order, many=True)
        return Response(status=200, data=order_serializer.data)

    def post(self, request):
        for cart in Cart.objects.filter(user=request.user,
                                        product=Product.objects.get(id=int(request.data["product"]))):
            cart.delete()

        product = Product.objects.get(id=int(request.data["product"]))
        product.stock -= int(request.data["quantity"])
        product.save()
        order = Orders.objects.create(
            user=request.user,
            product=product,
            total_price=request.data["total_price"],
            payment_method=request.data["payment_method"],
            ordered_date=timezone.now(),
            delivery_date=timezone.now() + timedelta(days=6),
            address=request.data["address"],
            quantity=int(request.data["quantity"]),
        )
        order.save()
        return Response()

    def put(self, request):
        order = Orders.objects.get(id=int(request.data["id"]))
        product = Product.objects.get(id=order.product.id)
        product.stock += order.quantity
        product.save()
        order.delivery_status = "Canceled"
        order.save()
        return Response()
