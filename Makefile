install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	pytest -vv --cov=src
	pytest --nbval src/*.ipynb

format:	
	black src/*.py tests/*.py

lint:
	ruff check src/*.py tests/*.py
	nbqa ruff src/*.ipynb

all: install lint format test

summary:
	python src/descriptive_stats.py