#!/usr/bin/python3
"""Fabric file"""

from fabric.api import *
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['142.44.167.236', '144.217.246.202']  # run on both servers
env.key_filename = '~/.ssh/holberton'  # path to my ssh public key


def do_pack():
    """Compress all `web_static` files"""

    now = datetime.now()  # get current date and time
    name = "web_static_" + now.strftime('%Y%m%d%H%M')

    local("mkdir -p versions")  # create dir

    with lcd("versions"):  # inside the version dir
        # compress web_static to .tgz -> archive
        result = local("tar -cvzf {}.tgz ../web_static"
                       .format(name), capture=True)
        print(result)

        path = local("pwd", capture=True)
        result = "{:s}/{:s}.tgz".format(path, name) if result.succeeded else None

    return result  # return the path to archive if successful else None


def do_deploy(archive_path):
    """deploy the web_static"""

    # check if archive exist
    if not os.path.isfile(archive_path):
        return False

    archive = os.path.basename(archive_path)  # get only the archive name
    dirname = "/data/web_static/releases/" + archive[:-4]  # dir path

    try:
        put(archive_path, "/tmp", use_sudo=True)  # transfer file

        run("mkdir -p " + dirname)  # create dir

        with cd("/tmp"):
            run("tar -xzvf {}".format(archive))  # uncompress archive
            run("mv web_static/* {}/".format(dirname))  # movie contents
            run("rm -rf {} web_static".format(archive))  # clear archive

        run("rm /data/web_static/current")  # remove softlink
        run("ln -fs {} /data/web_static/current".format(dirname))  # new link

        print(run("sudo service nginx restart"))  # restart nginx
    except:  # if any of the commands above failed return False
        return False

    return True  # everything ran successfuly


def deploy():
    """Full deployment"""

    archive_path = do_pack()

    deployment_result = do_deploy(archive_path)

    return deployment_result
