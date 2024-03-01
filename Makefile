run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

createuser:
	python manage.py createsuperuser

static:
	python manage.py collectstatic