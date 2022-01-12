import string
import re

alphabet = string.ascii_uppercase


# Config checking methods


def check_letter_pair(obj):
    """Checks if specified object is a two element tuple containing single
     uppercase letters.
    Used in map_plugboard."""
    if not isinstance(obj, tuple):
        raise InvalidPlugboardError("Plugs should be specified as tuples.")
    if not len(obj) == 2:
        raise InvalidPlugboardError("Plugs must specify two elements")
    for i in obj:
        check_letter(i, InvalidPlugboardError("Plugs must be uppercase\
letters."))


def check_letter_pair_list(obj):
    """Checks if specified object is a list containing only letter pairs."""
    letters = ""
    if not isinstance(obj, list):
        raise InvalidPlugboardError("Plugboard in config must be specified\
as a list.")
    for i in obj:
        check_letter_pair(i)
        if obj.count(i) > 1:
            raise InvalidPlugboardError("Plug duplication found.")
        if tuple(reversed(i)) in obj:
            raise InvalidPlugboardError("Plug duplication found.")
        letters += i[0] + i[1]
    for i in letters:
        if letters.count(i) > 1:
            raise InvalidPlugboardError("Same letter appears twice")


def check_letter(obj, exception):
    """Checks if specified object is a single letter string."""
    if not isinstance(obj, str):
        raise exception
    if len(obj) != 1:
        raise exception
    if obj not in alphabet:
        raise exception


def check_cipher_string(obj):
    """Checks if specified object is a string cipherable by enigma."""
    if not isinstance(obj, str):
        raise InvalidEnigmaCiphertextString("Given plaintext is not a string")
    for i in obj:
        if i == " ":
            continue
        check_letter(i, InvalidEnigmaCiphertextString)


def check_wiring(obj):
    """Checks if specified enigma wiring is correct."""
    if not isinstance(obj, str):
        raise InvalidWiringError("Specified wiring is not a string")
    if not len(obj) == 26:
        raise InvalidWiringError("Wiring must be 26 letters long")
    for i in obj:
        if obj.count(i) > 1:
            raise InvalidWiringError("Letter duplication found")
        check_letter(i, InvalidWiringError)


# Ciphering methods


def find_alphabet_index(letter):
    """Finds an alphabet index of specified upper case character."""
    return alphabet.find(letter)


def find_alphabet_letter(index):
    """Finds a letter corresponding to specified index"""
    return alphabet[index]


def map_right_to_left(wiring, top_letter, ring_setting, input_pos):
    """Find rotor's left side output index.
    top_letter is the visible by an operator rotor's offset indication."""
    offset = find_alphabet_index(top_letter)
    input_letter_index = (offset + input_pos) % 26
    output_letter = wiring[(input_letter_index - ring_setting) % 26]
    output_index = (
        find_alphabet_index(output_letter) - offset + ring_setting) % 26

    return output_index


def map_left_to_right(wiring, top_letter, ring_setting, input_pos):
    """Find rotor's right side output index.
    top_letter is the visible by an operator rotor's offset indication."""
    offset = find_alphabet_index(top_letter)
    input_letter_index = (offset + input_pos) % 26
    input_letter = find_alphabet_letter(
        (input_letter_index - ring_setting) % 26)
    output_index = (wiring.find((input_letter)) - offset + ring_setting) % 26
    return output_index


def map_reflector(reflector_map, input_pos):
    """Outputs exit position of current going though
       specified input position in reflector."""
    output_letter = reflector_map[input_pos]
    output_index = find_alphabet_index(output_letter)

    return output_index


def map_plugboard(pairs, input_pos):
    """Outputs exit position of current going through
        specified input position in plugboard.
        Pairs is an array of two element tuples,
        which represent connected letters in
        physical machine."""
    input_letter = find_alphabet_letter(input_pos)
    output_letter = None
    for i in pairs:
        if input_letter in i:
            if input_letter == i[0]:
                output_letter = i[1]
            else:
                output_letter = i[0]
            break
    if output_letter:
        output_pos = find_alphabet_index(output_letter)
    else:
        output_pos = input_pos

    return output_pos


def cipher_character(config, char):
    """Outputs a cipher of single character using
       specified enigma configuration"""
    input_pos = find_alphabet_index(char)

    input_pos = map_plugboard(config.plugs, input_pos)

    for i in config.rotors:
        input_pos = map_right_to_left(i.wiring, i.top_letter,
                                      i.ring_setting, input_pos)

    input_pos = map_reflector(config.reflector_map, input_pos)

    for i in config.rotors[::-1]:
        input_pos = map_left_to_right(i.wiring, i.top_letter,
                                      i.ring_setting, input_pos)

    input_pos = map_plugboard(config.plugs, input_pos)

    output_character = find_alphabet_letter(input_pos)
    return output_character


def cipher_string(config, plaintext):
    """Ciphers plaintext using specified enigma config.
        Note that strings can only contain uppercased english letter.
        Spaces and comas are forbidden."""
    cipher = ""
    for i in plaintext:
        if i == " ":
            cipher += " "
            continue
        config.step()
        cipher += cipher_character(config, i)
    return cipher


def create_plugboard_visual(plugs):
    output = ""
    for pair in plugs[:-1]:
        output += pair[0] + pair[1] + " "
    output += plugs[-1][0] + plugs[-1][1]
    return output


def transform_to_cipherable(data):
    data = data.upper()
    data = data.replace('\n', ' ')
    data = re.sub(' +', ' ', data)
    new_data = ''
    for letter in data:
        if letter in alphabet+' ':
            new_data += letter
    return new_data


# Excpetions

class InvalidWiringError(Exception):
    def __init__(self, info="Wiring should be specified by 26\
 upper case letters each appearing only once."):
        super().__init__(info)


class InvalidPlugboardError(Exception):
    def __init__(self, info="Invalid plugboard set specified."):
        super().__init__(info)


class InvalidEnigmaCiphertextString(Exception):
    def __init__(self, info="Enigma ciphertext should only contain\
uppercase letters. Symbols such as spaces and comas ar forbidden."):
        super().__init__(info)


class InvalidTurnoverSettingSpecified(Exception):
    def __init__(self, info="Turnover setting should be specified\
as single uppercase letter."):
        super().__init__(info)


class InvalidLetterSettingSpecified(Exception):
    def __init__(self, info="Starting letter setting should be specified\
as single uppercase letter."):
        super().__init__(info)
