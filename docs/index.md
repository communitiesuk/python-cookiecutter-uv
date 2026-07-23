# python-cookiecutter-uv

A production-ready Python cookiecutter template using [uv](https://docs.astral.sh/uv/) for dependency management.

## Overview

This template generates a Python project with:

- **uv** for fast, reliable dependency management
- **tox-uv** for multi-Python-version testing (3.12, 3.13, 3.14)
- **mkdocs** with Material theme for documentation on GitHub Pages
- **ruff** for linting and formatting
- **pre-commit** with security hooks (detect-secrets, IP detection)
- **GitHub Actions** CI/CD (quality, tests, docs deployment)
- Type checking via **mypy**, **ty**, or **pyrefly** (your choice)

## Quick Start

```bash
uvx cookiecutter gh:communitiesuk/python-cookiecutter-uv
```

Or clone and bake locally:

```bash
git clone https://github.com/communitiesuk/python-cookiecutter-uv.git
cd python-cookiecutter-uv
make bake-with-inputs
```
