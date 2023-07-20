import pytest

import my_solve

testdata = [
    ("USD", "30/06/2000", "28,07"),
    ("DKK", "30/06/2020", "10,5569")
]

@pytest.mark.parametrize("currency,date,expected_rate", testdata)

def test_some_date_ok(currency, date, expected_rate):
    res_tuple = my_solve.get_rate_by_date(currency, date)
    assert res_tuple[3] == expected_rate
