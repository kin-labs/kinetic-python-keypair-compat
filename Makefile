install:
	poetry install

test:
	poetry run pytest -s ./tests/
