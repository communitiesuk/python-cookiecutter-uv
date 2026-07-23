# Tutorial

## Prerequisites

- [uv](https://docs.astral.sh/uv/) installed
- [Git](https://git-scm.com/) installed
- A GitHub account with a repository ready

## Step 1: Generate Your Project

```bash
uvx cookiecutter gh:communitiesuk/python-cookiecutter-uv
```

Answer the prompts. The post-generation hook will:

1. Initialize a git repository
2. Install dependencies with uv
3. Run pre-commit hooks
4. Push `main` and `develop` branches to your remote

## Step 2: Enable GitHub Pages

1. Go to your repository Settings > Pages
2. Set Source to "GitHub Actions"
3. The `docs.yml` workflow will deploy on every push to main

## Step 3: Start Developing

```bash
cd your-project-name
git checkout develop
```

Available commands:

```bash
make install    # Re-sync environment
make check      # Run linting + type checking
make test       # Run tests
make docs       # Preview docs locally
make build      # Build wheel
```

## Step 4: Multi-Version Testing

Run tox locally to test across Python versions:

```bash
tox
```

This requires Python 3.12, 3.13, and 3.14 installed. Alternatively, rely on CI which runs the matrix automatically.
