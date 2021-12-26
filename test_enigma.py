from enigma_cipher import IncorrectEnigmaLetterError,\
    IncorrectLetterPairError, IncorrectLetterPairListError,\
    InvalidWiringError, check_cipher_string, check_index,\
    check_letter_pair, check_letter_pair_list,\
    check_wiring, cipher_character, cipher_string, create_plugboard_visual,\
    find_alphabet_index, check_letter, find_alphabet_letter,\
    map_left_to_right, map_plugboard, map_reflector, map_right_to_left
from enigma_classes import Rotor, Config
import enigma_io
import pytest

# specyfikacje z modelu Enigma I (1930)
rotor_wiring_A = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotor_wiring_B = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotor_wiring_C = "BDFHJLCPRTXVZNYEIWGAKMUSQO"

reflector_map = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

rotor_A = Rotor(rotor_wiring_A, "Q")
rotor_B = Rotor(rotor_wiring_B, "E")
rotor_C = Rotor(rotor_wiring_C, "V")

plugs = [("A", "Z"), ("C", "F"), ("P", "B"), ("K", "E"), ("U", "G"),
         ("W", "N"), ("X", "Y")]

config = Config([rotor_A, rotor_B, rotor_C], plugs, reflector_map)


def test_check_letter_pair():
    check_letter_pair(("A", "B"))

    with pytest.raises(IncorrectEnigmaLetterError):
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
        check_letter_pair_list([("A", "B"), ("B", "A"), ("E", "F")])


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

    with pytest.raises(IncorrectEnigmaLetterError):
        check_letter(1)
        check_letter(0.1)
        check_letter(("A", None))

    with pytest.raises(IncorrectEnigmaLetterError):
        check_letter("AB")
        check_letter("ABCD")


def test_check_wiring():
    check_wiring("EKMFLGDQVZNTOWYHXUSPAIBRCJ")

    with pytest.raises(InvalidWiringError):
        check_wiring("EKMFLGDDVZNTOWYHXUSPAIBRCJ")  # double D

    with pytest.raises(IncorrectEnigmaLetterError):
        check_wiring("EKMFLGDQvZNTOWYHXUSpAIBRCJ")  # small case v and p

    with pytest.raises(InvalidWiringError):
        check_wiring("EKTOWYHXUSpAIBRCJ")

    with pytest.raises(InvalidWiringError):
        check_wiring("")

    with pytest.raises(InvalidWiringError):
        check_wiring("EKMFLGDQVZNTOWYHXUSPAIBRCJŹ")


def test_check_cipher_string():
    check_cipher_string("HELLO")

    with pytest.raises(TypeError):
        check_cipher_string(110)

    with pytest.raises(IncorrectEnigmaLetterError):
        check_cipher_string(" HELLO ")

    with pytest.raises(IncorrectEnigmaLetterError):
        check_cipher_string("HELLO!")

    with pytest.raises(IncorrectEnigmaLetterError):
        check_cipher_string("HELLO.")

    with pytest.raises(IncorrectEnigmaLetterError):
        check_cipher_string("HELLÓ")


def test_find_alphabet_index():
    assert find_alphabet_index("A") == 0
    assert find_alphabet_index("B") == 1
    assert find_alphabet_index("Z") == 25
    assert find_alphabet_index("J") == 9

    with pytest.raises(IncorrectEnigmaLetterError):
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


def test_map_plugboard():
    plugs = ([("A", "Z"), ("C", "F"), ("P", "B"), ("K", "E"), ("U", "G"),
              ("W", "N"), ("X", "Y")])

    assert map_plugboard(plugs, 0) == 25
    assert map_plugboard(plugs, 2) == 5
    assert map_plugboard(plugs, 15) == 1
    assert map_plugboard(plugs, 10) == 4
    assert map_plugboard(plugs, 20) == 6
    assert map_plugboard(plugs, 22) == 13
    assert map_plugboard(plugs, 23) == 24

    assert map_plugboard(plugs, 25) == 0
    assert map_plugboard(plugs, 5) == 2
    assert map_plugboard(plugs, 1) == 15
    assert map_plugboard(plugs, 4) == 10
    assert map_plugboard(plugs, 6) == 20
    assert map_plugboard(plugs, 13) == 22
    assert map_plugboard(plugs, 24) == 23

    assert map_plugboard(plugs, 16) == 16
    assert map_plugboard(plugs, 12) == 12


def test_cipher_character():
    rotor_A.top_letter = "A"
    rotor_B.top_letter = "A"
    rotor_C.top_letter = "A"

    assert cipher_character(config, "A") == "X"

    rotor_A.top_letter = "L"
    rotor_B.top_letter = "P"
    rotor_C.top_letter = "R"

    assert cipher_character(config, "F") == "P"

    rotor_A.top_letter = "W"
    rotor_B.top_letter = "Z"
    rotor_C.top_letter = "W"

    assert cipher_character(config, "O") == "L"


