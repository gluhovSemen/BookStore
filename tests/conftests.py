import uuid

from django.contrib.auth.models import User

from tests.factories import AuthorFactory, BookFactory, PublisherFactory, UserFactory, ReviewFactory
import pytest
from rest_framework.test import APIClient


# fixtures
@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def author():
    return AuthorFactory.create()


@pytest.fixture
def publisher():
    return PublisherFactory.create()

@pytest.fixture
def book():
    return BookFactory.create()

@pytest.fixture
def user():
    return UserFactory.create()


@pytest.fixture
def default_user(user):
    user = User.objects.create_user(username="defaultuser", password="password")
    return user


@pytest.fixture
def authorized_user(api_client, default_user):
    user = User.objects.create_user(username="authorizeduser", password="password")
    api_client.login(username="authorizeduser", password="password")
    user.api_client = api_client
    return user

@pytest.fixture
def review():
    return ReviewFactory.create()