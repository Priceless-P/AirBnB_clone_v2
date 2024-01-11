#!/usr/bin/python3
"""
Generates a .tgz archive using do_pack fun
"""
from fabric.api import local, run, put, env
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive"""
    try:
        date = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        archive_name = "web_static_{}.tgz".format(date)
        full_path = "versions/{}".format(archive_name)
        local("tar -cvzf {} web_static/".format(full_path))
        return full_path
    except:
        return None

def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    env.hosts = ['52.201.221.134', '52.87.219.193']
    env.user = 'ubuntu'
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_filename = os.path.basename(archive_path)
        folder = "/data/web_static/releases/{}".format(archive_filename.split('.')[0])
        run("tar xvf /tmp/{} -C {}".format(archive_path, folder))
        run("sudo rm /tmp/{}".format(archive_path))
        current_link = "/data/web_static/current"
        run("rm -f {}".format(current_link))
        run("sudo ln -s {} {}".format(folder, current_link))
        print("New version deployed!")
        return True
    except Exception:
        return False