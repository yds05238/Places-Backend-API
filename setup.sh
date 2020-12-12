#!/bin/sh
# docker rm $(docker ps -a -q)
# docker rmi $(docker images -q)

echo "Building + Running containers"
docker-compose up -d --build

echo "Creating + Seeding DB"
docker-compose exec api python manage.py recreate_db
docker-compose exec api python manage.py seed_db

echo "Linting"
docker-compose exec api flake8 src

echo "Running + Editing using Black"
docker-compose exec api black src 