all:
	uvicorn app:app --host 0.0.0.0 --port 3002 --reload

venv:
	. venv/bin/activate

init:
	python3 -m venv venv ; . venv/bin/activate
	pip install -force-reinstall -r requirements.txt

clean:
	rm -rf venv
