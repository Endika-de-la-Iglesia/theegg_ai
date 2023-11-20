from tiempo import tierra, marte, jupiter, get_segundos_caida
import pytest
from unittest.mock import patch

def test_tierra():
    assert tierra(2) == 19.6
    assert tierra(0) == 0

def test_marte():
    assert marte(2) == 7.4
    assert marte(0) == 0

def test_jupiter():
    assert jupiter(2) == 49.6
    assert jupiter(0) == 0

@patch('builtins.input', side_effect=['tierra', '2'])
def test_get_segundos_caida_tierra(mock_input):
    planet, time = get_segundos_caida()
    assert planet == 'Tierra'
    assert time == 2

@patch('builtins.input', side_effect=['MARTE', '3'])
def test_get_segundos_caida_marte(mock_input):
    planet, time = get_segundos_caida()
    assert planet == 'Marte'
    assert time == 3

@patch('builtins.input', side_effect=['JUPiter', '4'])
def test_get_segundos_caida_jupiter(mock_input):
    planet, time = get_segundos_caida()
    assert planet == 'Jupiter'
    assert time == 4