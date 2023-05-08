from django.urls import path
from cart.views import CartItemDetail, CartDetail, CartItemList

urlpatterns = [
    path('carts/<int:pk>/', CartDetail.as_view(), name='cart_detail'),
    path('carts/<int:cart_id>/items/', CartItemList.as_view(), name='cart_item_list'),
    path('carts/<int:cart_id>/items/<int:pk>/', CartItemDetail.as_view(), name='cart_item_detail'),
]