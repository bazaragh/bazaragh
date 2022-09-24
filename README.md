# Flask-based REST API

## Prerequisites

- Python 3.10

## Getting started

### Create virtual environment

```bash
python3.10 -m venv ./venv
source venv/bin/activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Start application

```bash
flask run
# or
FLASK_ENV=development FLASK_DEBUG=1 flask run
```

Your application is running on `http://127.0.0.1:5000`

## About

This example contains three endpoints:

- `/` - simple "Hello world"
- `/hello/<name>` - endpoint with GET variable
- `/hello` - POST endpoint

While you can test GET endpoints in browser, to test POST endpoint, use `curl`:

```bash
curl -X POST http://127.0.0.1:5000/hello -d "your-name-here"
```
