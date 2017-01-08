===========
Hébergement
===========

L'application est hébergée sur pythonanywhere.com.


| Cette solution est simple d'utilisation.

Presque toute la configuration peut se faire dans l'interface web directement :
`https://www.pythonanywhere.com/user/GregLeBarbar/webapps/#tab_id_greglebarbar_pythonanywhere_com <https://www.pythonanywhere.com/user/GregLeBarbar/webapps/#tab_id_greglebarbar_pythonanywhere_com>`_

Virtualenv
==========

Pour la création du virtualenv nous avons utilisé Virtualenvwrapper.


Variable environnement DJANGO_SETTINGS_MODULE
---------------------------------------------

Nous avons définit la variable d'environnement **DJANGO_SETTINGS_MODULE** dans le fichier postactivate situé :

``/home/GregLeBarbar/.virtualenvs/pyromane/bin``

.. code:: bash

    export DJANGO_SETTINGS_MODULE=config.settings.prod


Astuce
------
Nous avons créé le fichier .project dans ``/home/GregLeBarbar/.virtualenvs/pyromane/``

ce fichier contient le répertoire racine du projet


.. code:: bash

    /home/GregLeBarbar/pyromane


Configuration WSGI
==================

Pour la configuration WSGI, if suffit :

1. d'ajouter le répertoire contenant le fichier ``wsgi.py`` au **pythonpath**
2. d'importer la variable application

Voici le code correspondant situé dans le fichier ``/var/www/greglebarbar_pythonanywhere_com_wsgi.py``

.. code:: python

    import sys

    path = '/home/GregLeBarbar/pyromane/src/config'

    if path not in sys.path:
        sys.path.append(path)

    from wsgi import application

Voici le contenu du fichier ``wsgi.py`` situé dans ``pyromane/src/config/`` :

.. code:: python

    import os
    import sys

    path = '/home/GregLeBarbar/pyromane/src'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings.prod'

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()


Base de données
===============

Avec un compte gratuit, on ne peut utiliser que MySQL.
C'est la solution retenue en attendant de passer à un compte payant et ainsi pouvoir utiliser postgreSQL,
la base de données recommandée pour django.

Pour se connecter à la base de données
---------------------------------------

On peut :
- soit lancer une console MySQL directement dans la partie admin de l'hébergeur
- soit lancer une console bash directement dans la partie admin de l'hébergeur puis :
mysql 'GregLeBarbar$pyromane' -uGregLeBarbar -pxxxxx -h 'GregLeBarbar.mysql.pythonanywhere-services.com'


Pour faire un dump de la base de données
----------------------------------------

Lancer une console bash directement dans la partie admin de l'hébergeur.
Puis

mysqldump 'GregLeBarbar$pyromane' -uGregLeBarbar -pxxxxx -h 'GregLeBarbar.mysql.pythonanywhere-services.com' > dump.sql


