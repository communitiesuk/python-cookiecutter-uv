# Features

## What You Get

| Feature | Description |
|---------|-------------|
| uv | Fast Python package manager for dependencies and virtual environments |
| tox-uv | Multi-version Python testing (3.12, 3.13, 3.14) |
| mkdocs + Material | Documentation site deployed to GitHub Pages |
| ruff | Fast linting and formatting |
| deptry | Checks for obsolete or missing dependencies |
| pre-commit | Git hooks for code quality and security |
| GitHub Actions | CI pipeline with quality, test, and docs jobs |
| Type checking | Choice of mypy, ty, or pyrefly |
| PyPI publishing | Optional release-to-PyPI workflow |

## Configurable Options

| Option | Default | Description |
|--------|---------|-------------|
| `typechecker` | mypy | Type checker: mypy, ty, or pyrefly |
| `publish_to_pypi` | y | Include PyPI release workflow |
| `use_ubuntu` | y | Test on Ubuntu in CI |
| `use_macos` | y | Test on macOS in CI |
| `use_windows` | y | Test on Windows in CI |
| `include_changelog` | y | Include CHANGELOG.md |
| `license` | OGL-UK-3.0 | Project licence |

## Publishing to PyPI

When `publish_to_pypi` is set to `"y"`, the `on-release-main.yml` workflow publishes your package to PyPI whenever you create a new GitHub release.

### Set up for PyPI

Before you can publish, you need to add a `PYPI_TOKEN` secret to your GitHub repository:

1. Navigate to **Settings > Secrets and variables > Actions** and press **New repository secret**.
2. Name it `PYPI_TOKEN`.
3. In a new tab, go to your [PyPI Account settings](https://pypi.org/manage/account/) and select **Add API token**.
4. Copy the token and paste it into the **Value** field. Save.

### How to trigger a release

1. Navigate to your repository on GitHub.
2. Click **Releases** on the right, then **Draft a new release**.
3. Add a new tag in the form `X.Y.Z` (e.g. `0.1.0`).
4. Press **Publish release**.

The workflow will update the version in `pyproject.toml`, build the wheel, and publish to PyPI.

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
