import string

alphabet = string.ascii_uppercase

def check_letter(obj):
    """Checks if specified object is a single letter string."""
    if not isinstance(obj, str): raise TypeError("Input letters should be strings.")
    if len(obj) != 1: raise ValueError("Input letters should be single characters.")

def check_index(obj):
    """Checks if specified object is an intager between 0 and 26."""
    if not isinstance(obj, int): raise TypeError
    if not obj in range(0, 26): raise ValueError

def find_alphabet_index(letter):
    """Finds an alphabet index of specified upper case character."""
    check_letter(letter)
    if alphabet.find(letter) != -1: return alphabet.find(letter)
    raise IncorrectAlphabetLetterError

def find_alphabet_letter(index):
    """Finds a letter corresponding to specified index"""
    check_index(index)
    return alphabet[index]

def map_right_to_left(wiring, top_letter, input_pos):
    """Find rotor's left side output index.
    top_letter is the visible by an operator rotor's offset indication."""
    offset = find_alphabet_index(top_letter)
    input_letter_index = (offset + input_pos)%26
    output_letter = wiring[input_letter_index]
    output_index = (find_alphabet_index(output_letter) - offset)%26

    return output_index
def map_left_to_right(wiring, top_letter, input_pos):
    """Find rotor's right side output index.
    top_letter is the visible by an operator rotor's offset indication."""
    offset = find_alphabet_index(top_letter)
    input_letter_index = (offset + input_pos)%26
    input_letter = find_alphabet_letter(input_letter_index)
    output_index = (wiring.find(input_letter) - offset)%26

    return output_index

def map_reflector(reflector_map, input_pos):
    """Outputs exit position of current going though specified input position"""
    output_letter = reflector_map[input_pos]
    output_index = find_alphabet_index(output_letter)

    return output_index
class IncorrectAlphabetLetterError(Exception):
    def __init__(self):
        super().__init__("Input letter should be enligsh alphabet characters and uppercased.")