.DEFAULT_GOAL := help
.PHONY: help install install-dev install-all generate-client lint format typecheck test test-cov coverage smoke docs docs-serve build clean

# Use uv if available (faster), otherwise fall back to pip.
PIP := $(shell command -v uv >/dev/null 2>&1 && echo "uv pip" || echo "pip")
PY  := python3

help:  ## Show this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

install:  ## Install runtime dependencies in editable mode
	$(PIP) install -e .

install-dev:  ## Install dev + test dependencies
	$(PIP) install -e ".[dev,test]"

install-all:  ## Install everything (dev + test + docs + client-gen)
	$(PIP) install -e ".[dev,test,docs,client-gen]"

generate-client:  ## Regenerate the typed DefectDojo API client from dd-api.json
	@command -v openapi-python-client >/dev/null 2>&1 || { \
		echo "openapi-python-client not installed. Run: make install-all"; exit 1; \
	}
	@echo "Regenerating client from dd-api.json…"
	@rm -rf src/dd_cli/_client
	@mkdir -p src/dd_cli/_client
	openapi-python-client generate \
		--path dd-api.json \
		--output-path src/dd_cli/_client \
		--meta none \
		--overwrite
	@echo "Client regenerated. Review the diff before committing."

lint:  ## Run ruff lint + format check
	ruff check src tests
	ruff format --check src tests

format:  ## Auto-format with ruff
	ruff check --fix src tests
	ruff format src tests

typecheck:  ## Run mypy --strict
	mypy src

test:  ## Run pytest
	pytest

test-cov:  ## Run pytest with coverage report
	pytest --cov-report=term-missing --cov-report=html

coverage: test-cov  ## Alias for test-cov

smoke:  ## Run integration tests against a live DefectDojo (requires DD_URL + DD_API_KEY)
	@if [ -z "$$DD_URL" ] || [ -z "$$DD_API_KEY" ]; then \
		echo "DD_URL and DD_API_KEY must be set in the environment."; \
		echo "Example:  DD_URL=http://localhost:8080 DD_API_KEY=… make smoke"; \
		exit 1; \
	fi
	pytest -m integration --no-cov -v

docs:  ## Build docs
	mkdocs build --strict

docs-serve:  ## Serve docs locally on :8000
	mkdocs serve

build:  ## Build sdist + wheel
	$(PY) -m build

clean:  ## Remove caches and build artifacts
	rm -rf build/ dist/ *.egg-info src/*.egg-info
	rm -rf .pytest_cache .mypy_cache .ruff_cache .coverage coverage.xml htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
