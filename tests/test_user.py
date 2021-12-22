import pytest
from user import User


def test_full_name(first_name, last_name):
    full_name = User.create_full_name(User)
    assert len(full_name) == len(first_name) + len(last_name)


def test_password(password):
    hashed_password = User.hash_password(User, password)
    if hashed_password == password:
        return False
    else:
        return True
