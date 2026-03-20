#!/usr/bin/env python3
"""
Authentication module containing password hashing and UUID generation
"""
import bcrypt
import uuid
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generate a random UUID.

    Returns:
        str: a string representation of a new UUID.
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """
    # ... Tes méthodes précédentes (register_user, valid_login, etc.)
