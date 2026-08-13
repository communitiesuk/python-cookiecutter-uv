# python-cookiecutter-uv

[![Build status](https://img.shields.io/github/actions/workflow/status/communitiesuk/python-cookiecutter-uv/main.yml?branch=main)](https://github.com/communitiesuk/python-cookiecutter-uv/actions/workflows/main.yml?query=branch%3Amain)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://communitiesuk.github.io/python-cookiecutter-uv/)

A Python cookiecutter template using [uv](https://docs.astral.sh/uv/) for dependency management.

## Features

- **`uv`** for fast, reliable dependency management
- **`tox-uv`** for multi-Python-version testing (3.12, 3.13, 3.14)
- **`mkdocs`** with Material theme for documentation on GitHub Pages
- **`ruff`** for linting and formatting
- **`deptry`** for detecting obsolete or missing dependencies
- **`pre-commit`** with security hooks (detect-secrets, IP detection)
- **GitHub Actions** CI/CD (quality, tests, docs deployment)
- Type checking via **`mypy`**, **`ty`**, or **`pyrefly`**
- Choice of **flat** or **src** project layout
- Optional **PyPI** publishing workflow
- Multi-OS CI support (Ubuntu, macOS, Windows)

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

## Documentation

Full documentation:
[communitiesuk.github.io/python-cookiecutter-uv](https://communitiesuk.github.io/python-cookiecutter-uv/)

## Development

```bash
make install       # Install environment
make test          # Run template tests
make bake          # Bake with defaults (for testing)
make docs          # Preview documentation
```
