from collections import namedtuple


def map_data_into_arrays(text_input: str) -> namedtuple:
    """
    - Input format:
        `Something\t653\tInserted\t45\tHere`
    """
    rows = text_input.split("\n")
    headers_array = rows[0].split("\t")
    rows_array = []
    for row in rows[1:]:
        rows_array += [row.split("\t")]

    if not len(rows_array) == len(rows):
        print("The number of rows mapped does not match the amount expected")

    return headers_array, rows_array

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

headers = headers_array.split("\t")
tuple_fields = f'{col_name} ' for col_name in headers
namedtuple('Row', tuple_fields)
