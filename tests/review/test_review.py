import pytest
from rest_framework import status
from django.urls import reverse

from review.models import Review
from tests.conftests import *


@pytest.mark.django_db
def test_review_list(review, api_client):
    url = reverse("review-list", kwargs={"book_pk": review.book.pk})
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_review_create_permission(api_client, book, user):
    url = reverse("review-list", kwargs={"book_pk": book.pk})
    payload = {"book": book.pk, "rating": 1, "review_text": "string"}
    response = api_client.post(url, payload, format="json")
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_review_create_book_rating(api_client, book, user):
    api_client.force_authenticate(user=user)
    url = reverse("review-list", kwargs={"book_pk": book.pk})
    payload = {"book": book.pk, "rating": 3, "review_text": "string"}
    response = api_client.post(url, payload, format="json")
    review = Review.objects.first()
    assert review.rating == 3


@pytest.mark.django_db
def test_review_create(api_client, book, user):
    api_client.force_authenticate(user=user)
    url = reverse("review-list", kwargs={"book_pk": book.pk})
    payload = {"book": book.pk, "rating": 1, "review_text": "string"}
    response = api_client.post(url, payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    review = Review.objects.first()
    assert review.customer == user
    assert review.book == book


@pytest.mark.django_db
def test_review_delete(api_client, review, user):
    api_client.force_authenticate(user=user)
    url = reverse(
        "review-destroy", kwargs={"book_pk": review.book.pk, "review_pk": review.pk}
    )
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_review_delete_permission(api_client, review, user):
    url = reverse(
        "review-destroy", kwargs={"book_pk": review.book.pk, "review_pk": review.pk}
    )
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
