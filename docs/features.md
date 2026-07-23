# Features

## What You Get

| Feature | Description |
|---------|-------------|
| uv | Fast Python package manager for dependencies and virtual environments |
| tox-uv | Multi-version Python testing (3.12, 3.13, 3.14) |
| mkdocs + Material | Documentation site deployed to GitHub Pages |
| ruff | Fast linting and formatting |
| pre-commit | Git hooks for code quality and security |
| GitHub Actions | CI pipeline with quality, test, and docs jobs |
| Type checking | Choice of mypy, ty, or pyrefly |
| Codecov | Optional code coverage integration |
| PyPI publishing | Optional release-to-PyPI workflow |

## Configurable Options

| Option | Default | Description |
|--------|---------|-------------|
| `typechecker` | mypy | Type checker: mypy, ty, or pyrefly |
| `codecov` | y | Include Codecov integration |
| `publish_to_pypi` | y | Include PyPI release workflow |
| `use_ubuntu` | y | Test on Ubuntu in CI |
| `use_macos` | y | Test on macOS in CI |
| `use_windows` | y | Test on Windows in CI |
| `include_changelog` | y | Include CHANGELOG.md |
| `license` | MIT | Project licence |

## Generated Project Structure

```
project-name/
├── project_slug/         # Your Python package
├── tests/                # pytest test suite
├── docs/                 # mkdocs documentation source
├── .github/              # CI workflows and templates
├── mkdocs.yml            # Documentation configuration
├── pyproject.toml        # Project metadata and tool config
├── tox.ini               # Multi-version test config
├── Makefile              # Development commands
└── .pre-commit-config.yaml
```
