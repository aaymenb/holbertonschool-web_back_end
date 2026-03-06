#!/usr/bin/env python3
"""
Users views
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """GET /api/v1/users
    Return all users
    """
    try:
        data = User.load_from_file()
        users = [User(**item) for item in data]
        return jsonify([user.to_dict() for user in users])
    except Exception:
        return jsonify([])


@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """POST /api/v1/users
    Create a new user
    """
    try:
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Not a JSON"}), 400
        if 'email' not in data:
            return jsonify({"error": "Missing email"}), 400
        if 'password' not in data:
            return jsonify({"error": "Missing password"}), 400
        users = User.search(**{'email': data['email']})
        if users:
            return jsonify({"error": "Already exist for this email"}), 400
        user = User(**data)
        user.save()
        return jsonify(user.to_dict()), 201
    except Exception:
        return jsonify({"error": "Not a JSON"}), 400


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """GET /api/v1/users/<user_id>
    Return a user by id, or current user if user_id is 'me'
    """
    if user_id == 'me':
        if request.current_user is None:
            abort(404)
        return jsonify(request.current_user.to_dict())
    try:
        users = User.search(**{'id': user_id})
        if not users:
            abort(404)
        return jsonify(users[0].to_dict())
    except Exception:
        abort(404)


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """PUT /api/v1/users/<user_id>
    Update a user by id
    """
    try:
        users = User.search(**{'id': user_id})
        if not users:
            abort(404)
        user = users[0]
        data = request.get_json()
        if data is None:
            return jsonify({"error": "Not a JSON"}), 400
        for key in ['password', 'email', 'first_name', 'last_name']:
            if key in data:
                setattr(user, key, data[key])
        user.save()
        return jsonify(user.to_dict())
    except Exception:
        abort(404)


@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """DELETE /api/v1/users/<user_id>
    Delete a user by id
    """
    try:
        users = User.search(**{'id': user_id})
        if not users:
            abort(404)
        user = users[0]
        import json
        import os
        filename = "User.json"
        data = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    data = []
        data = [item for item in data if item.get('id') != user_id]
        with open(filename, 'w') as f:
            json.dump(data, f)
        return jsonify({}), 200
    except Exception:
        abort(404)
