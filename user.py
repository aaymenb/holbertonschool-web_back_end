#!/usr/bin/env python3
"""
Module pour le modèle User
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# 1. Création de la base déclarative comme expliqué dans votre texte
Base = declarative_base()

# 2. Définition de la classe User mappée à la table 'users'
class User(Base):
    """
    Modèle SQLAlchemy pour la table 'users'
    """
    __tablename__ = 'users'

    # Attributs demandés par l'exercice (et non par le tutoriel générique)
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
