from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from offers.models import Offers
from offers.serializers import OfferSerializer


class OffersView(APIView):

    def get(self, request):
        offers = Offers.objects.all()
        return Response(status=200, data=OfferSerializer(offers, many=True).data)
