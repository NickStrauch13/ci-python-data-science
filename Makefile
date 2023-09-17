install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=src.lib

format:	
	black src/*.py 

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py
		
all: install lint format test
