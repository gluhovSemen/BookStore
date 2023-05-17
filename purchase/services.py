from django.db.models import F

from rest_framework.exceptions import ValidationError

from cart.models import Cart
from purchase.models import Purchase


def create_purchases_and_clear_cart(user):
    cart = (
        Cart.objects.select_related("customer")
        .prefetch_related("cartitem_set")
        .get(customer=user)
    )
    purchases = []
    for cart_item in cart.cartitem_set.all():
        book = cart_item.book
        if cart_item.quantity > book.available_stock:
            raise ValidationError(
                {"message": f"Not enough stock available for book: {book.title}"}
            )
        book.available_stock = F("available_stock") - cart_item.quantity
        book.save()

        purchase = Purchase(
            customer=user,
            book=book,
            quantity=cart_item.quantity,
            price=cart_item.price,
        )
        purchases.append(purchase)
    Purchase.objects.bulk_create(purchases)

    cart.delete_cart_items()

    return purchases
