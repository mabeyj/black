import pytest

from black.mode import Mode


@pytest.mark.parametrize("indentation, expected", [("    ", False), ("\t", True)])
def test_use_tabs(indentation: str, expected: bool) -> None:
    result = Mode(indentation=indentation).use_tabs
    assert result == expected


def test_get_cache_key() -> None:
    result = Mode(
        indentation="\t",
        tab_width=4,
        keep_blank_lines_in_brackets=True,
    ).get_cache_key()
    expected = "-.1.4.88.1.0.0.1.0.1"
    assert result == expected
