from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from user.serializers import UserCreateSerializer, UserLoginSerializer


class UserRegistration(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


class UserLogin(GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return Response({"message": "Login successful"})
        return Response(
            {"message": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
        )


class UserLogout(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Logout successful"})
