from vowel import vowel_id

def test_vowel_id():
    assert vowel_id('a') == True
    assert vowel_id('e') == True
    assert vowel_id('i') == True
    assert vowel_id('o') == True
    assert vowel_id('u') == True

    assert vowel_id('b') == False
    assert vowel_id('c') == False
    assert vowel_id('d') == False
    assert vowel_id('f') == False
    assert vowel_id('g') == False