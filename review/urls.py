from django.urls import path
from review.views import ReviewList, ReviewDestroy

urlpatterns = [
    path("books/<int:book_pk>/reviews/", ReviewList.as_view(), name="review-list"),
    path(
        "books/<int:book_pk>/reviews/<review_pk>/",
        ReviewDestroy.as_view(),
        name="review-destroy",
    ),
]
