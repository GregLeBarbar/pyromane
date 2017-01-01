=================
Gestion des slugs
=================

Chaque page possède une URL.
Pour cela le modèle Page a un champ slug.
Grâce à la librairie tierce autoslug, le slug est généré à partir du titre de la page.

Problème
========

A chaque fois que l'utilisateur change de titre, un nouveau slug va être généré donc une nouvelle URL.
Or l'ancienne ou les anciennes URLs doivent toujours répondre et rediriger sur la nouvelle URL

Solution
========

L'application de redirection de django permet de gérer ces redirections
https://docs.djangoproject.com/fr/1.10/ref/contrib/redirects/
