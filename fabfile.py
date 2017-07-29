from contextlib import contextmanager

from fabric.api import run
from fabric.context_managers import cd, prefix
from fabric.operations import local
from fabric.state import env


env.host_string = 'GregLeBarbar@ssh.pythonanywhere.com'
env.project_root_path = '/home/GregLeBarbar/pyromane'
env.virtualenv_path = '/home/GregLeBarbar/.virtualenvs/pyromane'


@contextmanager
def virtualenv():
    """
    Context manager that activate the virtualenv defined in env.virtualenv_path
    """
    with cd(env.project_root_path):
        with prefix('workon pyromane'):
            yield


def django_manage(cmd):
    """
    Run a Django manage command on the remote server.

    :param cmd string: the parameters to be passed to manage.py
    """
    with virtualenv():
        run('python src/manage.py ' + cmd)


def clone():
    """
    
    """
    cmd = "dumpdata --output dumpdata_29_07_2017"
    django_manage(cmd)

    cmd = "scp -r {host_string}:{project_root_path}/dumpdata_29_07_2017.json  /home/greg/workspace-perso/pyromane/".format(**env)
    local(cmd)

    cmd = "loaddata dumpdata_29_07_2017.json"""
    django_manage(cmd)
