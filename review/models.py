from django.db import models
from django.contrib.auth.models import User
from book.models import Book


class Review(models.Model):
    """This model represents a customer's review of a book"""
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
