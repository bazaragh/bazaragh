# Bazar AGH

[![CI](https://github.com/sokoloowski/pzio/actions/workflows/CI.yml/badge.svg)](https://github.com/sokoloowski/pzio/actions/workflows/CI.yml)
[![codecov](https://codecov.io/gh/sokoloowski/pzio/branch/master/graph/badge.svg?token=D21TUCS1RT)](https://codecov.io/gh/sokoloowski/pzio)

## Prerequisites

- Python 3.11

## Getting started

### Create virtual environment

```bash
python3 -m venv ./venv
source venv/bin/activate
```

### Install requirements

```bash
sudo apt install libmariadbclient-dev # not required on Windows
pip install -r requirements.txt
```

### Create local configuration

```bash
cp app/config.py config.local.py
```

Edit values in `config.local.py` to match Your environment.  

### Start application

```bash
flask run
# or
FLASK_ENV=development FLASK_DEBUG=1 flask run
```

Your application is running on `http://127.0.0.1:5000`

## Deployment

Use `gunicorn`:

```bash
gunicorn wsgi -b 127.0.0.1:8080 --daemon
```
