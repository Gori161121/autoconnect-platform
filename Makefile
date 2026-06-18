install:
	pip install -r backend/requirements.txt

run:
	uvicorn backend.main:app --reload

test:
	pytest
