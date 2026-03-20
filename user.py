#!/usr/bin/env python3
"""
User model for SQLAlchemy mapping.
Represents the 'users' table in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):

    """
    SQLAlchemy User model for 'users' table.
    Stores user authentication and session details.
    """

    __tablename__ = 'users'

    id: int = Column(Integer, primary_key=True)
    email: str = Column(String(250), nullable=False)
    hashed_password: str = Column(String(250), nullable=False)
    session_id: str = Column(String(250), nullable=True)
    reset_token: str = Column(String(250), nullable=True)
