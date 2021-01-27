install:
	pip install -r requirements.txt

coverage:
	py.test --nomigrations --tb=short --cov=uploads


report:
	py.test --nomigrations --tb=short --cov=uploads --cov-report=html