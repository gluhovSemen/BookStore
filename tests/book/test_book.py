import pytest
from rest_framework import status

from tests.conftests import *


@pytest.mark.django_db
def test_auther_list(author, api_client):
    response = api_client.get("/books/authors/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_publisher_list(publisher, api_client):
    response = api_client.get("/books/publishers/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_book_list(book, api_client):
    response = api_client.get("/books/books/")
    assert response.data["count"] == 1
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_book_detail(book, api_client):
    response = api_client.get(f"/books/books/{book.id}/")
    assert response.data['id'] == book.id
    assert response.status_code == status.HTTP_200_OK
