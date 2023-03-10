install: 
	pip install -r requirements.txt

test: 
	python -m unittest discover -s database -p '*_test.py'

run-local: 
	BOOTSTRAP_SERVERS=localhost:29092 TOPIC="purchases" FLASK_APP=main.py flask run --port=8080
