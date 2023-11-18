import pytest
from highest_number import highest_number

def test_highest_number():
    assert highest_number(5, 3, 2) == 5
    assert highest_number(3, 5, 2) == 5
    assert highest_number(3, 2, 5) == 5
    assert highest_number(1.5, 1.5, 1.5) == "Todos los números son iguales, así que no hay ninguno más alto que 1.5."
    assert highest_number(-10, -5, -2) == -2
    assert highest_number(0, 0, 0) == "Todos los números son iguales, así que no hay ninguno más alto que 0."
    assert highest_number(3, 3, 5) == 5
    assert highest_number(5, 3, 5) == 5
    assert highest_number(5, 5, 3) == 5
    assert highest_number(3, 5, 5) == 5
    assert highest_number(1.2, 1.3, 1.33) == 1.33