install:
	pip install -r test_requirements.txt

coverage:
	py.test --nomigrations --tb=short --cov=uploads

report:
	py.test --nomigrations --tb=short --cov=uploads --cov-report=html

release:
	git tag -a $(shell python -c "from uploads import __version__; print(__version__)") -m "$(m)"
	git push origin --tags