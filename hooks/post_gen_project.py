"""Run after cookiecutter to finish environment setup and remove excluded files."""

import shutil
import subprocess
from enum import StrEnum
from pathlib import Path


class Colors(StrEnum):
    """ANSI color codes for terminal output."""

    PURPLE = "\033[95m"
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    ORANGE = "\033[93m"
    RED = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


PROJECT_DIRECTORY = Path.cwd()


def run_command(command: list[str], description: str) -> None:
    """Run a command in the project directory and handle errors."""
    print(f"{Colors.BLUE}Running: {description}...{Colors.ENDC}")
    try:
        subprocess.run(command, check=True, cwd=PROJECT_DIRECTORY)
    except subprocess.CalledProcessError as e:
        print(
            f"{Colors.RED}Error during '{description}'. Command '{e.cmd}' returned non-zero exit status {e.returncode}.{Colors.ENDC}"
        )
        if e.stdout:
            print(f"--- STDOUT ---\n{e.stdout}")
        if e.stderr:
            print(f"--- STDERR ---\n{e.stderr}")
        raise
    except FileNotFoundError:
        print(
            f"{Colors.RED}Error: Command '{command[0]}' not found. Is it installed and in your PATH?{Colors.ENDC}"
        )
        raise


def setup_git() -> None:
    """Initialize a git repository and set up the initial commit."""
    print(f"\n{Colors.PURPLE}--- Setting up Git Repository ---{Colors.ENDC}")
    run_command(["git", "init", "-b", "main"], "Initializing Git repository")
    run_command(
        [
            "git",
            "remote",
            "add",
            "origin",
            "https://github.com/{{cookiecutter.repository_home}}/{{cookiecutter.repository_name}}.git",
        ],
        "Adding remote origin",
    )
    run_command(["git", "add", "."], "Staging all files for initial commit")
    run_command(["git", "commit", "-m", "Initial commit"], "Creating initial commit")
    print(f"{Colors.GREEN}Git repository initialized successfully.{Colors.ENDC}")


def setup_uv_environment_and_lock() -> None:
    """Set up the UV environment and create the lockfile."""
    print(
        f"\n{Colors.PURPLE}--- Setting up Python Environment and Lockfile ---{Colors.ENDC}"
    )
    run_command(["make", "install"], "Installing dependencies and pre-commit hooks")
    run_command(["uv", "lock"], "Creating uv.lock file")
    run_command(["make", "check"], "Running code checks")
    print(f"{Colors.GREEN}uv environment and lockfile setup complete.{Colors.ENDC}")


def finalize_repository_and_push() -> None:
    """Commits the lockfile and pushes main and develop branches."""
    print(
        f"\n{Colors.PURPLE}--- Finalizing Repository and Pushing to Remote ---{Colors.ENDC}"
    )
    run_command(["git", "add", "."], "Staging changes")
    run_command(["git", "commit", "-m", "feat: adding changes"], "Committing stages")
    run_command(
        ["git", "push", "-u", "origin", "main"], "Pushing main branch to origin"
    )
    run_command(["git", "checkout", "-b", "develop"], "Creating local develop branch")
    run_command(
        ["git", "push", "-u", "origin", "develop"], "Pushing develop branch to origin"
    )
    print(f"{Colors.GREEN}Main and develop branches pushed successfully.{Colors.ENDC}")


def remove(filepath: str) -> None:
    try:
        path = Path(filepath)
        if path.is_file():
            path.unlink()
        elif path.is_dir():
            shutil.rmtree(filepath)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"{Colors.ORANGE}Warning during remove ({filepath}): {e}{Colors.ENDC}")


def prune_unwanted_files() -> None:
    """Remove unwanted files and directories from the project."""
    print(f"\n{Colors.PURPLE}--- Pruning Unwanted Files ---{Colors.ENDC}")
    if "{{cookiecutter.include_unit_testing}}" != "y":
        remove("tests")
    if "{{cookiecutter.include_docs}}" != "y":
        remove("docs")
    if "{{cookiecutter.include_nox}}" != "y":
        remove("noxfile.py")
    if "{{cookiecutter.include_changelog}}" != "y":
        remove("CHANGELOG.md")
    remove(".github/linters")


def display_project_details() -> None:
    project_path = Path.cwd()
    print("\n\n###################################################################\n")
    print(f"{Colors.GREEN}Project Setup Complete!{Colors.ENDC}\n")
    print(f"Project Name: {Colors.CYAN}{{cookiecutter.project_name}}{Colors.ENDC}")
    print(
        f"Author: {Colors.CYAN}{{cookiecutter.author_name}} ({{cookiecutter.author_email}}){Colors.ENDC}"
    )
    print(f"Project Path: {Colors.CYAN}{project_path}{Colors.ENDC}")
    print(
        f"Git URL: {Colors.CYAN}https://github.com/{{cookiecutter.repository_home}}/{{cookiecutter.repository_name}}{Colors.ENDC}"
    )
    if "{{cookiecutter.include_docs}}" == "y":
        print(
            f"Documentation: {Colors.CYAN}https://{{cookiecutter.repository_home}}.github.io/{{cookiecutter.repository_name}}{Colors.ENDC}"
        )
    print(f"License: {Colors.CYAN}{{cookiecutter.license}}{Colors.ENDC}")
    print(
        f"Git Status: {Colors.CYAN}Repository initialized. You are on the 'develop' branch.{Colors.ENDC}"
    )
    print(f"uv setup: {Colors.CYAN}Complete{Colors.ENDC}")
    print(
        f"\n{Colors.PURPLE}--- Next steps ---{Colors.ENDC}\n"
    )
    print("  - Amend to your preferences")
    print("  - Setup branch protection rules")
    print("\n####################################################################\n")


if __name__ == "__main__":
    try:
        prune_unwanted_files()
        setup_git()
        setup_uv_environment_and_lock()
        finalize_repository_and_push()
        display_project_details()
    except Exception:
        print(
            f"\n{Colors.RED}The project setup failed. Please check the error messages above.{Colors.ENDC}"
        )
