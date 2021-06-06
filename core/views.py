from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from core.models import User, Address
from core.serializers import UserSerializer, AddressSerializer


class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        token = generate_token(user)
        return Response({
            'image': user.image.url,
            'name': user.first_name,
            'email': user.email,
            'phone': user.phone,
            'token': "Token " + str(token),
        }, status=200)


class LoginView(APIView):

    def post(self, request):
        user = User.objects.filter(username=request.data["email"])
        if len(user) == 0:
            return Response(status=404, data={"detail": "Email Not Found"})

        user = authenticate(username=request.data["email"], password=request.data["password"])
        if user is not None:
            token = generate_token(user)
            return Response({
                'image': user.image.url,
                'name': user.first_name,
                'email': user.email,
                'phone': user.phone,
                'token': "Token " + str(token),
            }, status=200)
        else:
            return Response(status=409, data={"detail": "Invalid Password"})


class RegisterView(APIView):
    def post(self, request):
        user = User.objects.filter(username=request.data["email"])
        if len(user) != 0:
            return Response(status=409, data={"detail": "Username Already Exists."})
        user = User.objects.filter(email=request.data["email"])
        if len(user) != 0:
            return Response(status=409, data={"detail": "Email Already Exists."})
        if len(request.data["password"]) < 8:
            return Response(status=409, data={"detail": "Password Length Should Be Greater Than 7"})

        user = UserSerializer().create(request.data)
        token = generate_token(user)
        return Response({
            'image': user.image.url,
            'name': user.first_name,
            'email': user.email,
            'phone': user.phone,
            'token': "Token " + str(token),
        }, status=200)


class UpdateView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        UserSerializer().update(validated_data=request.data, instance=request.user)
        user = request.user
        token = generate_token(user)
        return Response({
            'image': user.image.url,
            'name': user.first_name,
            'email': user.email,
            'phone': user.phone,
            'token': "Token " + str(token),
        }, status=200)


def generate_token(user):
    try:
        token = Token.objects.get(user_id=user.id)
    except Token.DoesNotExist:
        token = Token.objects.create(user=user)
    return token


class AddressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        addresses = Address.objects.filter(user=request.user)
        return Response(data=AddressSerializer(addresses, many=True).data)

    def post(self, request):
        address = Address.objects.create(
            user=request.user,
            name=request.data["name"],
            phone=request.data["phone"],
            address=request.data["address"],
            pin=request.data["pin"]
        )
        address.save()
        return Response()

    def put(self, request):
        address = Address.objects.get(id=request.data["id"])
        address.name = request.data["name"]
        address.phone = request.data["phone"]
        address.address = request.data["address"]
        address.pin = request.data["pin"]
        address.save()
        return Response()

    def delete(self, request):
        Address.objects.get(id=request.data["id"]).delete()
        return Response()
