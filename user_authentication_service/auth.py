#!/usr/bin/env python3
"""
Auth module for user registration and authentication
"""
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Initialize the Auth instance with a private DB instance.
        """
        self._db = DB()

    def register_user(self, email: str, password: str):
        """
        Registers a new user if they don't already exist.

        Args:
            email (str): The user's email.
            password (str): The user's plain-text password.

        Returns:
            User: The created User object.

        Raises:
            ValueError: If the user already exists.
        """
        try:
            # Check if user exists using the DB method from Task 2
            self._db.find_user_by(email=email)
            # If no exception is raised, the user exists
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            # User does not exist, proceed with registration
            hashed_pw = _hash_password(password)
            # Use the DB method from Task 1 to save
            new_user = self._db.add_user(email, hashed_pw.decode('utf-8'))
            return new_user
