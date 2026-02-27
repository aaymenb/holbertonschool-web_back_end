#!/usr/bin/env python3
"""
User model
"""
from models.base import Base


class User(Base):
    """User model class"""

    def __init__(self, *args, **kwargs):
        """Initialize a new User instance"""
        super().__init__(*args, **kwargs)
        if not hasattr(self, 'email'):
            self.email = ""
        if not hasattr(self, 'password'):
            self.password = ""
        if not hasattr(self, 'first_name'):
            self.first_name = None
        if not hasattr(self, 'last_name'):
            self.last_name = None

    def display_name(self) -> str:
        """Return display name"""
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.email

    def is_valid_password(self, pwd: str) -> bool:
        """Check if password is valid"""
        if not pwd or not self.password:
            return False
        return pwd == self.password
