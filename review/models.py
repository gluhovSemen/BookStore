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

    def update_book_rating(self):
        book = self.book
        reviews = Review.objects.filter(book=book)
        rating_sum = sum(review.rating for review in reviews)
        average_rating = rating_sum / reviews.count() if reviews.count() > 0 else 0.0
        book.rating = average_rating
        book.save()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_book_rating()

    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        self.update_book_rating()

    def update(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_book_rating()
