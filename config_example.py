import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_BASE_DIR = os.path.dirname(BASE_DIR)

settings_profile = 'scpc.settings.base'
secret_key = 'HERE YOUR SECRET KEY'

# database_default = {
#     'ENGINE': 'django.db.backends.mysql',
#     'NAME': 'database',
#     'USER': 'user',
#     'PASSWORD': 'password',
#     'HOST': 'localhost'
# }

database_default = {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}


media_root = os.path.join(PARENT_BASE_DIR, 'files')
