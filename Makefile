install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py && black test_*.py

lint:
	pylint --disable=R,C --ignore-patterns=test_*.py *.py

test:
	python -m pytest -vv --cov=main test_*.py *.py

deploy:
	# deploy goes here
		
all: install lint test format