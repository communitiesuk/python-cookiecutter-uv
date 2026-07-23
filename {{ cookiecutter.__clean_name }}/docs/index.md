# {{cookiecutter.repository_name}}

{{cookiecutter.project_description}}

## Installation

```bash
pip install {{cookiecutter.__clean_slug}}
```

Or with uv:

```bash
uv add {{cookiecutter.__clean_slug}}
```

## Quick Start

```python
import {{cookiecutter.__clean_slug}}

print({{cookiecutter.__clean_slug}}.hello())
```

## Development

Clone the repository and install the development environment:

```bash
git clone https://github.com/{{cookiecutter.repository_home}}/{{cookiecutter.repository_name}}.git
cd {{cookiecutter.repository_name}}
make install
```

Run the test suite:

```bash
make test
```
