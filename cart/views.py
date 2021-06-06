from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cart.models import Cart
from cart.serializers import CartSerializer
from products.models import Product


class CartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = Cart.objects.filter(user=request.user)
        cart_serializer = CartSerializer(cart, many=True)
        return Response(status=200, data=cart_serializer.data)

    def post(self, request):
        cart = Cart.objects.create(
            user=request.user,
            product=Product.objects.get(id=int(request.data["product"])),
            count=int(request.data["count"])
        )
        return Response(status=200, data=CartSerializer(cart).data)

    def put(self, request):
        print(request.data)
        cart = Cart.objects.get(id=request.data["id"])
        if request.data["fromFunction"] == 'true':
            cart.count += int(request.data["count"])
        else:
            cart.count = int(request.data["count"])

        cart.save()
        return Response()

    def delete(self, request):
        cart = Cart.objects.get(id=request.data["id"])
        cart.delete()
        return Response()
