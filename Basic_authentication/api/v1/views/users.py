#!/usr/bin/env python3
"""
Users views
"""
from flask import jsonify, request
from api.v1.views import app_views


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """GET /api/v1/users
    Return all users
    """
    try:
        from models.user import User
        data = User.load_from_file()
        users = [User(**item) for item in data]
        return jsonify([user.to_dict() for user in users])
    except Exception:
        return jsonify([])
