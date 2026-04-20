# ==================================================================================== #
# VARIABLES
# ==================================================================================== #

# Makefile Colors
PURPLE := \033[95m
BLUE := \033[94m
CYAN := \033[96m
GREEN := \033[92m
ORANGE := \033[93m
RED := \033[91m
ENDC := \033[0m
BOLD := \033[1m
UNDERLINE := \033[4m


# ==================================================================================== #
# MAKEFILE TARGETS
# ==================================================================================== #

.PHONY: install
install: ## Install the virtual environment and install the pre-commit hooks
	@echo "$(PURPLE)--- 🚀 Installing Environment ---$(ENDC)"
	@echo "$(BLUE) > Creating virtual environment and syncing dependencies...$(ENDC)"
	@uv sync --all-groups
	@echo "$(BLUE) > Installing pre-commit hooks...$(ENDC)"
	@uvx pre-commit install
	@echo "$(BLUE) > Creating lock file...$(ENDC)"
	@uv lock
	@echo "$(GREEN)✅ Install complete! Activate the venv with: source .venv/bin/activate$(ENDC)"


.PHONY: check
check: ## Run code quality tools.
	@echo "$(PURPLE)--- 🧐 Running Code Quality Checks ---$(ENDC)"
	@echo "$(BLUE) > Checking lock file consistency...$(ENDC)"
	@uv lock --locked
	@echo "$(BLUE) > Linting code with pre-commit...$(ENDC)"
	@uvx pre-commit run -a
	@echo "$(BLUE) > Sorting dependencies with uv-sort...$(ENDC)"
	@uvx uv-sort
	@echo "$(BLUE) > Running noxfile...$(ENDC)"
	@uvx nox
	@echo "$(GREEN)✅ All checks passed!$(ENDC)"

{% if cookiecutter.include_unit_testing == 'y' -%}
.PHONY: test
test: ## Test the code with pytest
	@echo "$(PURPLE)--- 🧪 Running Tests ---$(ENDC)"
	@echo "$(BLUE) > Running pytest with coverage report...$(ENDC)"
	@uvx pytest --cov --cov-config=pyproject.toml --cov-report=xml --color=yes
	@echo "$(GREEN)✅ Tests finished!$(ENDC)"
{%- endif%}

.PHONY: build
build: clean-build ## Build wheel file
	@echo "$(PURPLE)--- 📦 Building Project ---$(ENDC)"
	@echo "$(BLUE) > Creating wheel file...$(ENDC)"
	@uv build --wheel
	@echo "$(GREEN)✅ Build successful! Find the wheel in the 'dist' directory.$(ENDC)"

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@echo "$(ORANGE)--- 🧹 Cleaning Build Artifacts ---$(ENDC)"
	@rm -rf dist
	@echo "$(GREEN)✅ 'dist' directory removed.$(ENDC)"

.PHONY: help
help: ## Display this help message
	@echo "$(BOLD)Makefile Commands:$(ENDC)"
	@uvx python -c "import re; \
	[[print(f'  {m[0]:<20} {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
