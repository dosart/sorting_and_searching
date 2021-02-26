.PHONY: install selfcheck test lint check build

install:
	 poetry install

selfcheck:
	poetry check

test:
	poetry run python -m pytest tests/

lint:
	poetry run flake8 algorithms

check: selfcheck test lint

build: check
	poetry build

cc-coverage:
	poetry run python -m pytest --cov=algorithms tests/ --cov-report=xml