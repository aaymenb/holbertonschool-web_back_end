#!/usr/bin/env python3
"""
Authentication module containing password hashing and UUID generation
"""
import bcrypt
import uuid  # <--- Ajoute cet import
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generates a random UUID and returns its string representation.
    
    Returns:
        str: A string representation of a new UUID4.
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """
    # ... garde le reste de ta classe Auth ici ...
