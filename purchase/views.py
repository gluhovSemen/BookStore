from rest_framework import generics, permissions

from purchase.services import create_purchase_empty_cart
from purchase.models import Purchase
from purchase.serializers import PurchaseSerializer


class PurchaseList(generics.ListCreateAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        create_purchase_empty_cart()
        serializer.save(customer=self.request.user)


class PurchaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Purchase.objects.filter(customer=self.request.user)
