from django.db import models
from django.contrib.auth.models import User

from book.models import Book
from purchase.celery import send_purchase_data_to_api


class Purchase(models.Model):
    """This model represents purchases, also will be used in FastAPI microservice"""

    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    purchased_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        payload = [
            {
                "book_id": self.book.id,
                "user_id": self.customer.id,
                "book_title": self.book.title,
                "author": self.book.author,
                "purchase_price": float(self.price),
                "purchase_quantity": self.quantity,
            }
        ]

        send_purchase_data_to_api.delay(payload)
