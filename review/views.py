from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404

from review.models import Review
from review.serializers import ReviewSerializer, ReviewSerializerLong
from book.models import Book
from utils.permissions import IsOwnerOrReadOnly


class ReviewList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_pk = self.kwargs["book_pk"]
        book = get_object_or_404(Book, pk=book_pk)
        queryset = Review.objects.filter(book=book)
        return queryset

    def perform_create(self, serializer):
        book_pk = self.kwargs["book_pk"]
        book = get_object_or_404(Book, pk=book_pk)
        user = self.request.user
        serializer.save(customer=user, book=book)


class ReviewDestroy(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializerLong

    def get_object(self):
        book_pk = self.kwargs["book_pk"]
        review_pk = self.kwargs["review_pk"]
        return get_object_or_404(Review, pk=review_pk, book__pk=book_pk)
