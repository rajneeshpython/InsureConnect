# 🚀 Docker + Postgres + Django Cheatsheet for InsureConnect

## 🔹 Docker Basics
```bash
# Build and start containers (fresh build)
docker compose up --build

# Start in detached mode
docker compose up -d

# Stop all running containers
docker compose down

# Stop and remove everything (containers, networks, volumes, images)
docker compose down -v --rmi all

# List running containers
docker ps

# View logs (all services)
docker compose logs -f

# View logs of a specific service
docker compose logs -f web
docker compose logs -f worker
docker compose logs -f beat
docker compose logs -f db
🔹 PostgreSQL Commands (inside container)
1. Access Postgres

docker exec -it insureconnect-db psql -U postgres -d insureconnect
2. Useful psql Commands

-- List all databases
\l

-- Connect to a database
\c insureconnect

-- List all tables
\dt

-- Describe a table
\d tablename

-- Show current user
\du

-- Exit psql
\q
🔹 Django-Specific Commands
Run Django commands inside container

# Migrations
docker compose exec web python manage.py makemigrations
docker compose exec web python manage.py migrate

# Create superuser
docker compose exec web python manage.py createsuperuser

# Open Django shell
docker compose exec web python manage.py shell

# Run tests
docker compose exec web python manage.py test
🔹 Celery & Redis

# Check Celery worker logs
docker compose logs -f worker

# Check Celery beat logs
docker compose logs -f beat

# Check Redis logs
docker compose logs -f redis
🔹 Cleanup

# Remove all stopped containers
docker container prune -f

# Remove all unused images
docker image prune -a -f

# Remove all unused volumes
docker volume prune -f

# fixture data load into DB
docker-compose exec web python manage.py loaddata apps/insurers/fixtures/mock_data.json
