import random

from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product, ProductImage, ProductHighlights, ProductReviews, ProductWishlist
from products.serializers import ProductSerializer, ProductImageSerializer, ProductHighlightsSerializer, \
    ProductReviewsSerializer, ProductWishlistSerializer


class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'category__name', 'description', 'sold_by']


class Wishlist(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductWishlistSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['product__name', 'product__category__name', 'product__description', 'product__sold_by']

    def get_queryset(self):
        return ProductWishlist.objects.all().filter(user=self.request.user)


class tp(APIView):
    def get(self, request):
        return Response(data=ProductWishlist.objects.raw("select * from products_productwishlist"))


class TopProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        lst = random.sample(range(0, len(products)), 4)
        data1 = ProductSerializer(products[lst[0]]).data
        data2 = ProductSerializer(products[lst[1]]).data
        data3 = ProductSerializer(products[lst[2]]).data
        data4 = ProductSerializer(products[lst[3]]).data
        return Response(status=200, data=[data1, data2, data3, data4])


class TrendingProductView(APIView):
    def get(self, request):
        products = Product.objects.all()
        lst = random.sample(range(0, len(products)), 5)
        data1 = ProductSerializer(products[lst[0]]).data
        data2 = ProductSerializer(products[lst[1]]).data
        data3 = ProductSerializer(products[lst[2]]).data
        data4 = ProductSerializer(products[lst[3]]).data
        data5 = ProductSerializer(products[lst[4]]).data
        return Response(status=200, data=[data1, data2, data3, data4, data5])


class ProductImageView(APIView):
    def get(self, request, id):
        images = ProductImage.objects.filter(product=id)
        return Response(status=200, data=ProductImageSerializer(images, many=True).data)


class ProductHighlightsView(APIView):
    def get(self, request, id):
        highlights = ProductHighlights.objects.filter(product=id)
        return Response(status=200, data=ProductHighlightsSerializer(highlights, many=True).data)


class ProductReviewView(APIView):
    def get(self, request, id):
        reviews = ProductReviews.objects.filter(product=Product.objects.get(id=int(id)))
        return Response(status=200, data=ProductReviewsSerializer(reviews, many=True).data)


class ProductRetrive(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'


class ProductReviewRetrive(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        reviews = ProductReviews.objects.filter(product=Product.objects.get(id=int(id)), user=request.user)
        if len(reviews) != 0:
            return Response(status=200, data=ProductReviewsSerializer(reviews[0]).data)
        else:
            return Response(data={"id": 0, "rating": 1.0, "user": "", "description": ""})

    def post(self, request, id):
        product = Product.objects.get(id=id)
        reviews = ProductReviews.objects.create(
            user=request.user,
            product=product,
            description=request.data['description'],
            rating=float(request.data['rating']),
        )

        reviews.save()
        rating = 0
        for i in ProductReviews.objects.filter(product=product):
            rating += i.rating
        product.rating = rating / len(ProductReviews.objects.filter(product=product))
        product.save()

        return Response()

    def put(self, request, id):
        product = Product.objects.get(id=id)

        review = ProductReviews.objects.get(id=int(request.data['id']))
        review.description = request.data['description']
        review.rating = float(request.data['rating'])
        review.save()

        rating = 0
        for i in ProductReviews.objects.filter(product=product):
            rating += i.rating
        product.rating = rating / len(ProductReviews.objects.filter(product=product))
        product.save()

        return Response()


class WishlistView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        wishlist = ProductWishlist.objects.filter(user=request.user, product=Product.objects.get(id=id))
        if len(wishlist) == 0:
            return Response(data=0)
        else:
            return Response(data=wishlist[0].id)

    def post(self, request, id):
        ProductWishlist.objects.create(user=request.user, product=Product.objects.get(id=id)).save()
        return Response()

    def delete(self, request, id):
        ProductWishlist.objects.get(id=id).delete()
        return Response()
