.PHONY: check-code fix-code build-dist check-dist upload-dist clean

check-code:
	@python -m ruff check
	@python -m ruff format --check

fix-code:
	@python -m ruff check --fix
	@python -m ruff format

build-dist: clean
	@python -m build

check-dist:
	@python -m twine check dist/*

upload-dist:
	@python -m twine upload dist/*

clean:
	@rm -rf dist/ django_node_assets.egg-info/
