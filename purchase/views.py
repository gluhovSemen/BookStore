from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction

from cart.models import Cart
from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer, PurchaseSerializerShort
from utils.permissions import IsOwner


class CreatePurchaseAndClearCart(APIView):
    permission_classes = [IsOwner]

    @transaction.atomic
    def post(self, request):
        user = request.user
        try:
            cart = (
                Cart.objects.select_related("customer")
                .prefetch_related("cartitem_set")
                .get(customer=user)
            )
        except Cart.DoesNotExist:
            return Response({"message": "Cart does not exist"}, status=404)

        # Create purchases for each cart item
        purchases = []
        for cart_item in cart.cartitem_set.all():
            book = cart_item.book
            if cart_item.quantity > book.available_stock:
                raise ValidationError(
                    {"message": f"Not enough stock available for book: {book.title}"}
                )
            purchase = Purchase(
                customer=cart.customer,
                book=book,
                quantity=cart_item.quantity,
                price=cart_item.price,
            )
            purchases.append(purchase)
        Purchase.objects.bulk_create(purchases)

        cart.cartitem_set.all().delete()

        return Response({"message": "Purchases created and cart cleared"}, status=200)


class UserPurchaseListAPIView(ListAPIView):
    serializer_class = PurchaseSerializerShort
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(customer=user)


class UserPurchaseDitailAPIView(RetrieveAPIView):
    serializer_class = PurchaseSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = self.request.user
        return Purchase.objects.filter(customer=user)
