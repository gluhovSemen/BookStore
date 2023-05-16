from django.contrib.auth.models import User
from rest_framework import serializers

from django.conf import settings


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ("username", "password", "email")


class ClientLoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ("username", "password")


class ClientCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ("username", "password", "email", "first_name", "last_name")

    def create(self, validated_data):
        password = validated_data.pop("password")
        client = settings.AUTH_USER_MODEL(**validated_data)
        client.set_password(password)
        client.save()
        return client
