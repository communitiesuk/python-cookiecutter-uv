"""Sample tests for {{ cookiecutter.__clean_slug }}."""

from {{ cookiecutter.__clean_slug }} import hello


def test_hello() -> None:
    """Test the hello function returns expected greeting."""
    assert hello() == "Hello from {{ cookiecutter.__clean_slug }}!"
