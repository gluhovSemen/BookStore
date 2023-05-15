from django.urls import path
from purchase.views import CreatePurchaseAndClearCart, UserPurchaseListAPIView

urlpatterns = [
    path("purchases/", CreatePurchaseAndClearCart.as_view(), name="purchase-create"),
    path("purchases/list/", UserPurchaseListAPIView.as_view(), name="purchase-list"),
]
