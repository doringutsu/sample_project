import click

from sample_project import logging
from sample_project.utils.mongo_db import get_mongo_db


_logger = logging.logger('commands.mongo_db')


@click.group()
def mongo_db():
    pass


@mongo_db.command(short_help='insert a sample item in the database')
def insert():
    sample_record = {'_id': 1, 'test_field': 'test_value'}
    table_name = 'test_table'
    db = get_mongo_db()

    # inserting data into the database here
    db[table_name].insert(sample_record)

    _logger.info('Inserted %s into table - %s', sample_record, table_name)


@mongo_db.command(short_help='display sample data from the database')
def display():
    table_name = 'test_table'
    db = get_mongo_db()

    # requesting data from the database here
    data = list(db[table_name].find())

    _logger.info('Retrieved %s records from table - %s', len(data), table_name)
    _logger.info('Records - %s', data)
