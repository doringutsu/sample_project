import click

from sample_project.commands import (
    flask_server, mongo_db, psql_db, socket_server
)


@click.group()
def cli():
    pass


cli.add_command(flask_server)
cli.add_command(mongo_db)
cli.add_command(psql_db)
cli.add_command(socket_server)


if __name__ == '__main__':
    cli()
