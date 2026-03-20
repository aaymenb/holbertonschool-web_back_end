# Basic Authentication

This project implements Basic Authentication for a Flask API.

## Setup

```bash
pip3 install -r requirements.txt
```

## Run

```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

## Usage

The API supports Basic Authentication. Use the `Authorization` header with `Basic <base64_encoded_credentials>` format.
