from rest_framework import serializers
from book.models import Book, Author, Publisher


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"


class BookShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = "__all__"
