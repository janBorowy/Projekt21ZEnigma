from enigma import IncorrectAlphabetLetterError, check_index, find_alphabet_index, check_letter, find_alphabet_letter, map_left_to_right, map_right_to_left
import pytest

def test_check_index():
    check_index(5)

    with pytest.raises(TypeError):
        check_index("A")
        check_index(0.1)
        check_index((1, None))

    with pytest.raises(ValueError):
        check_index(27)
        check_index(-1)

def test_check_letter():
    check_letter("A")

    with pytest.raises(TypeError):
        check_letter(1)
        check_letter(0.1)
        check_letter(("A", None))

    with pytest.raises(ValueError):
        check_letter("AB")
        check_letter("ABCD")

def test_find_alphabet_index():
    assert find_alphabet_index("A") == 0
    assert find_alphabet_index("B") == 1
    assert find_alphabet_index("Z") == 25
    assert find_alphabet_index("J") == 9
    
    with pytest.raises(IncorrectAlphabetLetterError):
        find_alphabet_index("Ó")

def test_find_alphabet_letter():
    assert find_alphabet_letter(0) == "A"
    assert find_alphabet_letter(1) == "B"
    assert find_alphabet_letter(25) == "Z"
    assert find_alphabet_letter(9) == "J"

def test_map_right_to_left():
    rotor_wiring_A = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    assert map_right_to_left(rotor_wiring_A, "A", 0) == 4
    assert map_right_to_left(rotor_wiring_A, "B", 0) == 10

def test_map_left_to_right():
    rotor_wiring_A = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    assert map_left_to_right(rotor_wiring_A, "A", 4) == 0
    assert map_left_to_right(rotor_wiring_A, "B", 10) == 0
    assert map_left_to_right(rotor_wiring_A, "F", 10) == 14