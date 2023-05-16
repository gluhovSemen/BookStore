from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from book.models import Book


class Cart(models.Model):
    """This model represents the shopping cart of a user"""

    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def delete_cart_items(self, *args, **kwargs):
        self.cartitem_set.all().delete()


class CartItem(models.Model):
    """This model represents an item in the shopping cart"""

    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)


@receiver(post_save, sender=User)
def create_order_history(sender, instance, created, **kwargs):
    if created:
        Cart.objects.create(customer=instance)
