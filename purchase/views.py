from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from django.db import transaction

from cart.models import Cart
from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer, PurchaseSerializerShort
from purchase.services import create_purchases_and_clear_cart
from utils.permissions import IsOwner


class CreatePurchase(APIView):
    permission_classes = [IsOwner]
    serializer_class = PurchaseSerializer

    @transaction.atomic
    def post(self, request):
        user = request.user

        cart = (
            Cart.objects.select_related("customer")
            .prefetch_related("cartitem_set")
            .get(customer=user)
        )

        response = create_purchases_and_clear_cart(cart)

        return response


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
