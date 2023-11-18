from list_sum import list_sum, main
import pytest
from unittest.mock import patch

def test_list_sum():
    assert list_sum(['1', '2', '3']) == 6.0
    assert list_sum(['5.5', '2.5', '1.0']) == 9.0
    assert list_sum(['10', '20', '30']) == 60.0
    assert list_sum(['abc', '2', '3']) == 5.0 
    assert list_sum([]) == 0.0

#Using patch to mock user input during the test
@patch('builtins.input', side_effect=['1', '2', '3', 'STOP'])
def test_main(mock_input):
    assert main() == 6.0