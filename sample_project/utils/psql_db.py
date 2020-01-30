from sqlalchemy import create_engine

from sample_project import settings


_psql_engine = None


def get_psql_engine():
    global _psql_engine

    if _psql_engine is None:
        _psql_engine = create_engine(settings.PSQL_URI)

    return _psql_engine


def get_psql_connection():
    return get_psql_engine.connect()
