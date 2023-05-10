from rest_framework import generics, permissions
from django.shortcuts import get_object_or_404
from review.models import Review
from review.serializers import ReviewSerializer
from book.models import Book


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the review
        return obj.customer == request.user


class ReviewList(generics.ListCreateAPIView):
    permission_classes = permissions.IsAuthenticatedOrReadOnly
    serializer_class = ReviewSerializer

    def get_queryset(self):
        book_pk = self.kwargs['book_pk']
        book = get_object_or_404(Book, pk=book_pk)
        queryset = Review.objects.filter(book=book)
        return queryset

    def perform_create(self, serializer):
        book_pk = self.kwargs['book_pk']
        book = get_object_or_404(Book, pk=book_pk)
        serializer.save(customer=self.request.user, book=book)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = IsOwnerOrReadOnly
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_object(self):
        book_pk = self.kwargs['book_pk']
        review_pk = self.kwargs['review_pk']  # use correct parameter name
        return get_object_or_404(Review, pk=review_pk, book__pk=book_pk)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
