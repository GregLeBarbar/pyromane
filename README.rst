=================
PyRomane
=================

Cette application a pour but de répondre à mes besoins personnels dans la mise en ligne de contenu privé ou public.
Elle est réalisée en python3 et django 1.11.

Installation
============

créer un virtualenv
-------------------

mkvirtualenv --python=/usr/bin/python3 pyromane

installer les dépendances
-------------------------

pip install -r requirements/local.txt


Convention de codage
====================

Respect des conventions de django qui eux mêmes respectent PEP8.

Pour lancer flake8 :

.. code:: bash

    flake8 --exclude=migrations --max-line-length=120


Bonnes pratiques
================

Respect des bonnes pratiques énoncées dans le livre Two Scoops of django 1.11.


Comment exécuter les tests automatiques
=======================================


1ère solution (sans la couverture)
-----------------------------------

.. code:: bash

    python src/manage.py test --settings=config.settings.test


2ème solution (avec la couverture)
----------------------------------

.. code:: bash

    coverage run --source='.' src/manage.py test --settings=config.settings.test


Pour voir la couverture :

1. Lancer la commande

.. code:: bash

    coverage html

2. Puis ouvrir le fichier *index.html* présent dans *~/pyromane/htmlcov*
