from unittest.mock import patch

import black

from tests.util import (
    BlackBaseTestCase,
    fs,
    dump_to_stderr,
    read_data,
)


class TestSimpleFormatEX(BlackBaseTestCase):
    @patch("black.dump_to_file", dump_to_stderr)
    def test_indentation_2_spaces(self) -> None:
        self.check_file(
            "ex_indentation_2_spaces", black.Mode(indentation="  ", tab_width=2)
        )

    @patch("black.dump_to_file", dump_to_stderr)
    def test_indentation_tabs(self) -> None:
        self.check_file("ex_indentation_tabs", black.Mode(indentation="\t"))

    @patch("black.dump_to_file", dump_to_stderr)
    def test_keep_blank_lines_in_brackets(self) -> None:
        self.check_file(
            "ex_keep_blank_lines_in_brackets",
            black.Mode(keep_blank_lines_in_brackets=True),
        )

    @patch("black.dump_to_file", dump_to_stderr)
    def test_prefer_no_split_subscripts(self) -> None:
        self.check_file(
            "ex_prefer_no_split_subscripts",
            black.Mode(prefer_no_split_subscripts=True),
        )

    def check_file(self, filename: str, mode: black.Mode, *, data: bool = True) -> None:
        source, expected = read_data(filename, data=data)
        actual = fs(source, mode=mode)
        self.assertFormatEqual(expected, actual)
        black.assert_equivalent(source, actual)
        black.assert_stable(source, actual, mode)
