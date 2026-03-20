#!/usr/bin/env python3
"""
Auth module
"""
import bcrypt
import uuid
from typing import Optional  # Pour un type hinting plus précis
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string using bcrypt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generate a random UUID
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database
    """

    def __init__(self):
        """
        Initialize Auth with a private DB instance
        """
        self._db = DB()

    # ... (garder register_user et valid_login)

    def create_session(self, email: str) -> Optional[str]:
        """
        Creates a new session ID for a user if they exist.

        Args:
            email (str): The user email.

        Returns:
            Optional[str]: The session ID if user found, else None.
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            self._db.update_user(user.id, session_id=session_id)
            return session_id
        except NoResultFound:
            return None
