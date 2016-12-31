Respect des bonnes pratiques énoncés dans le livre Two Scoops of django 1.8

1. Style de codage :

Respect des conventions de django ce qui inclut PEP8

Utilisation de flake 8 :

flake8 --exclude=migrations --max-line-length=120

Astuces :
- les fichiers contenant cette ligne sont ignorés : # flake8: noqa
- les lignes contenant un commentaire # noqa à la fin sont ignorés


Détection automatique des erreurs flake8 avec git :
http://zds-site.readthedocs.io/fr/latest/utils/git-pre-hook.html?highlight=commit


2. La mise en place d'un environnement optimal de Django

3.

Structure

4. Fondements du design d'une application Django

5. Fichiers de Settings et de Requirements

- 1 fichier de settings par environnement
- 1 fichier de settings base pour la configuration commune
- utilisation de unipath pour gérer les chemins relatifs du projet
    -> BASE_DIR coorespond à la racine du projet
    BASE_DIR.child('db.sqlite3') permet de créer le fichier de la BD à la racine du projet
- Ajout dans le fichier postactivate du virtualenv de la variable d'environnement DJANGO_SETTINGS_MODULE
export DJANGO_SETTINGS_MODULE=config.settings.local
Ainsi, lorsque l'on activate le virtualenv, on indique grâce à cette variable d'environnement quel fichier de settings
doit être utilisé

- Fichier secrets.json pour sortir des clés secrètes



6. Bonnes pratiques des modèles

- Chaque modèle hérite de la classe TimeStampedModel

13. Templates: Bonnes pratiques

Pour l'organisation des templates, je préfère avoir les templates par application.


22. Les tests pue et c'est un gaspillage d'argent

- coverage :

https://confluence.epfl.ch:8443/display/SIAC/Couverture+de+code
+ définir un ficher .coveragerc pour par exemple exclure certains fichiers/: wsgi.py, manage.py etc


23. Documentation: Être obsédé

- Utiliser reStructuredText pour la doc python

