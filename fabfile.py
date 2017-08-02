from contextlib import contextmanager

from fabric.api import run
from fabric.context_managers import cd, prefix
from fabric.operations import local
from fabric.state import env


env.host_string = 'GregLeBarbar@ssh.pythonanywhere.com'
env.project_root_path = '/home/GregLeBarbar/pyromane'
env.local_project_root_path = "/home/greg/workspace-perso/pyromane/"
env.virtualenv_path = '/home/GregLeBarbar/.virtualenvs/pyromane'


@contextmanager
def virtualenv():
    """
    Context manager that activate the virtualenv defined in env.virtualenv_path
    """
    with cd(env.project_root_path):
        with prefix('workon pyromane'):
            yield


def django_manage(cmd, local_env=True):
    """
    Run a Django manage command on the remote server.

    :param cmd string: the parameters to be passed to manage.py
    """
    if local_env:
        # run django cmd on the local server
        local("python src/manage.py %s" % cmd)

    else:
        # run django cmd on the prod server
        with virtualenv():
            run('python src/manage.py ' + cmd)


def deploy():

    with cd(env.project_root_path):
        run("git pull")
        run("touch /var/www/greglebarbar_pythonanywhere_com_wsgi.py")


def clone():
    """
    Le but de cette commande est de permettre de récupérer les données
    c'est à dire le contenu de la base de données et les fichiers uploadés
    par l'utilisateur.

    Amélioration 1 :

    Avant de lancer 'fab clone'
    Il faut pour l'instant supprimer la base de données pyromane et la recréer à vide.
    Ceci peut bien sûr être automatisé

    Amélioration 2 :
    La date compris dans le nom du dump doit devenir un timestamp ou autre.
    """

    # création d'un dump de la base de données au format json
    cmd = "dumpdata --indent 4 --output dumpdata_30_07_2017.json"
    django_manage(cmd, local_env=False)

    # copier le dump sur la machine locale
    cmd = "scp -r {host_string}:{project_root_path}/dumpdata_30_07_2017.json " \
          "{local_project_root_path}".format(**env)
    local(cmd)

    # supprimer les enregistrements de la table django_content_type
    python_shell = "from django.contrib.contenttypes.models import ContentType;ContentType.objects.all().delete();"
    cmd = "shell --command='{0}'".format(python_shell)
    django_manage(cmd, local_env=True)

    # charger le dump
    cmd = "loaddata dumpdata_30_07_2017.json"""
    django_manage(cmd, local_env=True)
