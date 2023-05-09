from rest_framework import generics
from book.models import Book, Author, Publisher
from book.serializers import BookSerializer, AuthorSerializer, PublisherSerializer


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetail(generics.ListAPIView):
    serializer_class = BookSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")
        return Book.objects.filter(pk=pk)


class AuthorList(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class PublisherList(generics.ListAPIView):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer
