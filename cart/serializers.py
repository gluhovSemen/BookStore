from decimal import Decimal

from rest_framework import serializers

from book.models import Book
from book.serializers import BookShortSerializer
from cart.models import CartItem, Cart


class CartItemSerializer(serializers.ModelSerializer):
    book = BookShortSerializer(read_only=True)

    class Meta:
        model = CartItem
        fields = "__all__"


class CartItemSerializerShort(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ["book", "quantity", "price"]


class CartItemCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating a CartItem with the given book.id"""

    book_id = serializers.IntegerField(write_only=True)
    quantity = serializers.IntegerField(write_only=True)

    class Meta:
        model = CartItem
        fields = ["id", "book_id", "quantity"]

    def create(self, validated_data):
        book_id = validated_data.get("book_id")
        quantity = validated_data.get("quantity")
        book = Book.objects.get(id=book_id)
        cart = Cart.objects.get(customer=self.context["request"].user)
        price = book.price * Decimal(quantity)
        cart_item = CartItem.objects.create(
            cart=cart, book=book, quantity=quantity, price=price
        )
        return cart_item
