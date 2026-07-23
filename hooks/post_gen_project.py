"""Post-generation hook: remove files based on options, set up git and uv."""

import shutil
import subprocess
from pathlib import Path


PROJECT_DIRECTORY = Path.cwd()

LICENCE_FILES = {
    "OGL-UK-3.0": "LICENCE_OGL",
    "MIT license": "LICENCE_MIT",
    "BSD license": "LICENCE_BSD",
    "ISC license": "LICENCE_ISC",
    "MPL-2.0": "LICENCE_MPL",
    "Apache-2.0": "LICENCE_APACHE",
    "GPL-3.0": "LICENCE_GPL",
}


def remove(filepath: str) -> None:
    """Remove a file or directory, ignoring if it doesn't exist."""
    path = PROJECT_DIRECTORY / filepath
    if path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def run_command(command: list[str], description: str) -> None:
    """Run a command in the project directory."""
    print(f"  > {description}...")
    try:
        subprocess.run(command, check=True, cwd=PROJECT_DIRECTORY, capture_output=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"  ERROR: {description} failed (exit {e.returncode})")
        if e.stderr:
            print(f"  {e.stderr.strip()}")
        raise


def prune_files() -> None:
    """Remove files based on cookiecutter options."""
    # Codecov
    if "{{ cookiecutter.codecov }}" != "y":
        remove("codecov.yaml")

    # PyPI publishing
    if "{{ cookiecutter.publish_to_pypi }}" != "y":
        remove(".github/workflows/on-release-main.yml")

    # Changelog
    if "{{ cookiecutter.include_changelog }}" != "y":
        remove("CHANGELOG.md")

    # License: keep selected, remove others
    selected_licence = "{{ cookiecutter.license }}"
    for licence_name, licence_file in LICENCE_FILES.items():
        if licence_name == selected_licence:
            (PROJECT_DIRECTORY / licence_file).rename(PROJECT_DIRECTORY / "LICENCE")
        else:
            remove(licence_file)


def setup_git() -> None:
    """Initialize git repository."""
    print("\n--- Setting up Git Repository ---")
    run_command(["git", "init", "-b", "main"], "Initializing Git repository")
    run_command(
        ["git", "remote", "add", "origin",
         "https://github.com/{{ cookiecutter.repository_home }}/{{ cookiecutter.repository_name }}.git"],
        "Adding remote origin",
    )
    run_command(["git", "add", "."], "Staging all files")
    run_command(["git", "commit", "-m", "Initial commit"], "Creating initial commit")


def setup_environment() -> None:
    """Install dependencies and create lockfile."""
    print("\n--- Setting up Environment ---")
    run_command(["make", "install"], "Installing dependencies and pre-commit hooks")


def finalize_and_push() -> None:
    """Commit lockfile and push branches."""
    print("\n--- Pushing to Remote ---")
    run_command(["git", "add", "."], "Staging lockfile and generated files")
    run_command(["git", "commit", "-m", "feat: add lockfile and pre-commit config"], "Committing")
    run_command(["git", "push", "-u", "origin", "main"], "Pushing main branch")
    run_command(["git", "checkout", "-b", "develop"], "Creating develop branch")
    run_command(["git", "push", "-u", "origin", "develop"], "Pushing develop branch")


def display_summary() -> None:
    """Show project summary."""
    print("\n" + "=" * 60)
    print("Project Setup Complete!")
    print("=" * 60)
    print(f"  Project: {{ cookiecutter.project_name }}")
    print(f"  Author:  {{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})")
    print(f"  Path:    {PROJECT_DIRECTORY}")
    print(f"  Repo:    https://github.com/{{ cookiecutter.repository_home }}/{{ cookiecutter.repository_name }}")
    print(f"  Docs:    https://{{ cookiecutter.repository_home }}.github.io/{{ cookiecutter.repository_name }}")
    print(f"  Branch:  develop (active)")
    print("=" * 60)


if __name__ == "__main__":
    try:
        prune_files()
        setup_git()
        setup_environment()
        finalize_and_push()
        display_summary()
    except Exception:
        print("\nProject setup failed. Check the error messages above.")
