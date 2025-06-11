## Installation

Assumes you're using DAP.

### Step 1: Install `pipx`

Whereas `pip` is a general-purpose installer for libraries and apps with no environment isolation, [`pipx`](https://pipx.pypa.io/stable/) is made specifically for application installation as it adds isolation but still makes the apps available in your shell.

Open a command prompt and run:

```bash
python -m pip install --user pipx
```

Which should result in something similar to:

```bash
WARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH
```

Navigate to that specific directory ensure `pipx` is added the global environments:

```bash
cd <USER folder>\AppData\Roaming\Python\Python3x\Scripts
.\pipx.exe ensurepath
```

Close your command prompt and open a new one. Run the following to update `pipx` to the latest version:

```bash
python -m pip install --user --upgrade pipx
```

Verify it's been installed using:

```bash
pipx --version
```

### Step 2: Install `uv`, `cookiecutter` & `pre-commit`

In your command prompt, run the following:

```bash
pipx install uv
pipx install cookiecutter
pipx install pre-commit
```

Verify installations:

```bash
uv --version
cookiecutter --version
pre-commit --version
```

### Step 3: set global git

This is usuall already done, but you'll need your global git credentials set up before connecting to a repository.

You can check this by running the following in a command prompt:

```bash
git config --global user.name
git config --global user.email
```

If they don't return the expected information, run:

```bash
git config --global user.name "your-git-profile"
git config --global user.email "Joe.Bloggs@communities.gov.uk"
```

### Step 4: Set up your GitHub repository

Create an empty repository, for example in the [communitiesuk GitHub organisation](https://github.com/organizations/communitiesuk/repositories/new).

Give it a name that only contains alphanumeric characters and optionally `-` (e.g. `my-project`).

*DO NOT* check any boxes under the option `Initialize this repository with..`.

***Note***: you can also create a repository in your private user or a different organisation, just keep a reference for later.

### Step 5: Generate your project

On your local machine, navigate to the directory in which you want to create a project directory, and run the following command:

```bash
cookiecutter https://github.com/communitiesuk/python-cookiecutter-uv.git
```

Follow the onscreen prompts to set your project name which will be slugified for the repo name and package name within the repo.

Select whether you want to include unit testing in your project.

This should populate basic information in your `pyproject.toml`.

***Note***: we use a [flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/) by default.

### Step 6: Upload your project to GitHub

Close your command prompt.

Open a new VS Code window and select the newly created template folder.

Open a terminal and run the following commands:

```bash
git init -b main
git add .
git commit -m "chore: init commit"
git remote add origin https://github.com/<project-upstream>/<project_name>.git
git push -u origin main
```

- Replace `<project-upstream>` with your GitHub destination (e.g. `https://github.com/communitiesuk`, `https://github.com/your-user-profile`)
- Replace `<project-name>` with the name you gave to the GitHub repository

Install and run the `pre-commit` hooks:

```bash
uv run pre-commit install
uv run pre-commit run -a
```

Commit the changes:

```bash
git add .
git commit -m 'chore: pre-commit formatting'
git push origin main
```

Add a new `develop` branch:

```bash
git checkout -b develop
git push -u origin develop
```

### Step 7: Amend to your preferences

By default, the template provides CI/CD pipelines across multiple operating systems (`ubuntu`, `macOS`, `windows`) and Python versions (`3.12`, `3.13`).

When creating your repo and selected `n` to the prompt `include_unit_testing`, when you do not need to remove any unit testing.

If you want to test across specific operating systems and Python versions, amend the following files:

- `~/.github/workflows/main.yml`: lines 13-14
- `~/noxfile.py`: line 14

Ensure you commit any changes.

### Step 8: branch protection rules

By default, GitHub does not apply any branch protection policies to newly created repositories. We use policies to enforce best practice like:

- Pull requests into `main` been reviewed & approved
- Pull requests status checks must pass before being merged into `main`
- Default branch is `develop` as opposed to `main`

Open the `Settings` menu for your GitHub repository (your users needs the `Admin` role assigned to them):

![Settings](../images/settings.png)

Under the `Default branch` section, click on the `Switch to another branch` option and choose the newly created `develop`.

![Default branch](../images/rename_branch.png)

Go to the `Branches` section and click on the `Add branch rules` button:

![Add protection rules](../images/branch_rules.png)

Under the `Ruleset name`, set this to the relevant branch, e.g. `main`.

Go to the `Target branches` section:

![Branch Policy](../images/target_branches.png)

On the `Add target` dropdown, select the option `Include by pattern` and provide your branch name, e.g. `main`.

In the `Branch rules` section, select the following options:

- Restrict deletions
- Require a pull request before merging
  - Required approvals: 1
  - Require approval of the most recent reviewable push
  - Require conversation resolution before merging
- Block force pushes

Repeat the above steps for the `develop` branch.

On the `Add target` dropdown, select the option `Include by pattern` and provide your branch name, e.g. `main`.

In the `Branch rules` section, select the following options:

- Restrict deletions
- Require a pull request before merging
  - Required approvals: 1
  - Require approval of the most recent reviewable push
  - Require conversation resolution before merging
- Block force pushes

Repeat the above steps for the `develop` branch.
