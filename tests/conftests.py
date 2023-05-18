from tests.factories import AuthorFactory, BookFactory, PublisherFactory
import pytest
from rest_framework.test import APIClient

# fixtures
@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def author():
    return AuthorFactory


@pytest.fixture
def publisher():
    return PublisherFactory

@pytest.fixture
def book():
    return BookFactory()
