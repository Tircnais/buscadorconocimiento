# backend-buscador-conocimiento
Sistema recomendador basado en el conocimiento. Backend en Django. 

# GITHUB
1 git add .
2 git commit -m "Titulo" -m "Describe"
2 git push

# HEROKU
This worked for me, run the following commands:
En su sitio se puede elegir cual rama desplegar

## Install
1. sudo snap install --classic heroku
2. heroku --version

## Update
1. heroku update
2. apt
3. sudo apt-get update && sudo apt-get upgrade heroku

## Create Database
1. Revisar la base de datos (existentes)[https://elements.heroku.com/addons/]
2. Usar el comando proporcionado
 - heroku addons:create heroku-postgresql:hobby-dev
 - Documentacion y agregar al proyecto
3. Add lib **django-heroku==0.3.1** a requirements

## Connect project
1. git remote -v
2. heroku git:remote -a name_project
3. git push heroku master


## Si ya existe project
1. git add .
2. git commit -m "titulo" -m "Descripcion"
3. git push heroku master

## Getting started
1. heroku login

## Create App
python manage.py collectstatic --noinput
	
1. disable the collectstatic during a deploy

DEBUG_COLLECTSTATIC

	heroku config:set DEBUG_COLLECTSTATIC=1
Disabling Collectstatic

	heroku config:set DISABLE_COLLECTSTATIC=1
	_ heroku config:set DISABLE_COLLECTSTATIC=0
2.   deploy

	git push heroku master

3.  run migrations (django 1.10 added at least one)

	heroku run python manage.py migrate
	- heroku run python manage.py shell
	- heroku run python manage.py makemigrations servidor

4.  run collectstatic using bower (optional)

	heroku run 'bower install --config.interactive=false;grunt prep;python manage.py collectstatic --noinput'

5.  enable collecstatic for future deploys

	heroku config:unset DISABLE_COLLECTSTATIC

6.  try it on your own (optional)

	Multiples BD
	heroku run python manage.py collectstatic --noinput
	python manage.py migrate --noinput --database=db_2
	python manage.py collectstatic --noinput

future deploys should work as normal from now on

7.  Open or lift Heroku project

	heroku open
	- heroku logs
8.  Create superuser

	heroku run python manage.py createsuperuser

The application is now deployed. Ensure that at least one instance of the app is running:

heroku ps:scale web=1


heroku logs  # Show current logs
heroku logs --tail # Show current logs and keep updating with any new results
heroku config:set DEBUG_COLLECTSTATIC=1 # Add additional logging for collectstatic (this tool is run automatically during a build)
heroku ps   #Display dyno status

Lista de BD
heroku addons
heroku addons:open jawsdb-maria