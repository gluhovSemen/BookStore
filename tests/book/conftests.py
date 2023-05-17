from pytest_factoryboy import register
from .factories import AuthorFactory, BookFactory, PublisherFactory
import pytest

# Register Approach
factories = [AuthorFactory, PublisherFactory, BookFactory]
[register(_) for _ in factories]


# fixtures


@pytest.fixture
def authors():
    return AuthorFactory.create_batch(10)
