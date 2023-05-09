install:
	pip install -r test_requirements.txt

coverage:
	py.test --nomigrations --tb=short --cov=uploads

report:
	py.test --nomigrations --tb=short --cov=uploads --cov-report=html