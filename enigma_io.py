import enigma_classes
import enigma_cipher
import json


def initialize_rotor(data, index):
    enigma_cipher.check_wiring(data[f'rotor{index}_wiring'])
    enigma_cipher.check_letter(data[f'rotor{index}_turnover'],
                               enigma_cipher.InvalidTurnoverSettingSpecified)
    enigma_cipher.check_letter(data[f'rotor{index}_starting_letter'],
                               enigma_cipher.InvalidLetterSettingSpecified)
    wiring = data[f'rotor{index}_wiring']
    turnover = data[f'rotor{index}_turnover']
    top_letter = data[f'rotor{index}_starting_letter']

    return enigma_classes.Rotor(wiring, turnover, top_letter)


def read_config_from_json(file_handle):
    data = json.load(file_handle)
    try:
        enigma_cipher.check_wiring(data['reflector_map'])
        reflector_map = data['reflector_map']

        plugs = [tuple(plug) for plug in data['plugs']]
        enigma_cipher.check_letter_pair_list(plugs)

        rotorA = initialize_rotor(data, "A")
        rotorB = initialize_rotor(data, "B")
        rotorC = initialize_rotor(data, "C")
    except KeyError:
        raise MissingConfigKeyError('Config.json is missing a key.')

    return enigma_classes.Config([rotorA, rotorB, rotorC],
                                 plugs, reflector_map)


class MissingConfigKeyError(Exception):
    def __init__(self):
        super().__init__()
