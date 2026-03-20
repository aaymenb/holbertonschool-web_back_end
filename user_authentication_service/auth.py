#!/usr/bin/env python3
"""
Auth module for user registration
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string using bcrypt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """
    Auth class to interact with the authentication database
    """

    def __init__(self):
        """
        Initialize Auth with a private DB instance
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a user or raises ValueError if they exist
        """
        try:
            self._db.find_user_by(email=email)
            # If the line above doesn't raise an error, the user exists
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            # User doesn't exist, so hash and add
            hashed_pw = _hash_password(password)
            # Decode bytes to string for storage
            return self._db.add_user(email, hashed_pw.decode('utf-8'))
