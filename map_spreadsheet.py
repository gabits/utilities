from collections import namedtuple
from unittest import TestCase


def map_spreadsheet_data(text_input: str) -> namedtuple:
    """
    - Input format:
        `Something\t653\tInserted\t45\tHere`
    """
    text_input = text_input.split("\t")
    


class TestMapSpreadsheetData(TestCase):
    def test_tab_separated_unicode_text_returns_as_tuple(self):
        self.fail("TODO")

    def test_empty_string_does_not_return_data_if_map_is_provided(self):
        self.fail("TODO")

    def test_blank_string_returns_data_after_(self):
        self.fail("TODO")

