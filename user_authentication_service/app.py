#!/usr/bin/env python3
"""
Flask app module
"""
from flask import Flask, jsonify, request, abort, make_response
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


# ... (previous routes: / and /users)


@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """
    POST /sessions
    Validates user credentials, creates a session, and sets a cookie.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    # 1. Check if the login is valid
    if not AUTH.valid_login(email, password):
        abort(401)

    # 2. Create the session ID
    session_id = AUTH.create_session(email)

    # 3. Create the response with the JSON payload
    response = make_response(jsonify({"email": email, "message": "logged in"}))

    # 4. Set the cookie on the response object
    response.set_cookie("session_id", session_id)

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
