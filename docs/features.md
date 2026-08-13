# Features

## What You Get

| Feature | Description |
|---------|-------------|
| uv | Fast Python package manager for dependencies and virtual environments |
| tox-uv | Multi-version Python testing across Python 3.12, 3.13, and 3.14 |
| mkdocs + Material | Documentation site deployed to GitHub Pages |
| ruff | Fast linting and formatting |
| deptry | Detects obsolete or missing dependencies |
| pre-commit | Git hooks for code quality, file checks, and security |
| GitHub Actions | CI pipeline with quality, test, and docs jobs |
| Type checking | Choice of mypy, ty, or pyrefly |
| Layout choice | Flat (package at root) or src (package under `src/`) layout |
| PyPI publishing | Optional release-to-PyPI workflow |
| PR and issue templates | GitHub templates for consistent pull requests and issue reporting |

## pre-commit Hooks

The generated project includes the following pre-commit hooks:

| Hook | Description |
|------|-------------|
| check-case-conflict | Prevents files that differ only by case |
| check-merge-conflict | Catches unresolved merge conflict markers |
| check-toml | Validates TOML files |
| check-yaml | Validates YAML files |
| check-json | Validates JSON files |
| end-of-file-fixer | Ensures files end with a newline |
| trailing-whitespace | Removes trailing whitespace |
| check-added-large-files | Blocks files larger than 5 MB from being committed |
| ruff-check | Lints Python code with ruff |
| ruff-format | Formats Python code with ruff |
| detect-secrets | Prevents accidental commit of secrets and credentials |
| detect-ip | Prevents accidental commit of IP addresses |

## Configurable Options

| Option | Default | Description |
|--------|---------|-------------|
| `layout` | flat | Package layout: flat (package at root) or src (package under `src/`) |
| `typechecker` | mypy | Type checker: mypy, ty, or pyrefly |
| `publish_to_pypi` | y | Include PyPI release workflow |
| `use_ubuntu` | y | Test on Ubuntu in CI |
| `use_macos` | y | Test on macOS in CI |
| `use_windows` | y | Test on Windows in CI |
| `include_changelog` | y | Include CHANGELOG.md |
| `license` | OGL-UK-3.0 | Project licence — see [Licence options](#licence-options) below |

## Licence Options

| Licence | Description |
|---------|-------------|
| OGL-UK-3.0 | [Open Government Licence v3.0](http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/) — Crown Copyright. Default for MHCLG / communitiesuk projects |
| MIT | Permissive open source licence |
| BSD | BSD 3-Clause permissive licence |
| ISC | Functionally equivalent to MIT, used by OpenBSD |
| MPL-2.0 | Mozilla Public License — weak copyleft |
| Apache-2.0 | Apache Software License — permissive with patent protection |
| GPL-3.0 | GNU General Public License — strong copyleft |

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
├── project_slug/              # Your Python package
├── tests/                     # pytest test suite
├── docs/                      # mkdocs documentation source
├── .github/
│   ├── actions/               # Composite action for env setup
│   ├── workflows/             # CI/CD workflows (main, docs, release)
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── ISSUES_TEMPLATE.md
├── mkdocs.yml                 # Documentation configuration
├── pyproject.toml             # Project metadata and tool config
├── tox.ini                    # Multi-version test config
├── Makefile                   # Development commands
├── .pre-commit-config.yaml    # Pre-commit hook configuration
└── LICENCE
```
