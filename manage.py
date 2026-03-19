#!/usr/bin/env python3
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Insight.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

"""
user: student
pass: F@cky@u

to run: 
    http://127.0.0.1:8000/api/documents/


signals
    app.py -to work automatically
for download to go to a folder:
    add Media to settings
    add upload_to='pdfs/%Y/%m/%d/' for models(pdf)
install redis and celery, redis server,
add the CELERY line to settings
root folder- celery.py -add to __init__ the import stuff
task.py heavy lifter

REDIS(transporter)
    # Start the service now
sudo systemctl start redis-server

    # Enable it to start on boot
sudo systemctl enable redis-server  
redis-cli ping
turning off; sudo systemctl stop redis-server

Turn celery:(the worker)
    celery -A Insight worker --loglevel=info

pip install PyPDF2 textblob

pip install --upgrade certifi


for the front-end:
    drf-spectacular? 
    pip install drf-spectacular

    INSTALLED_APPS = [
        # ...
        'drf_spectacular',
    ]

    REST_FRAMEWORK = {
        'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    }

    metadata for your project’s "Instruction Manual."
    SPECTACULAR_SETTINGS = {
        'TITLE': 'Insight AI Document API',
        'DESCRIPTION': 'An API that summarizes PDFs using Celery and AI.',
        'VERSION': '1.0.0',
        'SERVE_INCLUDE_SCHEMA': False,
    }

"""

