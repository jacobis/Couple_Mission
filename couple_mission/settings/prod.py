"""Production settings and globals."""


from os import environ

from common import *

# DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'uai_db',
        'USER': 'uai_admin',
        'PASSWORD': '',
        'HOST': '10.0.1.4',
        'PORT': '6432',
    }
}
# END DATABASE CONFIGURATION


# PROD CONFIGURATION
CLOUD_FILESYSTEM = True
# END PROD CONFIGURATION


# EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host
EMAIL_HOST = environ.get('EMAIL_HOST', 'smtp.gmail.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-password
EMAIL_HOST_PASSWORD = environ.get('EMAIL_HOST_PASSWORD', '')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-host-user
EMAIL_HOST_USER = environ.get('EMAIL_HOST_USER', 'your_email@example.com')

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-port
EMAIL_PORT = environ.get('EMAIL_PORT', 587)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-subject-prefix
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#server-email
SERVER_EMAIL = EMAIL_HOST_USER
# END EMAIL CONFIGURATION


# ALLOWED HOSTS CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['207.46.132.251']
# END ALLOWED HOST CONFIGURATION


# STORAGE CONFIGURATION
AZURE_CONTENTS_ACCOUNT_NAME = 'couplemission'
AZURE_CONTENTS_ACCOUNT_KEY = 'MdVyDc5ZLUwj/jchMZe+Jt1mAtYpWeQdRLZxYAc2VWFuW2lss9K+eJtVTY3xwUqj+TwdBZNtTwf7V3y2U0KZpQ=='
CONTENTS_BASE_URL = 'http://couplemission.blob.core.windows.net/'
# END STORAGE CONFIGURATION
