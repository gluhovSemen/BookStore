import pytest
from rest_framework import status
from django.urls import reverse

from review.models import Review
from tests.conftests import *


@pytest.mark.django_db
@pytest.mark.enable_signals
def test_cart_create_when_user_created(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("cart_detail")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
@pytest.mark.enable_signals
def test_cart_item_delete(api_client, user, book):
    api_client.force_authenticate(user=user)
    url = reverse("cart_item_detail")
    payload = {"book_id": book.pk, "quantity": 3}
    api_client.post(url, payload, format="json")
    url = reverse("cart_item_delete", kwargs={"book_id": book.pk})
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
@pytest.mark.enable_signals
def test_cart_item_create(api_client, user, book):
    api_client.force_authenticate(user=user)
    url = reverse("cart_item_detail")
    payload = {"book_id": book.pk, "quantity": 3}
    response = api_client.post(url, payload, format="json")
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
@pytest.mark.enable_signals
def test_cart_permission(api_client, user):
    url = reverse("cart_detail")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_cart_factory(cart):
    assert cart.id == cart.id


@pytest.mark.django_db
def test_cart_item_factory(cart_item):
    assert cart_item.book == cart_item.book