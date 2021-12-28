from enigma_cipher import check_wiring,\
    find_alphabet_index, find_alphabet_letter


class Rotor:
    def __init__(self, wiring, turnover, top_letter="A", ring_setting=0):
        check_wiring(wiring)
        self.wiring = wiring
        self.top_letter = top_letter
        self.turnover = turnover
        self.ring_setting = ring_setting

    def step(self):
        top_letter_index = find_alphabet_index(self.top_letter)
        if not top_letter_index == 25:
            self.top_letter = find_alphabet_letter(top_letter_index + 1)
        else:
            self.top_letter = "A"

    def advance(self):
        top_letter_index = find_alphabet_index(self.top_letter)
        top_letter_index = top_letter_index + 1\
            if top_letter_index != 25 else 0
        self.top_letter = find_alphabet_letter(top_letter_index)

    def regress(self):
        top_letter_index = find_alphabet_index(self.top_letter)
        top_letter_index = top_letter_index - 1\
            if top_letter_index != 0 else 25
        self.top_letter = find_alphabet_letter(top_letter_index)


class Config:
    def __init__(self, rotors, plugs, reflector_map):
        # list of rotors in order the current flows when it first passes
        self.rotors = rotors
        self.plugs = plugs
        self.reflector_map = reflector_map

    def step(self):
        top_letter_A = self.rotors[0].top_letter
        top_letter_B = self.rotors[1].top_letter

        if self.rotors[1].turnover == top_letter_B:
            self.rotors[1].step()
            self.rotors[2].step()

        if self.rotors[0].turnover == top_letter_A and\
           self.rotors[1].turnover != top_letter_B:
            self.rotors[1].step()

        self.rotors[0].step()
