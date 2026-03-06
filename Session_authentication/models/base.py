#!/usr/bin/env python3
"""
Base model class
"""
import json
import os
from typing import Dict, List, Optional
from uuid import uuid4


class Base:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new Base instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
        if not hasattr(self, 'id'):
            self.id = str(uuid4())

    def to_dict(self) -> Dict:
        """Convert instance to dictionary"""
        result = {}
        for key, value in self.__dict__.items():
            if not key.startswith('_'):
                if isinstance(value, str):
                    result[key] = value
                elif isinstance(value, (int, float, bool)):
                    result[key] = value
                elif value is None:
                    result[key] = None
                else:
                    result[key] = str(value)
        return result

    def save(self):
        """Save instance to file"""
        filename = f"{self.__class__.__name__}.json"
        data = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        
        # Remove existing instance if present
        data = [item for item in data if item.get('id') != self.id]
        
        # Add current instance
        data.append(self.to_dict())
        
        with open(filename, 'w') as f:
            json.dump(data, f)

    @classmethod
    def load_from_file(cls) -> List:
        """Load all instances from file"""
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []

    @classmethod
    def search(cls, **kwargs) -> List:
        """Search for instances matching kwargs"""
        results = []
        data = cls.load_from_file()
        for item in data:
            match = True
            for key, value in kwargs.items():
                if item.get(key) != value:
                    match = False
                    break
            if match:
                instance = cls(**item)
                results.append(instance)
        return results
