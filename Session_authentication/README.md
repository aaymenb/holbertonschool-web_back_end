# Session Authentication - Et moi et moi et moi!

This project extends Basic Authentication with a new endpoint: **GET /api/v1/users/me** to retrieve the authenticated user.

## Setup

```bash
pip3 install -r requirements.txt
```

## Run

```bash
API_HOST=0.0.0.0 API_PORT=5000 AUTH_TYPE=basic_auth python3 -m api.v1.app
```

## Endpoints

- `GET /api/v1/status` - API status
- `GET /api/v1/users` - List all users (requires auth)
- `POST /api/v1/users` - Create user (requires auth)
- `GET /api/v1/users/<user_id>` - Get user by ID (requires auth)
- `GET /api/v1/users/me` - Get authenticated user (requires auth)
- `PUT /api/v1/users/<user_id>` - Update user (requires auth)
- `DELETE /api/v1/users/<user_id>` - Delete user (requires auth)

## Usage

Use the `Authorization` header with `Basic <base64_encoded_credentials>` format.
