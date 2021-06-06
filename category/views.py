from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from category.models import Category
from category.serializers import CategorySerializer
import random


class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class TopCategoryView(APIView):
    def get(self, request):
        categories = Category.objects.all();
        lst = random.sample(range(0, len(categories)), 4)
        data1 = CategorySerializer(categories[lst[0]]).data
        data2 = CategorySerializer(categories[lst[1]]).data
        data3 = CategorySerializer(categories[lst[2]]).data
        data4 = CategorySerializer(categories[lst[3]]).data
        return Response(status=200, data=[data1, data2, data3, data4])