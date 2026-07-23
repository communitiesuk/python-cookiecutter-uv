# Tutorial

This page contains a complete tutorial on how to create your project.

## Step 1: Install uv

To start, we will need to install `uv`. The instructions to install uv can be found
[here](https://docs.astral.sh/uv/#getting-started). For macOS or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Step 2: Generate your project

On your local machine, navigate to the directory in which you want to
create a project directory, and run the following command:

```bash
uvx cookiecutter gh:communitiesuk/python-cookiecutter-uv
```

Follow the prompts to configure your project. For an explanation of the prompt arguments, see [Features](features.md#configurable-options).

## Step 3: Set up your GitHub repository

Create an empty [new repository](https://github.com/new) on GitHub. Give
it a name that only contains alphanumeric characters and optionally `-`.
**DO NOT** check any boxes under the option `Initialize this repository with`.

## Step 4: Upload your project to GitHub

Navigate into your newly created project directory and run:

```bash
cd <project-name>
git init -b main
git add .
git commit -m "Initial commit"
git remote add origin git@github.com:<repository_home>/<project-name>.git
git push -u origin main
```

## Step 5: Set up your development environment

The CI/CD pipeline will initially fail because the project does not yet contain a `uv.lock` file. To fix that, install the environment and pre-commit hooks:

```bash
make install
```

This will generate the `uv.lock` file and install the pre-commit hooks.

## Step 6: Run the pre-commit hooks

To resolve any formatting issues from the template, run the pre-commit hooks:

```bash
uv run pre-commit run -a
```

## Step 7: Commit and push the changes

```bash
git add .
git commit -m "chore: add lockfile and fix formatting"
git push origin main
```

## Step 8: Configure repository secrets (PyPI)

If you enabled `publish_to_pypi`, you need to set up a PyPI API token so the release workflow can publish your package.

1. Go to your [PyPI Account settings](https://pypi.org/manage/account/) and select **Add API token**.
2. Copy the token.
3. In your GitHub repository, navigate to **Settings > Secrets and variables > Actions** and press **New repository secret**.
4. Name it `PYPI_TOKEN` and paste the token value.

The `on-release-main.yml` workflow will now automatically publish to PyPI whenever you create a new GitHub release.

## Step 9: Enable GitHub Pages for documentation

1. Navigate to **Settings > Actions > General** in your repository.
2. Under **Workflow permissions**, select **Read and write permissions**.
3. Navigate to **Settings > Pages**.
4. Under **Build and deployment > Source**, select **GitHub Actions**.

The `docs.yml` workflow will now deploy your documentation on every push to `main`.

## Step 10: Create a develop branch

```bash
git checkout -b develop
git push -u origin develop
```

Set up branch protection rules on `main` if desired.

## Step 11: Create your first release

To trigger a release (and publish to PyPI if enabled):

1. Navigate to your repository on GitHub.
2. Click **Releases** on the right, then **Draft a new release**.
3. Add a new tag in the form `X.Y.Z` (e.g. `0.1.0`).
4. Press **Publish release**.

This will trigger the release workflow which updates the version in `pyproject.toml`, builds the wheel, and publishes to PyPI.

## Step 12: You're all set!

Your documentation should now be live at `https://<repository_home>.github.io/<project-name>/`.

Available commands for daily development:

```bash
make install    # Re-sync environment
make check      # Lint, type check, and deptry
make test       # Run tests
make docs       # Preview docs locally
make build      # Build wheel
```
