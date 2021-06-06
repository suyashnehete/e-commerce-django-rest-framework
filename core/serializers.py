from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework.validators import UniqueValidator

from core.models import User, Address


class UserSerializer(Serializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    def update(self, instance, validated_data):
        if validated_data.get('file', None) is not None:
            user = User.objects.update(
                first_name=validated_data['name'],
                phone=validated_data['phone'],
                image=validated_data['file'],
            )
        else:
            user = User.objects.update(
                first_name=validated_data['name'],
                phone=validated_data['phone'],
            )

        return user

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['name'],
            phone=validated_data['phone'],
            image=validated_data['file'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['name', 'id', 'phone', 'address', 'pin']
