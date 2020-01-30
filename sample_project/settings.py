import os

PROJECT_ENV = os.getenv('PROJECT_ENV', 'development')

FLASK_HOST = 'localhost'
FLASK_PORT = 5000

SOCKETS_HOST = '127.0.0.1'
SOCKETS_PORT = 65432

PSQL_USER = 'sample_project'
PSQL_PASS = 'protected_password'
PSQL_HOST = 'localhost'
PSQL_PORT = 5432
PSQL_DATABASE = 'sample_project_development'

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DATABASE = 'sample_project_development'

LOGGERS = {
    '': {
        'level': 'INFO',
        'handlers': ['console']
    }
}

"""
You can set local settings by creating a local_settings.py file
in the project root path and assigning all your values there
"""

try:
    from local_settings import *
except ImportError:
    pass


if PROJECT_ENV == 'test':
    PSQL_DATABASE = 'sample_project_test'


PSQL_URI = f'postgresql://{PSQL_USER}:{PSQL_PASS}@{PSQL_HOST}:{PSQL_PORT}/{PSQL_DATABASE}'
