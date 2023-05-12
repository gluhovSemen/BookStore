from django.urls import path
from cart.views import CartItemCreateView, CartItemListAPIView, CartItemDeleteView

urlpatterns = [
    path("carts/", CartItemListAPIView.as_view(), name="cart_detail"),
    path(
        "carts/<int:book_id>/delete/",
        CartItemDeleteView().as_view(),
        name="cart_item_delete",
    ),
    path("carts/items/create/", CartItemCreateView.as_view(), name="cart_item_detail"),
]
