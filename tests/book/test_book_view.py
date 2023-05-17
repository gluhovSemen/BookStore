from rest_framework.test import APIClient
import pytest
from .conftests import authors

client = APIClient()


@pytest.mark.django_db
def test_get_auther(authors):
    response = client.get("/books/books/")
    assert response.status_code == 200
