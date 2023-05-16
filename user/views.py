from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.conf import settings
from user.models import Client
from user.serializers import ClientCreateSerializer, ClientLoginSerializer


class ClientRegistration(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientCreateSerializer


class ClientLogin(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ClientLoginSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        client = authenticate(request, username=username, password=password)
        if client:
            login(request, client)
            return Response({"message": "Login successful"})
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})
