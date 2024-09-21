setup:
	pip3 install -r requirements.txt
test_code:
	pytest
lint:
	pylint --errors-only src/main.py
	pylint --errors-only test/test_main.py