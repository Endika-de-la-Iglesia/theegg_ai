import pytest
from sentence_lenght import sentence_lenght

def test_sentence_lenght():
    assert sentence_lenght("Hola") == len("Hola")
    assert sentence_lenght("Hola") == len("Hola")
    assert sentence_lenght("Hola, ¿qué tal estás?") == len("Hola, ¿qué tal estás?")
    assert sentence_lenght("Hol") == len("Hol")
    assert sentence_lenght("") == len("")