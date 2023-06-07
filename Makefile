.PHONY: check-code fix-code build-dist check-dist upload-dist clean

check-code:
	@python -m flake8 django_node_assets
	@python -m isort django_node_assets --check
	@python -m black django_node_assets --check

fix-code:
	@python -m isort django_node_assets
	@python -m black django_node_assets

build-dist: clean
	@python -m build

check-dist:
	@python -m twine check dist/*

upload-dist:
	@python -m twine upload dist/*

clean:
	@rm -rf dist/ django_node_assets.egg-info/
