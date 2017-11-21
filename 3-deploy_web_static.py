#!/usr/bin/python3
"""Fabric file"""

from fabric.api import *
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['142.44.167.236', '144.217.246.202']
env.key_filename = '~/.ssh/holberton'


def do_pack():
    """Compress all `web_static` files"""

    now = datetime.now()
    name = "web_static_" + now.strftime('%Y%m%d%H%M')

    local("mkdir -p versions")

    with lcd("versions"):
        result = local("tar -cvzf {}.tgz ../web_static"
                       .format(name), capture=True)
        print(result)

        path = local("pwd", capture=True)
        result = "{:s}/{:s}.tgz".format(path, name) if result.succeeded else None

    return result


def do_deploy(archive_path):
    """deploy the web_static"""

    if not os.path.isfile(archive_path):
        return False

    archive = os.path.basename(archive_path)
    dirname = "/data/web_static/releases/" + archive[:-4]

    try:
        put(archive_path, "/tmp", use_sudo=True)

        run("mkdir -p " + dirname)

        with cd("/tmp"):
            run("tar -xzvf {}".format(archive))
            run("mv web_static/* {}/".format(dirname))
            run("rm -rf {} web_static".format(archive))

        run("rm /data/web_static/current")
        run("ln -fs {} /data/web_static/current".format(dirname))

        print(run("sudo service nginx restart"))
    except:
        return False

    return True


def deploy():
    """Full deployment"""

    archive_path = do_pack()

    deployment_result = do_deploy(archive_path)

    return deployment_result
