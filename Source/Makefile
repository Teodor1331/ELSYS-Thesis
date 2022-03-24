make: pylint pylama pycodestyle pydocstyle pyflakes test

pylint:
	cd logic/ && pylint __init__.py
	cd logic/ && pylint pedigree_builder.py
	cd logic/ && pylint pedigree_fields.py


pylama:
	cd logic/ && pylama __init__.py
	cd logic/ && pylama pedigree_builder.py
	cd logic/ && pylama pedigree_fields.py


pycodestyle:
	cd logic/ && pycodestyle __init__.py
	cd logic/ && pycodestyle pedigree_builder.py
	cd logic/ && pycodestyle pedigree_fields.py


pydocstyle:
	cd logic/ && pydocstyle __init__.py
	cd logic/ && pydocstyle pedigree_builder.py
	cd logic/ && pydocstyle pedigree_fields.py


pyflakes:
	cd logic/ && pyflakes pedigree_fields.py
	cd logic/ && pyflakes pedigree_builder.py


test:
	cd tests/ && pytest test_pedigree_fields.py
	cd tests/ && pytest test_pedigree_builder.py


coverage:
	cd tests/ && coverage run -m pytest test_pedigree_fields.py && coverage html && cd htmlcov && google-chrome index.html
	cd tests/ && coverage run -m pytest test_pedigree_builder.py && coverage html && cd htmlcov && google-chrome index.html


clean:
	rm -r __pycache__
	cd logic/ && rm -r __pycache__
	cd tests/ && rm -r __pycache__
	cd tests/ && rm -r .pytest_cache
	# cd tests/ && rm -r .coverage
	# cd tests/ && rm -r htmlcov/