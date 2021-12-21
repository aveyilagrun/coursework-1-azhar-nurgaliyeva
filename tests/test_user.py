import pytest
import bcrypt


def test_full_name(first_name, last_name):
    full_name = first_name + last_name
    assert len(full_name) == len(first_name) + len(last_name)


def test_password(password):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf8'), salt)
    if hashed_password == password:
        return False
    else:
        return True
