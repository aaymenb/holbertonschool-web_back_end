#!/usr/bin/env python3
"""
Authentication module containing password hashing logic
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string using bcrypt.

    Args:
        password (str): The password string to hash.

    Returns:
        bytes: The salted and hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
