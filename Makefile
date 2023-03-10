.PHONY: test

install:
	pip install -r requirements.txt

test:
	python -m unittest discover -s database -p '*_test.py'

run-dev:
	export FLASK_RUN_PORT=8000 FLASK_DEBUG=true FLASK_APP=main.py flask run

run-prod:
	export FLASK_RUN_PORT=8000 FLASK_DEBUG=false FLASK_APP=main.py flask run