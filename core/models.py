from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    """This model represents an author of a book"""
    name = models.CharField(max_length=255)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(null=True)
    date_of_death = models.DateField(null=True, blank=True)


class Publisher(models.Model):
    """This model represents a publisher of a book"""
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)


class Book(models.Model):
    """This model represents a book in the online store"""
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/')
    language = models.CharField(max_length=255)
    available_stock = models.IntegerField()
    rating = models.FloatField(default=0.0)


class Cart(models.Model):
    """This model represents the shopping cart of a user"""
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class CartItem(models.Model):
    """This model represents an item in the shopping cart"""
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)


class Review(models.Model):
    """This model represents a customer's review of a book"""
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    rating = models.IntegerField()
    review_text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.title
