import click

from sqlalchemy_utils import create_database, database_exists, drop_database

from sample_project import logging
from sample_project import settings
from sample_project.utils.psql_db import get_psql_engine


_logger = logging.logger('commands.psql_db')


@click.group()
def psql_db():
    pass


@psql_db.command(short_help='create PostgreSQL database')
def create():
    error_msg = 'You can run this command only in development / test env'
    assert settings.PROJECT_ENV in ['development', 'test'], error_msg

    engine = get_psql_engine()

    if database_exists(engine.url):
        _logger.info('Database already exists with URI - %s', engine.url)
    else:
        create_database(engine.url)
        _logger.info('Database succesfully created with URI - %s', engine.url)


@psql_db.command(short_help='drop PostgreSQL database')
def drop():
    error_msg = 'You can run this command only in development / test env'
    assert settings.PROJECT_ENV in ['development', 'test'], error_msg

    engine = get_psql_engine()

    if database_exists(engine.url):
        drop_database(engine.url)
        _logger.info('Database succesfully dropped - %s', engine.url)
    else:
        _logger.info('Database doesn\'t exist with URI - %s', engine.url)
