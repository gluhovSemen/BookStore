from django.urls import path
from purchase.views import PurchaseList
urlpatterns = [
    path('purchases/', PurchaseList.as_view(), name='purchase-list'),
    path('purchases/<int:cart_pk>/', PurchaseList.as_view(), name='purchase-list'),
]
