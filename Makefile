install:
	pip install --upgrade pip &&\
			pip install -r requirements.txt

test:
	python -m pytest -vvv --cov=greting \
		--cov=smath --cov=web tests
	python -m pytest --mbval notbook.ipynb
	#python -m pytest -v tests/test_web.py

debug:
	python -m pytest -vv --pdb

one-test:
	python -m pytest --v tests/test_greeting.py::test_my_name4
format:
	black *.py

lint:
	pylint --disable=R,C hello.py

all: install lint test