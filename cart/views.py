from rest_framework import generics, status, permissions
from rest_framework.generics import DestroyAPIView, CreateAPIView
from rest_framework.response import Response

from cart.models import CartItem
from cart.serializers import (
    CartItemSerializer,
    CartItemCreateSerializer,
)
from utils.permissions import IsOwner


class CartItemListAPIView(generics.ListAPIView):
    """Shows the cart of the certain User"""

    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(cart__customer=user)


class CartItemDeleteView(DestroyAPIView):
    """Deletes the CartItem from a certain User by the book id"""

    permission_classes = [permissions.IsAuthenticated, IsOwner]

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

    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = CartItemCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        cart_item = serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
