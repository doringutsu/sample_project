import click
import socket

from sample_project import logging, settings


_logger = logging.logger('commands.socket_server')


@click.group()
def socket_server():
    pass


@socket_server.command(short_help='start the sockets server')
def start():
    """
    This would look much better and more organised with more time invested
    Comprehensive tutorials here
    - https://docs.python.org/3/howto/sockets.html
    - https://realpython.com/python-sockets
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((settings.SOCKETS_HOST, settings.SOCKETS_PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            _logger.info('[server] New connection from - %s', addr)

            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


@socket_server.command(short_help='connect and send a message to the socket server')
def message():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((settings.SOCKETS_HOST, settings.SOCKETS_PORT))
        s.sendall(b'Hello, world')
        data = s.recv(1024)

    _logger.info('[client] Received message from server - %s', repr(data))
