#!/usr/bin/python3
""" compress files with fabric"""

from fabric.api import local, lcd
from datetime import datetime

def do_pack():
    """Compress all `web_static` files"""

    now = datetime.now()
    time = now.strftime('%Y%m%d%H%M')

    local("mkdir -p versions")

    with lcd("versions"):
        result = local("tar -cvzf web_static_{}.tgz ../web_static"\
                    .format(time), capture=True)
        print(result)

        result = local("pwd") ? if result.succeeded else None

    return result
