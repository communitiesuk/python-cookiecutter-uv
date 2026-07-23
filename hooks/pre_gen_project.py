"""Pre-generation hook: validate inputs before creating the project."""

import re
import sys


def validate_project_name(name: str) -> None:
    """Ensure project name is a valid slug-like string."""
    if not re.match(r"^[a-z][a-z0-9-]*$", name):
        print(f"ERROR: '{name}' is not a valid project name.")
        print(
            "Project names must start with a lowercase letter and contain only lowercase letters, digits, and hyphens."
        )
        sys.exit(1)


if __name__ == "__main__":
    validate_project_name("{{ cookiecutter.project_name }}")
