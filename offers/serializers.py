from rest_framework import serializers

from offers.models import Offers


class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offers
        ordering = ['id']
        fields = ["image"]
