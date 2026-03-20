#!/usr/bin/env python3
"""
Authentication module for the user service
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
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_pw = _hash_password(password)
            # On stocke le hash sous forme de string décodée
            return self._db.add_user(email, hashed_pw.decode('utf-8'))

    def valid_login(self, email: str, password: str) -> bool:
        """
        Checks if the provided credentials are valid.

        Args:
            email (str): The user email.
            password (str): The plain-text password.

        Returns:
            bool: True if valid, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
        except (NoResultFound, Exception):
            return False

        # bcrypt.checkpw compare des bytes (password) avec des bytes (hash)
        if bcrypt.checkpw(password.encode('utf-8'),
                         user.hashed_password.encode('utf-8')):
            return True

        return False
