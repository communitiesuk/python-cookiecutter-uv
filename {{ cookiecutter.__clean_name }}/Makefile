.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "Creating virtual environment using uv"
	@uv venv
	@uv sync --all-groups
	@uvx pre-commit install
	@uv lock

.PHONY: check
check: ## Run code quality tools.
	@echo "Checking lock file consistency with 'pyproject.toml'"
	@uv lock --locked
	@echo "Running pre-commit"
	@uvx pre-commit run -a
	@echo "Static type checking"
	{%- if cookiecutter.typechecker == 'ty' %}
	@uv run ty
	{% else %}
	@uv run mypy
	{%- endif %}

{% if cookiecutter.include_unit_testing == 'y' -%}
.PHONY: test
test: ## Test the code with pytest
	@echo "Testing code: Running pytest"
	@uv run pytest --cov --cov-config=pyproject.toml --cov-report=xml --color=yes
{%- endif%}

.PHONY: build
build: clean-build ## Build wheel file
	@echo "Creating wheel file"
	@uvx --from build pyproject-build --installer uv

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@echo "Removing build artifacts"
	@rm -rf dist

.PHONY: help
help:
	@uvx python -c "import re; \
	[[print(f'\033[36m{m[0]:<20}\033[0m {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
