
#!/usr/bin/python
"""Fabric file"""

from fabric.api import *
env.user = 'ubuntu'
env.hosts = ['142.44.167.236', '144.217.246.202']
env.key_filename = '~/.ssh/holberton'

def do_ln():
    """deploy the web_static"""

    run("rm /data/web_static/current")
    run("ln -fs /data/web_static/releases/web_static_201711210147 /data/web_static/current")
