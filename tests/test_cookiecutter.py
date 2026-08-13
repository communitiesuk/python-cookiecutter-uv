"""Tests for the cookiecutter template output."""

from __future__ import annotations

import zipfile


def test_bake_project(bake):
    """Test that the template bakes successfully with defaults."""
    project = bake(project_name="my-project")
    assert project.path.name == "my-project"
    assert project.path.is_dir()


def test_pyproject_is_valid_toml(bake):
    """Test that pyproject.toml is valid TOML."""
    project = bake(project_name="test-proj")
    assert project.is_valid_toml("pyproject.toml")


def test_mkdocs_yml_is_valid(bake):
    """Test that mkdocs.yml is valid YAML."""
    project = bake(project_name="test-proj")
    assert project.is_valid_yaml("mkdocs.yml")


def test_main_workflow_is_valid(bake):
    """Test that main.yml is valid YAML."""
    project = bake(project_name="test-proj")
    assert project.is_valid_yaml(".github/workflows/main.yml")


def test_docs_workflow_is_valid(bake):
    """Test that docs.yml is valid YAML."""
    project = bake(project_name="test-proj")
    assert project.is_valid_yaml(".github/workflows/docs.yml")


def test_has_tox_ini(bake):
    """Test that tox.ini exists."""
    project = bake(project_name="test-proj")
    assert project.has_file("tox.ini")
    assert project.file_contains("tox.ini", "[tox]")


def test_has_mkdocs(bake):
    """Test that mkdocs documentation exists."""
    project = bake(project_name="test-proj")
    assert project.has_file("mkdocs.yml")
    assert project.has_dir("docs")
    assert project.has_file("docs/index.md")
    assert project.has_file("docs/modules.md")


def test_has_tests(bake):
    """Test that test directory and sample test exist."""
    project = bake(project_name="test-proj")
    assert project.has_dir("tests")
    assert project.has_file("tests/test_sample.py")


def test_makefile_has_docs_targets(bake):
    """Test that Makefile contains docs targets."""
    project = bake(project_name="test-proj")
    assert project.file_contains("Makefile", "docs:")
    assert project.file_contains("Makefile", "docs-test:")


def test_typechecker_mypy(bake):
    """Test mypy configuration."""
    project = bake(project_name="test-proj", typechecker="mypy")
    assert project.file_contains("pyproject.toml", "[tool.mypy]")
    assert project.file_contains("Makefile", "mypy")


def test_typechecker_ty(bake):
    """Test ty configuration."""
    project = bake(project_name="test-proj", typechecker="ty")
    assert project.file_contains("pyproject.toml", "[tool.ty]")
    assert project.file_contains("Makefile", "ty check")


def test_typechecker_pyrefly(bake):
    """Test pyrefly configuration."""
    project = bake(project_name="test-proj", typechecker="pyrefly")
    assert project.file_contains("pyproject.toml", "[tool.pyrefly]")
    assert project.file_contains("Makefile", "pyrefly check")


def test_publish_to_pypi_enabled(bake):
    """Test that PyPI workflow exists when publishing enabled."""
    project = bake(project_name="test-proj", publish_to_pypi="y")
    assert project.has_file(".github/workflows/on-release-main.yml")
    assert project.file_contains(".github/workflows/on-release-main.yml", "PYPI_TOKEN")


def test_publish_to_pypi_disabled(bake):
    """Test that PyPI workflow is removed when publishing disabled.

    The post-gen hook removes on-release-main.yml entirely when publish_to_pypi='n'.
    """
    project = bake(project_name="test-proj", publish_to_pypi="n")
    assert not project.has_file(".github/workflows/on-release-main.yml")


def test_changelog_enabled(bake):
    """Test that changelog exists when enabled."""
    project = bake(project_name="test-proj", include_changelog="y")
    assert project.has_file("CHANGELOG.md")


def test_changelog_disabled(bake):
    """Test that changelog is absent when disabled."""
    project = bake(project_name="test-proj", include_changelog="n")
    assert not project.has_file("CHANGELOG.md")


def test_license_mit(bake):
    """Test MIT license selection.

    The post-gen hook renames the selected licence file to LICENCE.
    """
    project = bake(project_name="test-proj", license="MIT license")
    assert project.has_file("LICENCE")
    assert project.file_contains("LICENCE", "MIT License")


def test_license_bsd(bake):
    """Test BSD license selection."""
    project = bake(project_name="test-proj", license="BSD license")
    assert project.has_file("LICENCE")
    assert project.file_contains("LICENCE", "Redistribution")


def test_license_apache(bake):
    """Test Apache license selection."""
    project = bake(project_name="test-proj", license="Apache-2.0")
    assert project.has_file("LICENCE")
    assert project.file_contains("LICENCE", "Apache License")


def test_no_extra_licence_files(bake):
    """Test that only the selected licence file remains (others are removed)."""
    project = bake(project_name="test-proj", license="MIT license")
    for leftover in ("LICENCE_MIT", "LICENCE_BSD", "LICENCE_ISC", "LICENCE_MPL", "LICENCE_APACHE", "LICENCE_GPL"):
        assert not project.has_file(leftover), f"Unexpected licence file present: {leftover}"


def test_pre_commit_has_security_hooks(bake):
    """Test that security hooks are present."""
    project = bake(project_name="test-proj")
    assert project.file_contains(".pre-commit-config.yaml", "detect-secrets")
    assert project.file_contains(".pre-commit-config.yaml", "detect-ip")


def test_flat_layout_default(bake):
    """Test that the default layout keeps the package at the project root."""
    project = bake(project_name="test-proj")
    assert project.has_file("test_proj/__init__.py")
    assert not project.has_dir("src")
    assert project.file_contains("pyproject.toml", 'packages = ["test_proj"]')


def test_src_layout(bake):
    """Test that layout='src' places the package under src/ and updates tool paths."""
    project = bake(project_name="test-proj", layout="src")
    assert project.has_file("src/test_proj/__init__.py")
    assert not project.has_dir("test_proj")
    assert project.file_contains("pyproject.toml", 'packages = ["src/test_proj"]')
    assert project.file_contains("pyproject.toml", 'files = ["src/test_proj"]')
    assert project.file_contains("mkdocs.yml", 'paths: ["src"]')


def test_src_layout_project_runs(bake):
    """Functional smoke test: a src-layout project installs, passes tests, and builds a correct wheel."""
    project = bake(project_name="test-proj", layout="src")

    sync = project.run("uv sync")
    assert sync.returncode == 0, f"uv sync failed:\n{sync.stderr}"

    tests = project.run("uv run python -m pytest tests")
    assert tests.returncode == 0, f"pytest failed:\n{tests.stdout}\n{tests.stderr}"

    build = project.run("uv build --wheel")
    assert build.returncode == 0, f"uv build failed:\n{build.stderr}"

    wheels = list((project.path / "dist").glob("*.whl"))
    assert len(wheels) == 1, f"expected exactly one wheel, found: {wheels}"
    with zipfile.ZipFile(wheels[0]) as wheel:
        assert "test_proj/__init__.py" in wheel.namelist(), f"wheel does not contain the package: {wheel.namelist()}"
