===================
Environnement local
===================


Virtualenv
==========

Pour la création du virtualenv nous avons utilisé Virtualenvwrapper.


Variable environnement DJANGO_SETTINGS_MODULE
---------------------------------------------

Nous avons définit la variable d'environnement **DJANGO_SETTINGS_MODULE** dans le fichier postactivate situé :

``/home/greg/.virtualenvs/pyromane/bin``

.. code:: bash

    export DJANGO_SETTINGS_MODULE=config.settings.prod


Astuce
------
Nous avons créé le fichier .project dans ``/home/greg/.virtualenvs/pyromane/``

ce fichier contient le répertoire racine du projet


.. code:: bash

    /home/greg/pyromane


PyCharm
=======

