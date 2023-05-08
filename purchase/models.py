from django.db import models
from user.models import Profile

from book.models import Book


class Purchase(models.Model):
    """This model represents purchases, also will be used in FastAPI microservice"""
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    purchased_date = models.DateTimeField(auto_now_add=True)
