from palindrome import is_palindrome, main
import pytest
from unittest.mock import patch

def test_is_palindrome():
    assert is_palindrome("level") == True
    assert is_palindrome("python") == False
    assert is_palindrome("radar") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("") == True  # an empty string is considered a palindrome

@patch('builtins.input', side_effect=['level'])
def test_main_palindrome_input(mock_input, capsys):
    main()
    captured = capsys.readouterr()
    assert "Es un palíndromo" in captured.out

@patch('builtins.input', side_effect=['python'])
def test_main_non_palindrome_input(mock_input, capsys):
    main()
    captured = capsys.readouterr()
    assert "No es un palíndromo" in captured.out