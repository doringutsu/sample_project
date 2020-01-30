import click
from flask import Flask

from sample_project import logging, settings


@click.group()
def flask_server():
    pass


_logger = logging.logger('commands.flask_server')
app = Flask(__name__)

"""
We'll have a nice class (a service) that will properly handle all the controllers
- nice starting example - https://flask.palletsprojects.com/en/1.1.x/quickstart/#a-minimal-application
"""
@app.route('/')
def hello():
    _logger.info('Received a new request to the resource /')
    return "Hello World!"


@flask_server.command(short_help='start the Flask server')
def start():
    app.run(host=settings.FLASK_HOST, port=settings.FLASK_PORT)
