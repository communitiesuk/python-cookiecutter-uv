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
uvx cookiecutter https://github.com/communitiesuk/python-cookiecutter-uv.git
```

Or if you do not have `uv` installed:

```bash
pip install cookiecutter
cookiecutter https://github.com/communitiesuk/python-cookiecutter-uv.git
```

Or clone and use `cookiecutter` locally:

```bash
git clone https://github.com/communitiesuk/python-cookiecutter-uv.git
cookiecutter python-cookiecutter-uv
```
