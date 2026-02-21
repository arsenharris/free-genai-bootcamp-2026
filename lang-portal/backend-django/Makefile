VENV=.venv
PY=$(VENV)/bin/python
PIP=$(VENV)/bin/pip

.PHONY: init migrate seed run

init:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

migrate:
	$(PY) manage.py migrate

seed:
	$(PY) manage.py seed

run:
	$(PY) manage.py runserver
