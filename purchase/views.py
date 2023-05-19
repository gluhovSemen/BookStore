from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import transaction

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
        purchases = create_purchases_and_clear_cart(user)
        return Response(PurchaseSerializer(purchases, many=True).data, status=200)


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
