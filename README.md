# UV Python Cookiecutter

Basic Python template using [`cookiecutter`](https://github.com/cookiecutter/cookiecutter) and [`uv`](https://docs.astral.sh/uv/).

Objective: make it simpler to set up new Python projects with commonly used developer tooling.

This *should* be platform agnostic and work in DAP.

There are step-by-step installation instructions for [macOS/Linux](https://github.com/communitiesuk/python-cookiecutter-uv/blob/main/docs/unix.md) and [Windows](https://github.com/communitiesuk/python-cookiecutter-uv/blob/main/docs/windows.md) machines.

If you have any issues *and/or* suggestions please contact <jordan.pinder@communities.gov.uk>.

---

## What's included?

- [`uv`](https://docs.astral.sh/uv/) for Python package and dependency management.
- [`pre-commit`](https://pre-commit.com/) ensuring code quality & consistency, prevent commits of sensitive information (e.g. secrets).
- [`ruff`](https://docs.astral.sh/ruff/) for linting and formatting.
- [`mypy`](https://mypy.readthedocs.io/en/stable/#) for checking type hints.
- [`nox`](https://nox.thea.codes/en/stable/) for automated code quality checks in multiple Python environments.
- [`pytest`](https://docs.pytest.org/) for running unit tests (if selected when using the `cookiecutter` template).
- [GitHub Actions](https://github.com/features/actions) for CI workflows.

It also includes pull request and issue templates.
