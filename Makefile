dev-start:
	python manage.py runserver --settings=config.settings.dev
dev-install:
	pip install -r requirements/dev.txt
base-install:
	pip install -r requirements/base.txt
dev-migrate:
	python manage.py migrate --settings=config.settings.dev

dev-makemigrations:
	python manage.py makemigrations --settings=config.settings.dev
dev-test:
	python manage.py test  --settings=config.settings.dev