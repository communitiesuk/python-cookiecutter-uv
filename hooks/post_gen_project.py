"""Post-generation hook: remove files based on cookiecutter options."""

import shutil
from pathlib import Path

# ANSI colour codes
PURPLE = "\033[95m"
BLUE = "\033[94m"
CYAN = "\033[96m"
GREEN = "\033[92m"
ORANGE = "\033[93m"
RED = "\033[91m"
ENDC = "\033[0m"
BOLD = "\033[1m"

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


def apply_layout() -> None:
    """Move the package into src/ when the src layout is selected."""
    if "{{ cookiecutter.layout }}" != "src":
        return
    print(f"{BLUE} > Moving package into src/ (src layout selected){ENDC}")
    src_dir = PROJECT_DIRECTORY / "src"
    src_dir.mkdir()
    (PROJECT_DIRECTORY / "{{ cookiecutter.__clean_slug }}").rename(src_dir / "{{ cookiecutter.__clean_slug }}")


def prune_files() -> None:
    """Remove files based on cookiecutter options."""
    print(f"\n{PURPLE}--- Pruning files based on options ---{ENDC}")

    # PyPI publishing
    if "{{ cookiecutter.publish_to_pypi }}" != "y":
        print(f"{BLUE} > Removing PyPI release workflow (not selected){ENDC}")
        remove(".github/workflows/on-release-main.yml")

    # Changelog
    if "{{ cookiecutter.include_changelog }}" != "y":
        print(f"{BLUE} > Removing CHANGELOG.md (not selected){ENDC}")
        remove("CHANGELOG.md")

    # License: keep selected, remove others
    selected_licence = "{{ cookiecutter.license }}"
    print(f"{BLUE} > Setting licence to: {selected_licence}{ENDC}")
    for licence_name, licence_file in LICENCE_FILES.items():
        if licence_name == selected_licence:
            (PROJECT_DIRECTORY / licence_file).rename(PROJECT_DIRECTORY / "LICENCE")
        else:
            remove(licence_file)

    print(f"{GREEN}Pruning complete.{ENDC}")


def display_summary() -> None:
    """Show next steps after project generation."""
    print(f"\n{GREEN}{'=' * 60}{ENDC}")
    print(f"{GREEN}{BOLD}Project generated successfully!{ENDC}")
    print(f"{GREEN}{'=' * 60}{ENDC}")
    print(f"  {CYAN}Project:{ENDC} {{ cookiecutter.project_name }}")
    print(f"  {CYAN}Author:{ENDC}  {{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})")
    print(f"  {CYAN}Path:{ENDC}    {PROJECT_DIRECTORY}")
    print(f"\n{PURPLE}{BOLD}Next steps:{ENDC}")
    print(f"  {BLUE}cd {PROJECT_DIRECTORY.name}{ENDC}")
    print(f"  {BLUE}git init -b main{ENDC}")
    print(f"  {BLUE}make install{ENDC}")
    print(f"  {BLUE}git add .{ENDC}")
    print(f"  {BLUE}git commit -m 'Initial commit'{ENDC}")
    print(f"{GREEN}{'=' * 60}{ENDC}")


if __name__ == "__main__":
    try:
        apply_layout()
        prune_files()
        display_summary()
    except Exception:
        print(f"\n{RED}Project generation failed. Check the error messages above.{ENDC}")
