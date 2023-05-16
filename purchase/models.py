from django.db import models
from django.contrib.auth.models import User

from book.models import Book


class Purchase(models.Model):
    """This model represents purchases, also will be used in FastAPI microservice"""

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    purchased_date = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)
    #     # Remove the purchased items from the cart
    #     cart = get_object_or_404(Cart, customer=self.customer)
    #     cart_items = CartItem.objects.filter(cart=cart, book=self.book)
    #     cart_items.delete()
    #     # Reduce the available stock of the book
    #     self.book.available_stock -= self.quantity
    #     self.book.save()
