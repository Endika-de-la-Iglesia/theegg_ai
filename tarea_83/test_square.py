from square import square, main
import pytest
from unittest.mock import patch

def test_square():
    assert square(5) == 25
    assert square(0) == 0
    assert square(-3) == 9

@patch('builtins.input', side_effect=['4'])
def test_main_with_valid_input(mock_input, capsys):
    main()
    captured = capsys.readouterr()
    assert "16" in captured.out

@patch('builtins.input', side_effect=['0'])
def test_main_with_zero_input(mock_input, capsys):
    main()
    captured = capsys.readouterr()
    assert "0" in captured.out

@patch('builtins.input', side_effect=['abc', '3'])
def test_main_with_invalid_then_valid_input(mock_input, capsys):
    main()
    captured = capsys.readouterr()
    assert "No es un número entero." in captured.out
    assert "9" in captured.out
