import pytest


@pytest.fixture(scope="module")
def first_name():
    first_name = "Alex"
    yield first_name


@pytest.fixture(scope="module")
def last_name():
    last_name = "Russo"
    yield last_name


@pytest.fixture(scope="module")
def email():
    email = "az.nur@gmail.com"
    yield email


@pytest.fixture(scope="module")
def password():
    password = "12345678"
    yield password
