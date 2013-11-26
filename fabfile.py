"""Management utilities."""

import socket

from fabric.contrib.console import confirm
from fabric.api import abort, env, local, settings, task

def get_local_ip_address(target):
    ipaddr=''
    try:
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((target, 8000))
        ipaddr=s.getsockname()[0]
        s.close()
    except:
        pass

    return ipaddr

SETTINGS='--settings=couple_mission.settings'

DEFAULT_MODE='dev'
DEFAULT_IP=get_local_ip_address('1.1.1.1')
DEFAULT_PORT=8000   

def runserver(mode = DEFAULT_MODE, ip = DEFAULT_IP, port = DEFAULT_PORT):
    ip=DEFAULT_IP
    local("./manage.py runserver_plus %s:%s %s.%s"%(ip, port, SETTINGS, mode))
