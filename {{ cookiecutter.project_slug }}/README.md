# {{ cookiecutter.project_name }}

---

## About this project

This project uses:

- [`uv`](https://docs.astral.sh/uv/) for Python package and dependency management.
- [`pre-commit`](https://pre-commit.com/) ensuring code quality & consistency, prevent commits of sensitive information (e.g. secrets).
- [`ruff`](https://docs.astral.sh/ruff/) for linting and formatting.
- [`mypy`](https://mypy.readthedocs.io/en/stable/#) for checking type hints.
- [`nox`](https://nox.thea.codes/en/stable/) for automated code quality checks in multiple Python environments.
- [`pytest`](https://docs.pytest.org/) for running unit tests (if selected when using the `cookiecutter` template).
- [GitHub Actions](https://github.com/features/actions) for CI workflows.

It also includes pull request and issue templates.

## Install

Default Python is set to `>=3.12` and `<3.14`. Make sure you have a relevant Python version.

Follow the `uv` and `pre-commit` [installation instructions](https://github.com/communitiesuk/python-cookiecutter-uv).

Install project dependencies with `uv`:

```bash
uv sync
uv lock --locked
```

Install `pre-commit` hooks:

```bash
uv run pre-commit install
```

## Linting & formatting

Using `uv` and `pre-commit`:

```bash
uv run pre-commit run -a
```

{% if cookiecutter.include_unit_testing == "y" %}

## Unit testing

By default, we use `pytest`.

Assuming dependencies have been installed, the testing suite can be ran using:

```bash
uv run pytest tests --cov --cov-config=pyproject.toml --cov-report=xml
```

{% endif %}

## GitHub workflows

A GitHub Workflow is an automated process set up in a repository that runs jobs (e.g. code liniting/formatting, testing.) when certain events occur — such as a push, pull request, or on a schedule.

By default in `.github`, we have:

- `actions`: `setup-poetry-env` to set up the poetry environment
- `linters`: `.mypy.ini` configuration file for `mypy` type checking.
- `workflows`: `main.yml` to run all linting, formatting and testing.

If you have not selected the `include_unit_testing` when creating the repo with `cookiecutter` then the testing suite will not be included.

## Specific OS & Python versions?

As default, workflows test across `ubuntu`, `macOS` and `windows` operating systems for Python versions `3.12` and `3.13`.

If you want to test across specific operating systems and Python versions, amend the following files:

- `~/.github/workflows/main.yml`: lines 13-14
- `~/noxfile.py`: line 14
