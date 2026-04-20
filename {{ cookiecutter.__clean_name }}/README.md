# {{ cookiecutter.project_name }}

---

## About this project

{{cookiecutter.project_description}}

This project uses:

- [`uv`](https://docs.astral.sh/uv/) for Python package and dependency management.
- [`pre-commit`](https://pre-commit.com/) ensuring code quality & consistency, prevent commits of sensitive information (e.g. secrets).
- [`ruff`](https://docs.astral.sh/ruff/) for linting and formatting.
- {% if cookiecutter.typechecker == 'ty' %}[`ty`](https://github.com/astral-sh/ty){% elif cookiecutter.typechecker == 'pyrefly' %}[`pyrefly`](https://pyrefly.org/){% else %}[`mypy`](https://www.mypy-lang.org/){%- endif %} for typechecking.
{% if cookiecutter.include_nox == 'y' %}
- [`nox`](https://nox.thea.codes/en/stable/) for automated code quality checks in multiple Python environments.
{%- endif %}
{% if cookiecutter.include_unit_testing == 'y' %}
- [`pytest`](https://docs.pytest.org/) for running unit tests).
{%- endif %}
- [GitHub Actions](https://github.com/features/actions) for CI workflows.

It also includes pull request and issue templates.

## Setup Dev Environment

Assumes you've installed `uv` & `pre-commit`.

We've included a `Makefile` for ease of use.

Install the `uv` virtual environment and `pre-commit` hooks:

```zsh
make install
```

For code linting and formatting:

```zsh
make check
```

_Note_: `pre-commit` will also run the linting and formatting when committing code.

## Github Repo Setup

Ensure you've made a GitHub repository named: `https://github.com/{{cookiecutter.repository_home}}/{{cookiecutter.repository_name}}`.

Then push your new project to the repository:

```bash
git init -b main
git add .
git commit -m "chore: init commit"
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.repository_name}}.git
git branch -M main
git push -u origin main
```

Run linting & formatting, pushes any changes:

```bash
make check
git add .
git commit -m 'chore: pre-commit formatting'
git push origin main
```

Add a new `develop` branch:

```bash
git checkout -b develop
git push -u origin develop
```

Refer to the [guidance document](https://github.com.mcas.ms/communitiesuk/python-cookiecutter-uv/blob/main/docs/unix.md#step-8-branch-protection-rules) for setting up branch protection rules.

{% if cookiecutter.include_unit_testing == "y" %}

## Unit testing

By default, we use `pytest`.

Assuming dependencies have been installed, the testing suite can be ran using:

```bash
make test
```

{% endif %}

## GitHub workflows

A GitHub Workflow is an automated process set up in a repository that runs jobs (e.g. code liniting/formatting, testing.) when certain events occur — such as a push, pull request, or on a schedule.

By default in `.github`, we have:

- `actions`: `setup-uv-env` to set up the `uv` environment
- `workflows`: `main.yml` to run all linting, formatting and testing.


## Specific OS & Python versions?

Default Python is set to >=3.12 and <3.14.

Workflows test across which operating system you specified in the `cookiecutter` set up, but it will test for Python 3.12 & 3.13.

If you want to test across specific operating systems and Python versions, amend the following:

- `~/.github/workflows/main.yml`: lines 13-14
{% if cookiecutter.include_nox == 'y' %}
- `~/noxfile.py`: line 14
{%- endif %}

---

Repository initiated with [communitiesuk/python-cookiecutter-uv](https://github.com/communitiesuk/python-cookiecutter-uv).
