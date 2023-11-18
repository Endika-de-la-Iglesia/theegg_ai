from list_comparison import get_lists, list_comparison, main
import pytest
from unittest.mock import patch

def test_list_comparison():
    assert list_comparison([1, 2, 3], [3, 4, 5]) == (True, [3])
    assert list_comparison(['a', 'b', 'c'], ['c', 'd', 'e']) == (True, ['c'])
    assert list_comparison([], ['x', 'y', 'z']) == (False, [])
    assert list_comparison(['apple', 'orange'], []) == (False, [])
    assert list_comparison(['apple', 'orange'], ['orange', 'apple']) == (True, ['apple', 'orange'])

# Using patch to mock user input during the test
@patch('builtins.input', side_effect=['1', '2', '3', 'STOP', '3', '4', '5', 'STOP'])
def test_main_with_similarities(mock_input, capsys):
    main()
    captured = capsys.readouterr()
    assert "Hay valores coincidentes: ['3']" in captured.out

@patch('builtins.input', side_effect=['1', '2', '3', 'STOP', '4', '5', '6', 'STOP'])
def test_main_without_similarities(mock_input, capsys):
    main()
    captured = capsys.readouterr()
    assert "No hay valores coincidentes" in captured.out