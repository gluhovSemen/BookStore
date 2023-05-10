from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from cart.models import Cart, CartItem
from cart.serializers import CartSerializer, CartItemSerializer


class CartList(generics.ListCreateAPIView):
    """Shows all the carts, for admins only"""
    permission_classes = [permissions.IsAdminUser]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    """Shows the cart of the certain User"""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        obj = super().get_object()
        if obj.customer != self.request.user:
            self.permission_denied(
                self.request, message="You do not have permission to access this cart."
            )
        return obj


class CartItemList(generics.ListCreateAPIView):
    """Shows all the CartItems in a cart for a certain user"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart = get_object_or_404(Cart, customer=self.request.user)
        queryset = CartItem.objects.filter(cart=cart)
        return queryset

    def perform_create(self, serializer):
        cart = get_object_or_404(Cart, customer=self.request.user)
        serializer.save(cart=cart)


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """Shows a specific cartitem of a certain user"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def get_object(self):
        obj = super().get_object()
        if obj.cart.customer != self.request.user:
            self.permission_denied(
                self.request, message="You do not have permission to access this cart item."
            )
        return obj
