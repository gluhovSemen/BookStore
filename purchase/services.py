from django.shortcuts import get_object_or_404

from cart.models import CartItem, Cart


def create_purchase_empty_cart(self):
    cart = get_object_or_404(Cart, customer=self.customer)
    cart_items = CartItem.objects.filter(cart=cart, book=self.book)
    cart_items.delete()
    self.book.available_stock -= self.quantity
    self.book.save()
