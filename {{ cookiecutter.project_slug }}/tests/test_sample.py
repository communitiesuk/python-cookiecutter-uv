class ExpectedPositiveValueError(ValueError):
    def __init__(self) -> None:
        super().__init__("Expected positive value.")


def test_basic() -> None:
    if 1 + 1 != 2:
        raise ExpectedPositiveValueError()
