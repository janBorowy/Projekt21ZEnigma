from enigma import IncorrectAlphabetLetterError, IncorrectLetterPairError, IncorrectLetterPairListError, check_index, check_letter_pair, check_letter_pair_list, find_alphabet_index, check_letter, find_alphabet_letter, map_left_to_right, map_reflector, map_right_to_left
import pytest

#specyfikacje z modelu Enigma I (1930)
rotor_wiring_A = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor_wiring_B = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor_wiring_C = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

reflector_map = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

def test_check_letter_pair():
    check_letter_pair(("A", "B"))

    with pytest.raises(TypeError):
        check_letter_pair((1, 2))

    with pytest.raises(IncorrectLetterPairError):
        check_letter_pair(["A", "B"])

def test_check_letter_pair_list():
    check_letter_pair_list([("A", "B"), ("C", "D"), ("E", "F")])
    check_letter_pair_list([])

    with pytest.raises(TypeError):
        check_letter_pair_list((("A", "B"), ("C", "D"), ("E", "F")))

    with pytest.raises(IncorrectLetterPairListError):
        check_letter_pair_list([("A", "B"), ("A", "B"), ("E", "F")])

    with pytest.raises(IncorrectLetterPairListError):
        check_letter_pair_list((("A", "B"), ("B", "A"), ("E", "F")))


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
    assert map_right_to_left(rotor_wiring_A, "R", 3) == 9
    assert map_right_to_left(rotor_wiring_A, "W", 19) == 11
    assert map_right_to_left(rotor_wiring_A, "C", 25) == 8
    assert map_right_to_left(rotor_wiring_A, "K", 6) == 13
    assert map_right_to_left(rotor_wiring_A, "F", 14) == 10
    assert map_right_to_left(rotor_wiring_A, "M", 10) == 15
    assert map_right_to_left(rotor_wiring_B, "A", 19) == 13
    assert map_right_to_left(rotor_wiring_B, "M", 2) == 0
    assert map_right_to_left(rotor_wiring_B, "G", 14) == 9
    assert map_right_to_left(rotor_wiring_B, "N", 1) == 25

def test_map_left_to_right():
    assert map_left_to_right(rotor_wiring_A, "K", 13) == 6
    assert map_left_to_right(rotor_wiring_A, "U", 23) == 3
    assert map_left_to_right(rotor_wiring_A, "C", 7) == 23
    assert map_left_to_right(rotor_wiring_A, "M", 15) == 10
    assert map_left_to_right(rotor_wiring_A, "F", 10) == 14
    assert map_left_to_right(rotor_wiring_A, "K", 13) == 6
    assert map_left_to_right(rotor_wiring_B, "A", 13) == 19
    assert map_left_to_right(rotor_wiring_B, "M", 0) == 2
    assert map_left_to_right(rotor_wiring_B, "G", 9) == 14
    assert map_left_to_right(rotor_wiring_B, "N", 25) == 1

def test_map_reflector():
    assert map_reflector(reflector_map, 12) == 14
    assert map_reflector(reflector_map, 0) == 24
    assert map_reflector(reflector_map, 7) == 3
    assert map_reflector(reflector_map, 23) == 9
    assert map_reflector(reflector_map, 22) == 21