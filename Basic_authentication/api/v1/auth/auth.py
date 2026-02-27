#!/usr/bin/env python3
"""
Auth class for API authentication
"""
from flask import request
from typing import List, TypeVar

User = TypeVar('User')


class Auth:
    """Template for all authentication systems"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Returns True if path is not in excluded_paths, False otherwise.
        Slash tolerant: /api/v1/status and /api/v1/status/ match /api/v1/status/
        """
        if path is None:
            return True
        if excluded_paths is None or len(excluded_paths) == 0:
            return True
        path_normalized = path if path.endswith('/') else path + '/'
        if path_normalized in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """Returns None - request will be the Flask request object"""
        return None

    def current_user(self, request=None) -> User:
        """Returns None - request will be the Flask request object"""
        return None
