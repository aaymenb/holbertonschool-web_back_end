#!/usr/bin/env python3
"""
Basic Auth class
"""
import base64
from typing import TypeVar
from api.v1.auth.auth import Auth

User = TypeVar('User')


class BasicAuth(Auth):
    """Basic authentication class - inherits from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """Returns the Base64 part of the Authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """Returns the decoded value of a Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            decoded = base64.b64decode(base64_authorization_header)
            return decoded.decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> (str, str):
        """Returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return (None, None)
        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        parts = decoded_base64_authorization_header.split(':', 1)
        user_email, user_password = parts[0], parts[1]
        return (user_email, user_password)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> User:
        """Returns the User instance based on email and password"""
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        import sys
        import os
        # Find models: try script dir (main_4.py) and its parent
        paths_to_add = []
        if '__main__' in sys.modules and hasattr(sys.modules['__main__'], '__file__'):
            main_file = sys.modules['__main__'].__file__
            script_dir = os.path.dirname(os.path.abspath(main_file))
            paths_to_add.extend([script_dir, os.path.dirname(script_dir)])
        file_dir = os.path.dirname(os.path.abspath(__file__))
        basic_auth = os.path.abspath(os.path.join(file_dir, '..', '..', '..'))
        paths_to_add.extend([basic_auth, os.path.dirname(basic_auth)])
        for path in paths_to_add:
            if path and path not in sys.path:
                sys.path.insert(0, path)
        from models.user import User as UserModel
        users = UserModel.search(email=user_email)
        if not users:
            return None
        user = users[0]
        if not user.is_valid_password(user_pwd):
            return None
        return user
