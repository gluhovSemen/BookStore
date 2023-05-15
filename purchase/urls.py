from django.urls import path
from purchase.views import (
    CreatePurchase,
    UserPurchaseListAPIView,
    UserPurchaseDitailAPIView,
)

urlpatterns = [
    path("purchases/", CreatePurchase.as_view(), name="purchase-create"),
    path(
        "purchases/list/<int:pk>/",
        UserPurchaseDitailAPIView.as_view(),
        name="purchase-Ditail",
    ),
    path("purchases/list/", UserPurchaseListAPIView.as_view(), name="purchase-list"),
]
