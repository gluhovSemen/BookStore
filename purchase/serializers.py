from rest_framework import serializers
from .models import Purchase


class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = "__all__"


class PurchaseSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = ["book", "quantity", "price"]
