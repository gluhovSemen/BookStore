from django.db.models import Avg


def update_book_rating(book):
    reviews = book.review_set.all()
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    book.rating = average_rating if average_rating else 0.0
    book.save()