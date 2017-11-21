#!/usr/bin/python
"""Fabric file"""

from fabric.api import *
from fabric.contrib import files
from datetime import datetime
import os

def do_pack():
    """Compress all `web_static` files"""

    now = datetime.now()
    name = "web_static_" + now.strftime('%Y%m%d%H%M')

    local("mkdir -p versions")

    with lcd("versions"):
        result = local("tar -cvzf {}.tgz ../web_static"\
                    .format(name), capture=True)
        print(result)

        path = local("pwd")
        result = "{:s}/{:s}".format(path, name) if result.succeeded else None

    return result

env.user = 'ubuntu'
env.hosts = ['142.44.167.236']
env.key_filename = '~/.ssh/holberton'

def do_deploy(archive_path):
    """deploy the web_static"""

    if not files.exists(archive_path):
        return False

    base = os.path.basename(archive_path)
    dirname = os.path.splittext(base)[0]

    try:
        put(archive_path, "/tmp/", use_sudo=True)
        run("tar -xzvf {} -C /data/web_static/releases/{}".\
                format(archive_path, dirname))
        run("rm -rf {}".format(archive_path))
        sudo("ln -fs /data/web_static/releases/{} /data/web_static/current".\
                format(dirname))
    except:
        return False
    else:
        return True
