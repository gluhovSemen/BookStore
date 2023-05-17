from rest_framework import generics
from django.shortcuts import get_object_or_404
from review.models import Review
from review.serializers import ReviewSerializer
from book.models import Book
from utils.permissions import IsOwnerOrReadOnly


class ReviewList(generics.ListCreateAPIView):
    permission_classes = [IsOwnerOrReadOnly]
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
