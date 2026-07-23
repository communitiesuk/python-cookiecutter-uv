# Contributing to {{cookiecutter.repository_name}}

Contributions are welcome!

## Setup

1. Fork the repository
2. Clone your fork: `git clone git@github.com:YOUR_NAME/{{cookiecutter.repository_name}}.git`
3. Install the environment: `make install`
4. Create a branch: `git checkout -b my-feature`

## Development Workflow

1. Make your changes
2. Add tests for new functionality
3. Run checks: `make check`
4. Run tests: `make test`
5. Run tox for multi-version testing: `tox` (optional locally, runs in CI)
6. Commit and push
7. Submit a pull request

## Pull Request Guidelines

- Include tests for new functionality
- Update documentation if behaviour changes
- Ensure all CI checks pass
