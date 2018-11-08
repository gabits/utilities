from .mapping import map_spreadsheet_data


def test_tab_separated_unicode_text_returns_as_tuple(self):
    input_sample = (
        "r1c1\tr1c2\tr1c3\tr1c4"
        "\nr2c1\tr2c2\tr2c3\tr2c4"
    )
    # Test that the first line is ignored
    result = map_spreadsheet_data(input_sample)

    assert type(result) == namedtuple
    assert result == expected_result


def test_empty_string_does_not_return_data_if_map_is_provided(self):
    assert False

def test_blank_string_returns_data_after_(self):
    assert False


if __name__ == '__main__':
    available_functions = dir(__file__)
    tests = [exec(f'{func}()') for func in available_functions if 'test' in func]
    print(tests)
