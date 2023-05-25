import pytest
from rest_framework import status
from rest_framework.reverse import reverse

from tests.conftests import *
from purchase.models import Purchase


@pytest.mark.django_db
def test_purchase_list(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("purchase-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def test_purchase_list_permission(api_client, user):
    url = reverse("purchase-list")
    response = api_client.get(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_purchase_ditail(api_client, user):
    api_client.force_authenticate(user=user)
    url = "purchases/purchases/list/1/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_purchase_ditail_permission(api_client, user):
    api_client.force_authenticate(user=user)
    url = "purchases/purchases/list/1/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.enable_signals
@pytest.mark.django_db
def test_purchase_create_permission(api_client, user):
    url = reverse("purchase-create")
    response = api_client.post(url)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.enable_signals
@pytest.mark.django_db
def test_purchase_create_on_empty_cart(api_client, user):
    api_client.force_authenticate(user=user)
    url = reverse("purchase-create")
    response = api_client.post(url)
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.enable_signals
@pytest.mark.django_db
def test_purchase_create_on_cart_item(api_client, user, book):
    api_client.force_authenticate(user=user)
    stock = book.available_stock
    # book.available_stock = stock - 3
    url = reverse("cart_item_detail")
    payload = {"book_id": book.pk, "quantity": 3}
    api_client.post(url, payload, format="json")
    breakpoint()
    url = reverse("purchase-create")
    response = api_client.post(url)
    breakpoint()
    assert response.status_code == status.HTTP_200_OK
    purchase = Purchase.objects.first()
    assert purchase.customer == user
    assert purchase.quantity == 3
    assert book.available_stock == int(stock - 3)


@pytest.mark.enable_signals
@pytest.mark.django_db
def test_purchase_ditail_2(api_client, user, book):
    api_client.force_authenticate(user=user)
    url = reverse("cart_item_detail")
    payload = {"book_id": book.pk, "quantity": 3}
    api_client.post(url, payload, format="json")
    url = reverse("purchase-create")
    api_client.post(url)
    purchase = Purchase.objects.first()
    url = f"purchases/purchases/list/{purchase.id}/"
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
