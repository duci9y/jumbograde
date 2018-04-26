import os
from celery import Celery

# celery wants the settings module as an env var
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jumbograde.settings')

# TODO: Constance? 
app = Celery('jumbograde', broker='redis://localhost')

# tell celery to use 'CELERY_' prefixed variables in the settings module for
# configuration
app.config_from_object('django.conf:settings', namespace='CELERY')

# scans tasks.py files in all installed apps and registers tasks found in them
app.autodiscover_tasks()
