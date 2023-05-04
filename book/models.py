from django.db import models


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
