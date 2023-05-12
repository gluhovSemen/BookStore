from rest_framework import serializers

from book.serializers import BookShortSerializer
from cart.models import CartItem


class CartItemSerializer(serializers.ModelSerializer):
    book = BookShortSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = "__all__"


class CartItemSerializerLong(serializers.ModelSerializer):
    book_id = serializers.CharField(source="book.id")

    class Meta:
        model = CartItem
        fields = ["id", "book_id", "quantity", "price"]


class CartItemSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["book", "quantity", "price"]
