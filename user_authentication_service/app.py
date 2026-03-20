@app.route("/sessions", methods=["POST"], strict_slashes=False)
def login() -> str:
    """
    POST /sessions
    - Expects form data: "email", "password"
    - Returns 401 if invalid
    - Sets "session_id" cookie and returns JSON if valid
    """
    email = request.form.get("email")
    password = request.form.get("password")

    # Use the AUTH instance created at the module level
    if not AUTH.valid_login(email, password):
        abort(401)

    # Create session and capture the ID
    session_id = AUTH.create_session(email)
    
    # Prepare the JSON response
    payload = {"email": email, "message": "logged in"}
    response = make_response(jsonify(payload))
    
    # Set the cookie with the exact key "session_id"
    response.set_cookie("session_id", session_id)
    
    return response
