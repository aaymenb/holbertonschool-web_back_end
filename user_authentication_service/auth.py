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
    Hashes a password string using bcrypt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def _generate_uuid() -> str:
    """
    Generates a random UUID string.
    """
    return str(uuid.uuid4())


class Auth:
    """
    Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Initialize the Auth instance with a private DB instance.
        """
        self._db = DB()

    # ... (Keep your existing register_user, valid_login, create_session)

    def get_user_from_session_id(self, session_id: str) -> Optional[object]:
        """
        Finds a user by session ID.

        Args:
            session_id (str): The session ID to search for.

        Returns:
            The User object if found, otherwise None.
        """
        if session_id is None:
            return None

        try:
            # Using the public find_user_by method with session_id keyword
            user = self._db.find_user_by(session_id=session_id)
            return user
        except NoResultFound:
            return None
