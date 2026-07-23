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

.PHONY: bake
bake: ## Bake without inputs and overwrite if exists
	@echo "$(PURPLE)--- Baking project with defaults ---$(ENDC)"
	@uv run cookiecutter --no-input . --overwrite-if-exists
	@echo "$(GREEN)Bake complete!$(ENDC)"

.PHONY: bake-with-inputs
bake-with-inputs: ## Bake with interactive inputs
	@uv run cookiecutter . --overwrite-if-exists

.PHONY: install
install: ## Install the virtual environment and pre-commit hooks
	@echo "$(PURPLE)--- Installing Environment ---$(ENDC)"
	@echo "$(BLUE) > Creating virtual environment and syncing dependencies...$(ENDC)"
	@uv sync
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
	@echo "$(BLUE) > Static type checking: Running pyrefly...$(ENDC)"
	@uv run pyrefly check
	@echo "$(BLUE) > Checking for obsolete dependencies: Running deptry...$(ENDC)"
	@uv run deptry .
	@echo "$(GREEN)All checks passed!$(ENDC)"

.PHONY: test
test: ## Test the code with pytest
	@echo "$(PURPLE)--- Running Tests ---$(ENDC)"
	@echo "$(BLUE) > Running pytest...$(ENDC)"
	@uv run python -m pytest tests
	@echo "$(GREEN)Tests finished!$(ENDC)"

.PHONY: build
build: clean-build ## Build wheel file
	@echo "$(PURPLE)--- Building Project ---$(ENDC)"
	@echo "$(BLUE) > Creating wheel file...$(ENDC)"
	@uv build --wheel
	@echo "$(GREEN)Build successful! Find the wheel in the 'dist' directory.$(ENDC)"

.PHONY: clean-build
clean-build: ## Clean build artifacts
	@echo "$(ORANGE)--- Cleaning Build Artifacts ---$(ENDC)"
	@rm -rf dist
	@echo "$(GREEN)'dist' directory removed.$(ENDC)"

.PHONY: docs-test
docs-test: ## Test if documentation can be built without warnings or errors
	@echo "$(PURPLE)--- Testing Documentation Build ---$(ENDC)"
	@uv run mkdocs build -s
	@echo "$(GREEN)Documentation builds successfully!$(ENDC)"

.PHONY: docs
docs: ## Build and serve the documentation
	@echo "$(PURPLE)--- Serving Documentation ---$(ENDC)"
	@uv run mkdocs serve

.PHONY: help
help: ## Display this help message
	@echo "$(BOLD)Makefile Commands:$(ENDC)"
	@uv run python -c "import re; \
	[[print(f'  {m[0]:<20} {m[1]}') for m in re.findall(r'^([a-zA-Z_-]+):.*?## (.*)$$', open(makefile).read(), re.M)] for makefile in ('$(MAKEFILE_LIST)').strip().split()]"

.DEFAULT_GOAL := help