def test_rotor_step():
    rotor_A.top_letter = "A"
    rotor_B.top_letter = "A"
    rotor_C.top_letter = "A"

    assert rotor_A.top_letter == "A"
    rotor_A.step()
    assert rotor_A.top_letter == "B"
    rotor_A.top_letter = "W"
    rotor_A.step()
    assert rotor_A.top_letter == "X"


def test_config_step():
    rotor_A.top_letter = "A"
    rotor_B.top_letter = "A"
    rotor_C.top_letter = "A"

    config.step()
    assert rotor_A.top_letter == "B"
    assert rotor_B.top_letter == "A"
    assert rotor_C.top_letter == "A"
    config.step()
    assert rotor_A.top_letter == "C"
    assert rotor_B.top_letter == "A"
    assert rotor_C.top_letter == "A"

    rotor_A.top_letter = "Q"
    config.step()
    assert rotor_A.top_letter == "R"
    assert rotor_B.top_letter == "B"
    assert rotor_C.top_letter == "A"
    config.step()
    assert rotor_A.top_letter == "S"
    assert rotor_B.top_letter == "B"
    assert rotor_C.top_letter == "A"

    rotor_A.top_letter = "Q"
    rotor_B.top_letter = "E"
    rotor_C.top_letter = "V"
    config.step()
    assert rotor_A.top_letter == "R"
    assert rotor_B.top_letter == "F"
    assert rotor_C.top_letter == "W"

    rotor_A.top_letter = "O"
    rotor_B.top_letter = "E"
    rotor_C.top_letter = "F"
    config.step()
    assert rotor_A.top_letter == "P"
    assert rotor_B.top_letter == "F"
    assert rotor_C.top_letter == "G"


def test_cipher_string():
    rotor_A.top_letter = "A"
    rotor_B.top_letter = "A"
    rotor_C.top_letter = "A"

    assert cipher_string(config, "HELLO") == "MJWFA"
    assert rotor_A.top_letter == "F"
    assert rotor_B.top_letter == "A"
    assert rotor_C.top_letter == "A"

    rotor_A.top_letter = "Q"
    rotor_B.top_letter = "Q"
    rotor_C.top_letter = "Z"

    assert cipher_string(config, "HELLO") == "YKMGG"

    rotor_A.top_letter = "F"
    rotor_B.top_letter = "E"
    rotor_C.top_letter = "H"

    assert cipher_string(config, "POZDRAWIAMCIEPLUTKOZFRONTU")\
        == "OTPMSTXGPDYCODVTLFTXEMJVDZ"

    rotor_A.top_letter = "F"
    rotor_B.top_letter = "E"
    rotor_C.top_letter = "H"

    assert cipher_string(config, "OTPMSTXGPDYCODVTLFTXEMJVDZ")\
        == "POZDRAWIAMCIEPLUTKOZFRONTU"

    rotor_A.top_letter = "P"
    rotor_B.top_letter = "V"
    rotor_C.top_letter = "A"

    assert cipher_string(config, "UWAGANAFLANKEZLEWEJ")\
        == "ENLUGHNOYGPHMKWWASS"

    rotor_A.top_letter = "P"
    rotor_B.top_letter = "V"
    rotor_C.top_letter = "A"

    assert cipher_string(config, "ENLUGHNOYGPHMKWWASS")\
        == "UWAGANAFLANKEZLEWEJ"

    rotor_A.top_letter = "O"
    rotor_B.top_letter = "D"
    rotor_C.top_letter = "V"

    assert cipher_string(config, "POZDROWODZU")\
        == "BTUMWLFPUKQ"


def test_read_config_from_json():

    with open('test_config.json', 'r') as file_handle:
        config = enigma_io.read_config_from_json(file_handle)

    assert config.rotors[0].wiring == "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    assert config.rotors[0].top_letter == "A"
    assert config.rotors[0].turnover == "Q"

    assert config.plugs == [("A", "Z"), ("C", "F"), ("P", "B"),
                            ("K", "E"), ("U", "G"), ("W", "N"), ("X", "Y")]

    assert config.reflector_map == "YRUHQSLDPXNGOKMIEBFZCWVJAT"


def test_create_plugboard_visual():
    assert create_plugboard_visual(plugs) == "AZ CF PB KE UG WN XY"


def test_rotor_regress_and_advance():
    rotor = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "A")
    rotor.regress()
    assert rotor.top_letter == "Z"
    rotor.advance()
    assert rotor.top_letter == "A"
    rotor.top_letter = "Q"
    rotor.advance()
    assert rotor.top_letter == "R"
    rotor.top_letter = "Y"
    rotor.regress()
    assert rotor.top_letter == "X"
