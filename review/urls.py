from django.urls import path
from review.views import ReviewList,ReviewDetail

urlpatterns = [
    path('books/<int:book_pk>/reviews/', ReviewList.as_view(), name='review-list'),
    path('books/<int:book_pk>/reviews/<review_pk>/', ReviewDetail.as_view(), name='review-detail')
]
