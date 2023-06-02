## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

#### Docker 

La commande unique afin de récupérer l'image et la lancer sur Docker Desktop:

`docker pull trksdi/oc_p13:v1 && docker run -p 8000:8000 trksdi/oc_p13:v1`

#### Deploiement

##### Configuration requise

- Accès au compte [GitHub](https://github.com/) (Workflow)
- Accès au compte [DockerHub](https://hub.docker.com/) (Image)
- Accès au compte [Heroku](https://id.heroku.com/) (Déploiement)
- Accès au compte [Sentry](https://sentry.io/) (Surveillance erreur)

##### Fonctionnement 

- Le workflow CI/CD se fait à travers la plateforme GitHub Actions
- Il procède au lancement des tests dans un premier temps. 
- Si les tests passent avec succès, il procède à la construction d'une image Docker et la 
sauvegarde sur la plateforme DockerHub
- Si la construction et la sauvegrade l'image Docker sont réussies, il procède au déploiement sur 
la platforme Heroku
- Le déploiement est accessible sur ce lien : [LIEN](https://fast-gorge-63898.herokuapp.com/)
- Après le déploiement, une veille erreur est mise en place avec l'outil Sentry

IMPORTANT : Le déploiement est déclenché à chaque mise à jour de la branche `main`

##### Etapes de mise en place

###### GitHub

- Allez sur l'onglet `Actions` et créer un nouveau workflow




### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

