lint:
	pylint pedigree_fields.py
	
	pylama pedigree_fields.py

	pycodestyle pedigree_fields.py

	pydocstyle pedigree_fields.py

	pyflakes pedigree_fields.py

	cd tests/ && pylint test_pedigree_fields.py

	cd tests/ && pylama test_pedigree_fields.py

	cd tests/ && pycodestyle test_pedigree_fields.py

	cd tests/ && pydocstyle test_pedigree_fields.py

	cd tests/ && pyflakes test_pedigree_fields.py


analyze:
	radon cc pedigree_fields.py

	radon raw pedigree_fields.py

	radon mi pedigree_fields.py

	radon hal pedigree_fields.py

	cd tests/ && radon cc test_pedigree_fields.py

	cd tests/ && radon raw test_pedigree_fields.py

	cd tests/ && radon mi test_pedigree_fields.py

	cd tests/ && radon hal test_pedigree_fields.py

test:
	cd tests/ && pytest

clean:
	rm -r __pycache__
	cd tests/ && rm -r __pycache__