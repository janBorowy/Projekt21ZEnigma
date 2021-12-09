import string

alphabet = string.ascii_uppercase

rotor_wiring_A = "DMTWSILRUYQNKFEJCAZBPGXOHV"
rotor_wiring_B = "HQZGPJTMOBLNCIFDYAWVEUSRKX"
rotor_wiring_C = "UQNTLSZFMREHDPXKIBVYGJCWOA"

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

def map_right_to_left(wiring, top_letter, input_index):
    """Find rotor's left side output index.
    top_letter is the visible by an operator rotor's offset indication."""
    offset = find_alphabet_index(top_letter)
    input_index_offset = (input_index + offset)%26
    output_letter = wiring[input_index_offset]
    output_index = find_alphabet_index(output_letter)

    return output_index
def map_left_to_right(wiring, top_letter, input_index):
    """Find rotor's right side output index.
    top_letter is the visible by an operator rotor's offset indication."""
    offset = find_alphabet_index(top_letter)
    input_letter = find_alphabet_letter(input_index)
    output_index_offset = wiring.find(input_letter)
    output_index = (output_index_offset - offset)%26

    return output_index
class IncorrectAlphabetLetterError(Exception):
    def __init__(self):
        super().__init__("Input letter should be enligsh alphabet characters and uppercased.")