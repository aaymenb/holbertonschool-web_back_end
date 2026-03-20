#!/usr/bin/env python3
"""
Auth module for user session management
"""
import bcrypt
import uuid
from typing import Optional
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hashes a password string using bcrypt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generate a random UUID string
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

    # ... (garder register_user et valid_login intacts)

    def create_session(self, email: str) -> Optional[str]:
        """
        Creates a new session ID for a user.

        Args:
            email (str): The user email to look for.

        Returns:
            Optional[str]: The generated session ID, or None if no user.
        """
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return None

        session_id = _generate_uuid()
        self._db.update_user(user.id, session_id=session_id)
        return session_id
