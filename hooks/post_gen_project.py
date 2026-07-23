"""Post-generation hook: remove files based on cookiecutter options."""

import shutil
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


def prune_files() -> None:
    """Remove files based on cookiecutter options."""
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


def display_summary() -> None:
    """Show next steps after project generation."""
    print("\n" + "=" * 60)
    print("Project generated successfully!")
    print("=" * 60)
    print(f"  Project: {{ cookiecutter.project_name }}")
    print(f"  Author:  {{ cookiecutter.author_name }} ({{ cookiecutter.author_email }})")
    print(f"  Path:    {PROJECT_DIRECTORY}")
    print(f"\nNext steps:")
    print(f"  cd {PROJECT_DIRECTORY.name}")
    print(f"  git init -b main")
    print(f"  make install")
    print(f"  git add .")
    print(f"  git commit -m 'Initial commit'")
    print("=" * 60)


if __name__ == "__main__":
    try:
        prune_files()
        display_summary()
    except Exception:
        print("\nProject generation failed. Check the error messages above.")
