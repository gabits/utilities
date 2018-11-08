from collections import namedtuple


def map_data_into_arrays(text_input: str) -> namedtuple:
    """
    - Input format:
        `Something\t653\tInserted\t45\tHere`
    """
    text_input = text_input.split("\t")


def map_arrays_into_named_tuples():
    pass


def map_spreadsheet_data():
    """
    Maps a simple spreadsheet table into a named tuple according to the columns
    defined by the table header.
    """
    line_arrays = map_data_into_arrays()
    named_tuples = map_arrays_into_named_tuples(line_arrays)
    return named_tuples
