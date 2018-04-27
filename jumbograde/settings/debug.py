import os
from .base import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x90p^6mxt(v3tj_4&cfbei9gn(5vm056-6s(#y97eycr8**nm$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

SUBMISSION_DIR = os.environ.get('SUBMISSION_DIR')
