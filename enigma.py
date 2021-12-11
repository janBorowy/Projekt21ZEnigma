import string

alphabet = string.ascii_uppercase

def check_letter_pair(obj):
    """Checks if specified object is a two element tuple containing single uppercase letters.
    Used in map_plugboard."""
    if not isinstance(obj, tuple): raise IncorrectLetterPairError
    if not len(obj) == 2: raise IncorrectLetterPairError
    for i in obj:
        check_letter(i)

def check_letter_pair_list(obj):
    """Checks if specified object is a list containing only letter pairs."""
    if not isinstance(obj, list): raise TypeError
    for i in obj:
        check_letter_pair(i)
        if obj.count(i) > 1: raise IncorrectLetterPairListError
        if tuple(reversed(i)) in obj: raise IncorrectLetterPairListError

def check_letter(obj):
    """Checks if specified object is a single letter string."""
    if not isinstance(obj, str): raise IncorrectEnigmaLetterError
    if len(obj) != 1: raise IncorrectEnigmaLetterError
    if not obj in alphabet: raise IncorrectEnigmaLetterError

def check_index(obj):
    """Checks if specified object is an intager between 0 and 26."""
    if not isinstance(obj, int): raise TypeError
    if not obj in range(0, 26): raise ValueError

def check_wiring(obj):
    if not isinstance(obj, str): raise InvalidWiringError
    if not len(obj) == 26: raise InvalidWiringError
    for i in obj:
        if obj.count(i) > 1: raise InvalidWiringError
        check_letter(i)

def find_alphabet_index(letter):
    """Finds an alphabet index of specified upper case character."""
    check_letter(letter)
    if alphabet.find(letter) != -1: return alphabet.find(letter)
    raise IncorrectEnigmaLetterError

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
    """Outputs exit position of current going though specified input position in reflector."""
    output_letter = reflector_map[input_pos]
    output_index = find_alphabet_index(output_letter)

    return output_index

def map_plugboard(pairs, input_pos):
    """Outputs exit position of current going through specified input position in plugboard.
        Pairs is an array of two element tuples, which represent connected letters in 
        physical machine."""
    check_letter_pair_list(pairs)
    input_letter = find_alphabet_letter(input_pos)
    output_letter = None
    for i in pairs:
        if input_letter in i:
            if input_letter == i[0]: output_letter = i[1]
            else : output_letter = i[0]
            break
    if output_letter:
        output_pos = find_alphabet_index(output_letter)
    else: output_pos = input_pos

    return output_pos

def cipher_character(config, char):
    """Outputs a cipher of single character using specified enigma configuration"""
    input_pos = find_alphabet_index(char)

    input_pos = map_plugboard(config.plugs, input_pos)

    for i in config.rotors:
        input_pos = map_right_to_left(i.wiring, i.top_letter, input_pos)
    
    input_pos = map_reflector(config.reflector_map, input_pos)

    for i in config.rotors[::-1]:
        input_pos = map_left_to_right(i.wiring, i.top_letter, input_pos)

    input_pos = map_plugboard(config.plugs, input_pos)

    output_character = find_alphabet_letter(input_pos)
    return output_character

def cipher_string(config, str):
    """Ciphers enitre string using specified enigma config. Note that strings can only contain uppercased english letter. Spaces and comas are forbidden."""

class Rotor:
    def __init__(self, wiring, turnover, top_letter="A"):
        check_wiring(wiring)
        self.wiring = wiring
        self.top_letter = top_letter
        self.turnover = turnover

    def step(self):
        top_letter_index = find_alphabet_index(self.top_letter)
        if not top_letter_index == 25:
            self.top_letter = find_alphabet_letter(top_letter_index + 1)
        else: self.top_letter = "A"

class Config:
    def __init__(self, rotors, plugs, reflector_map):
        self.rotors = rotors # list of rotors in order the current flows when it first passes
        self.plugs = plugs
        self.reflector_map = reflector_map

    def step(self):
        top_letter_A = self.rotors[0].top_letter
        top_letter_B = self.rotors[1].top_letter

        if self.rotors[1].turnover == top_letter_B:
            self.rotors[2].step()

        if self.rotors[0].turnover == top_letter_A:
            self.rotors[1].step()
        
        self.rotors[0].step()

class IncorrectLetterPairError(Exception):
    def __init__(self):
        super().__init__("Letter pairs given to map_plugboard function should be two element tuples conataining single uppercase characters.")

class IncorrectLetterPairListError(Exception):
    def __init__(self):
        super().__init__("Letter pair list should contain only elements which fulfill letter pair conditions. No two elements can contain the same character.")

class InvalidWiringError(Exception):
    def __init__(self):
        super().__init__("Wiring should be specified by 26 upper case letters each appearing only once.")

class IncorrectEnigmaLetterError(Exception):
    def __init__(self):
        super().__init__("Letters used in enigma should be uppercase english letters.")