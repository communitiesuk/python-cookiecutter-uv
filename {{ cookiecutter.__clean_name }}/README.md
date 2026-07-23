# {{cookiecutter.repository_name}}

[![Build status](https://img.shields.io/github/actions/workflow/status/{{cookiecutter.repository_home}}/{{cookiecutter.repository_name}}/main.yml?branch=main)](https://github.com/{{cookiecutter.repository_home}}/{{cookiecutter.repository_name}}/actions/workflows/main.yml?query=branch%3Amain)
[![License](https://img.shields.io/github/license/{{cookiecutter.repository_home}}/{{cookiecutter.repository_name}})](https://github.com/{{cookiecutter.repository_home}}/{{cookiecutter.repository_name}}/blob/main/LICENCE)

{{cookiecutter.project_description}}

## Installation

```bash
pip install {{cookiecutter.__clean_slug}}
```

## Quick Start

```python
import {{cookiecutter.__clean_slug}}

print({{cookiecutter.__clean_slug}}.hello())
```

## Development

```bash
git clone https://github.com/{{cookiecutter.repository_home}}/{{cookiecutter.repository_name}}.git
cd {{cookiecutter.repository_name}}
make install
```

| Command | Description |
|---------|-------------|
| `make install` | Install environment and pre-commit hooks |
| `make check` | Run linting and type checking |
| `make test` | Run test suite |
| `make docs` | Serve documentation locally |
| `make build` | Build wheel |

## Documentation

Full documentation is available at [{{cookiecutter.repository_home}}.github.io/{{cookiecutter.repository_name}}](https://{{cookiecutter.repository_home}}.github.io/{{cookiecutter.repository_name}}).

---

Repository initiated with [communitiesuk/python-cookiecutter-uv](https://github.com/communitiesuk/python-cookiecutter-uv).
