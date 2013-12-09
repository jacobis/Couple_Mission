import socket
import multiprocessing

from gevent import monkey
monkey.patch_all()

# utils


def get_local_ip_address(target):
    ipaddr = ''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((target, 8000))
        ipaddr = s.getsockname()[0]
        s.close()
    except:
        pass

    return ipaddr

# Server Socket
bind = get_local_ip_address('127.0.0.1') + ':8001'
backlog = 2048

# Worker Processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gevent'
worker_connections = 1000
timeout = 60


def def_post_fork(server, worker):
    from psycogreen.gevent import patch_psycopg
    patch_psycopg()
    worker.log.info("Made Psycopg Green")

post_fork = def_post_fork


# Server Mechanics
preload_app = True
daemon = False  # this allows supervisor to correctly handle gunicorn
pidfile = 'gunicorn.pid'

# Log
errorlog = 'gunicorn.log'
loglevel = 'warning'
