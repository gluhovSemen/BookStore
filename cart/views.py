from rest_framework import generics, status, permissions
from rest_framework.response import Response
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.cart.user == request.user


class CartList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser, IsOwner]
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get_object(self):
        return self.queryset.get(pk=self.request.user.pk)


class CartItemList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser, IsOwner]
    serializer_class = CartItemSerializer

    def get_queryset(self):
        cart_id = self.kwargs['cart_id']
        return CartItem.objects.filter(cart_id=cart_id)

    def create(self, request, cart_id):
        request.data['cart'] = cart_id
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser, IsOwner]
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
