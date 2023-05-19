from tests.conftests import *


@pytest.mark.django_db
def test_user_create(user):
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_default_user(default_user):
    assert default_user.username == "defaultuser"


@pytest.mark.django_db
def test_authorized_user(authorized_user):
    assert authorized_user.username == "authorizeduser"

