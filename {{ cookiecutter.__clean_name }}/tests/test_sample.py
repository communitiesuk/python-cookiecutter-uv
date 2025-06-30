"""An example of a basic test file."""

from {{cookiecutter.__clean_slug}} import basic_calculation


class ExpectedEqualValueError(ValueError):
    """Custom error for non-equal value expectations."""

    def __init__(self) -> None:
        """Initialize the error with a standard message."""
        super().__init__("Expected equal value.")


def test_basic() -> None:
    """A basic test to ensure arithmetic works as expected."""
    expected_result = 2
    actual_result = basic_calculation()
    if actual_result != expected_result:
        raise ExpectedEqualValueError
