"""Pytest configuration and fixtures for cookiecutter template tests."""

from __future__ import annotations

import os
import subprocess
from dataclasses import dataclass, field
from pathlib import Path

import pytest
import yaml

try:
    import tomllib
except ImportError:
    import tomli as tomllib  # type: ignore[no-redef]


@dataclass
class BakedProject:
    """Wrapper around a baked cookiecutter project with convenience methods."""

    project_path: Path
    exit_code: int
    exception: Exception | None
    options: dict[str, str] = field(default_factory=dict)

    @property
    def path(self) -> Path:
        return self.project_path

    def has_file(self, rel_path: str) -> bool:
        return (self.path / rel_path).is_file()

    def has_dir(self, rel_path: str) -> bool:
        return (self.path / rel_path).is_dir()

    def read_file(self, rel_path: str) -> str:
        return (self.path / rel_path).read_text()

    def file_contains(self, rel_path: str, text: str) -> bool:
        return text in self.read_file(rel_path)

    def is_valid_yaml(self, rel_path: str) -> bool:
        path = self.path / rel_path
        if not path.is_file():
            return False
        try:
            with path.open() as f:
                yaml.safe_load(f)
        except (yaml.YAMLError, OSError):
            return False
        return True

    def is_valid_toml(self, rel_path: str) -> bool:
        path = self.path / rel_path
        if not path.is_file():
            return False
        try:
            with path.open("rb") as f:
                tomllib.load(f)
        except Exception:
            return False
        return True

    def run(self, command: str, check: bool = False) -> subprocess.CompletedProcess:
        import shlex

        env = {k: v for k, v in os.environ.items() if k != "VIRTUAL_ENV"}
        return subprocess.run(
            shlex.split(command),
            cwd=self.path,
            capture_output=True,
            text=True,
            check=check,
            env=env,
        )


@pytest.fixture
def bake(cookies):
    """Fixture factory that bakes a cookiecutter project and returns a BakedProject."""

    def _bake(**options) -> BakedProject:
        result = cookies.bake(extra_context=options)
        project = BakedProject(
            project_path=result.project_path,
            exit_code=result.exit_code,
            exception=result.exception,
            options=options,
        )
        assert project.exit_code == 0, f"Bake failed with options {options}: {project.exception}"
        assert project.exception is None
        return project

    return _bake
