make: pylint pycodestyle pydocstyle pyflakes test

pylint:
	cd logic/ && pylint __init__.py
	cd logic/ && pylint pedigree_builder.py
	cd logic/ && pylint pedigree_fields.py


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


clean:
	rm -r -f __pycache__
	cd logic/ && rm -r -f __pycache__
	cd tests/ && rm -r -f __pycache__
	cd tests/ && rm -r -f .pytest_cache