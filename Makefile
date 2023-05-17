install:
	cp .env.dev .env
	@make build
	@make up
	@make migrate
	@make superuser

build:
	docker compose build

up:
	docker compose up -d

migrate:
	docker compose exec app python manage.py migrate

superuser:
	docker compose exec app python manage.py createsuperuser

test:
	docker compose exec app python manage.py test

lint:
	docker compose exec app flake8

app-bin:
	docker compose exec app /bin/sh