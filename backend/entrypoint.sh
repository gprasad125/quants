#!/bin/bash
python manage.py migrate
gunicorn --bind :8000 --workers 2 backend.wsgi
