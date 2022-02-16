check-code:
	flake8 django_node_assets
	isort django_node_assets --check
	black django_node_assets --check

fix-code:
	isort django_node_assets
	black django_node_assets
