# ==================================================================================== #
# VARIABLES
# ==================================================================================== #

PURPLE := \033[95m
BLUE := \033[94m
GREEN := \033[92m
ORANGE := \033[93m
RED := \033[91m
ENDC := \033[0m
BOLD := \033[1m

# ==================================================================================== #
# MAKEFILE TARGETS
# ==================================================================================== #

.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "$(PURPLE)--- Installing Environment ---$(ENDC)"
	@echo "$(BLUE) > Creating virtual environment and syncing dependencies...$(ENDC)"
	@uv sync --all-groups
	@echo "$(BLUE) > Installing pre-commit hooks...$(ENDC)"
	@uv run pre-commit install
	@echo "$(GREEN)Install complete! Activate the venv with: source .venv/bin/activate$(ENDC)"

.PHONY: check
check: ## Run code quality tools
	@echo "$(PURPLE)--- Running Code Quality Checks ---$(ENDC)"
	@echo "$(BLUE) > Checking lock file consistency...$(ENDC)"
	@uv lock --locked
	@echo "$(BLUE) > Linting code with pre-commit...$(ENDC)"
	@uv run pre-commit run -a
	@echo "$(BLUE) > Static type checking...$(ENDC)"
	@uv run {% if cookiecutter.typechecker == "mypy" %}mypy{% elif cookiecutter.typechecker == "ty" %}ty check{% else %}pyrefly check{% endif %}
	@echo "$(GREEN)All checks passed!$(ENDC)"

.PHONY: test
test: ## Test the code with pytest
	@echo "$(PURPLE)--- Running Tests ---$(ENDC)"
	@echo "$(BLUE) > Running pytest...$(ENDC)"
{% if cookiecutter.codecov == "y" %}
	@uv run python -m pytest --cov --cov-config=pyproject.toml --cov-report=xml
{% else %}
	@uv run python -m pytest tests
{% endif %}
	@echo "$(GREEN)Tests finished!$(ENDC)"

.PHONY: build
build: clean-build ## Build wheel file
	@echo "$(PURPLE)--- Building Project ---$(ENDC)"
	@uv build --wheel
	@echo "$(GREEN)Build successful!$(ENDC)"

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@rm -rf dist

.PHONY: docs
docs: ## Build and serve the documentation
	@uv run mkdocs serve

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@uv run mkdocs build -s

.PHONY: help
help: ## Display this help message
	@echo "$(BOLD)Makefile Commands:$(ENDC)"
	@uv run python -c "import re; \
	[[print(f'  {m[0]:<20} {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
