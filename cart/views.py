from rest_framework import generics, status
from rest_framework.generics import DestroyAPIView, CreateAPIView
from rest_framework.response import Response

from book.models import Book
from cart.models import Cart, CartItem
from cart.serializers import CartItemSerializer, CartItemSerializerLong
from utils.permissions import IsOwner


class CartItemListAPIView(generics.ListAPIView):
    """Shows the cart of the certain User"""

    permission_classes = [IsOwner]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(cart__customer=user)


class CartItemDeleteView(DestroyAPIView):
    """Deletes the CartItem from a certain User by the book id"""

    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(cart__customer=user)

    def get_object(self):
        book_id = self.kwargs["book_id"]
        queryset = self.get_queryset()
        obj = queryset.filter(book__id=book_id).first()
        return obj


class CartItemCreateView(CreateAPIView):
    """Creates a CartItem with the given book.id"""

    serializer_class = CartItemSerializerLong
    permission_classes = [IsOwner]

    def post(self, request, *args, **kwargs):
        book_id = request.data.get("book_id")
        quantity = request.data.get("quantity")

        # Ensure book_id and quantity are provided
        if not all([book_id, quantity]):
            return Response(
                {"error": "book_id and quantity are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response(
                {"error": "Invalid book_id."}, status=status.HTTP_400_BAD_REQUEST
            )

        cart = Cart.objects.get(customer=request.user)

        cart_item = CartItem.objects.create(
            cart=cart, book=book, quantity=quantity, price=book.price
        )

        serializer = CartItemSerializerLong(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
