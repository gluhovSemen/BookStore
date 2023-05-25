from collections import defaultdict

from django.db.models import F

from rest_framework.exceptions import ValidationError

from book.models import Book
from cart.models import Cart
from purchase.models import Purchase


def create_purchases_and_clear_cart(user):
    cart = (
        Cart.objects.select_related("customer")
        .prefetch_related("cartitem_set")
        .get(customer=user)
    )
    updates = []
    stock_updates = defaultdict(int)
    purchases = []
    breakpoint()
    for cart_item in cart.cartitem_set.all():
        book = cart_item.book
        if cart_item.quantity > book.available_stock:
            raise ValidationError(
                {"message": f"Not enough stock available for book: {book.title}"}
            )
        stock_updates[book.pk] += cart_item.quantity

        purchase = Purchase(
            customer=user,
            book=book,
            quantity=cart_item.quantity,
            price=cart_item.price,
        )
        purchases.append(purchase)
    Purchase.objects.bulk_create(purchases)
    books = Book.objects.filter(pk__in=stock_updates.keys())
    for book in books:
        book.available_stock = F("available_stock") - stock_updates[book.pk]
        updates.append(book)

    Book.objects.bulk_update(updates, fields=["available_stock"])

    cart.delete_cart_items()

    return purchases
