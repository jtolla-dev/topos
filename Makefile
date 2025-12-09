.PHONY: run stop nuke test check fmt migrate logs help

# Default target
help:
	@echo "Strata Development Commands"
	@echo ""
	@echo "  make run      - Start all services (db, api, worker, agent, samba)"
	@echo "  make stop     - Stop all services"
	@echo "  make nuke     - Stop and remove all containers, volumes, and images"
	@echo "  make test     - Run tests"
	@echo "  make check    - Run all code quality checks (ruff, vulture, bandit)"
	@echo "  make fmt      - Format code with ruff"
	@echo "  make typecheck - Run mypy type checking"
	@echo "  make migrate  - Run database migrations"
	@echo "  make logs     - Tail logs from api and worker"
	@echo ""

# Start all services
run:
	docker-compose up -d --build
	@echo ""
	@echo "Services started. Run 'make logs' to view logs."
	@echo "API available at http://localhost:8000"

# Stop all services
stop:
	docker-compose down

# Nuclear option - remove everything
nuke:
	docker-compose down -v --rmi local --remove-orphans
	@echo ""
	@echo "All containers, volumes, and local images removed."

# Run tests
test:
	docker-compose exec api pytest -v

# Run all code quality checks
check:
	uvx pre-commit run --all-files

# Format code
fmt:
	uvx ruff format .
	uvx ruff check --fix .

# Run type checking
typecheck:
	uvx pyright strata/ strata_agent/

# Run database migrations
migrate:
	docker-compose exec api alembic upgrade head

# Tail logs
logs:
	docker-compose logs -f api worker
