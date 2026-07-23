# Contributing to python-cookiecutter-uv

Contributions are welcome! Here's how to get started.

## Setup

1. Fork and clone the repository
2. Install the environment: `make install`
3. Create a feature branch: `git checkout -b my-feature`

## Development

- Run quality checks: `make check`
- Run tests: `make test`
- Bake a test project: `make bake`
- Preview docs: `make docs`

## Testing

Tests use `pytest-cookies` to bake the template with various option combinations and validate the
output. When adding a new cookiecutter option, add corresponding tests in
`tests/test_cookiecutter.py`.

## Pull Requests

1. Ensure all checks pass: `make check && make test`
2. Update documentation if you've changed template features
3. Submit a PR with a clear description of changes
