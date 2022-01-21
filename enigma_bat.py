from enigma_config_io import MissingConfigKeyError, read_config_from_json
import enigma_cipher
import json
import sys
import argparse
from textwrap import wrap


def validate_key(key):
    # Only validates if key is a valid string.
    # Doesn't validate key values
    if not isinstance(key, str):
        raise IncorrectKeySpecifiedError
    if not len(key) == 9:
        raise IncorrectKeySpecifiedError


def receive_key(key):
    # Allow keys as in A01B02C03
    letters = []
    for i in key[::3]:
        letters.append(i)
    numbers = []
    for letter in letters:
        enigma_cipher.check_letter(letter, IncorrectKeySpecifiedError)
    for i in range(3):
        numbers.append(key[i*3 + 1] + key[i*3 + 2])
    for number in numbers:
        if not number.isdigit():
            raise IncorrectKeySpecifiedError
        if int(number) not in range(26):
            raise IncorrectKeySpecifiedError
    for i in range(3):
        numbers[i] = int(numbers[i])
    return letters, numbers


def init_config(key, config_file_path):
    try:
        validate_key(key)
        received = receive_key(key)
    except IncorrectKeySpecifiedError:
        print("Incorrect key specified. Key should consist only of uppercase letters \
and numbers as in examples: A00A00A00, G23D04E11")
        exit()
    letters = received[0]
    ring_settings = received[1]
    try:
        with open(config_file_path) as file_handle:
            config = read_config_from_json(file_handle)
            if isinstance(file_handle, str):
                json.loads(file_handle)
        for i in range(len(config.rotors)):
            config.rotors[i].top_letter = letters[i]
            config.rotors[i].ring_setting = ring_settings[i]
    except ValueError:
        print("config_bat.json file is corrupted, \
if the problem persists try deleting it")
        exit()
    except MissingConfigKeyError:
        print("config_bat.json file is missing data, \
if the problem persists try deleting it")
        exit()
    except FileNotFoundError:
        print("config_bat.json couldn't be found, \
creating default settings file.")
        create_default_config_file()
        with open('config_bat.json') as file_handle:
            config = read_config_from_json(file_handle)
    except enigma_cipher.InvalidLetterSettingSpecified:
        print("Invalid starting letter specified in \
config_bat.json file, even though this input \
is redundant")
        exit()
    except enigma_cipher.InvalidPlugboardError:
        print("Invalid plugboard setting specified in \
config.json file")
        exit()
    except enigma_cipher.InvalidTurnoverSettingSpecified:
        print("Incorrect turnover setting specified in \
config.json file")
        exit()
    except enigma_cipher.InvalidWiringError:
        print("Incorrect wiring specified in \
config.json file")
        exit()
    return config


def create_default_config_file():
    data = {
        "rotorA_wiring": "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
        "rotorA_starting_letter": "A",
        "rotorA_turnover": "Q",

        "rotorB_wiring": "AJDKSIRUXBLHWTMCQGZNPYFVOE",
        "rotorB_starting_letter": "A",
        "rotorB_turnover": "E",

        "rotorC_wiring": "BDFHJLCPRTXVZNYEIWGAKMUSQO",
        "rotorC_starting_letter": "A",
        "rotorC_turnover": "V",

        "reflector_map": "YRUHQSLDPXNGOKMIEBFZCWVJAT",

        "plugs": []
    }
    with open('config_bat.json', 'w') as file_handle:
        data = json.dumps(data, indent=1)
        file_handle.write(data)


def cipher_file(file_handle, config):
    data = file_handle.read().split("\n")
    ciphertext = ''
    for line in data:
        line = enigma_cipher.transform_to_cipherable(line)
        line = line + " "
        ciphertext += enigma_cipher.\
            cipher_string(config, line)
    return ciphertext


def cipher_text(plaintext, config):
    plaintext = enigma_cipher.transform_to_cipherable(plaintext)
    ciphertext = enigma_cipher.cipher_string(config, plaintext)
    return ciphertext


def generate_settings_in_str(config):
    str_settings = f'Ciphered with key: \
{config.rotors[0].top_letter}{config.rotors[0].ring_setting:02}\
{config.rotors[1].top_letter}{config.rotors[1].ring_setting:02}\
{config.rotors[2].top_letter}{config.rotors[2].ring_setting:02}'
    return str_settings


def transform_ciphertext(ciphertext, str_settings):
    data = wrap(ciphertext, 79)
    data_str = ""
    for line in data:
        data_str += line + "\n"
    data_str += "\n" + str_settings
    return data_str


class IncorrectKeySpecifiedError(Exception):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    missing_input_msg = "No file to cipher specified."

    parser = argparse.ArgumentParser(description="Cipher file using key")
    parser.add_argument('-k', '--key', metavar='', help='Key \
used to cipher the file. Must be in format: LNNLNNLNN, where L is a top \
letter of the rotor and NN is a ringsetting.', required=True)
    if not sys.stdin.isatty():
        plaintext = sys.stdin.read()

    parser.add_argument('-path', '--file_path', metavar='',
                        type=str, help="File_path of the file to be ciphered. \
this variable is prioritized over pipe.")
    parser.add_argument('-q', '--quiet', action='store_true',
                        help='print quiet')

    args = parser.parse_args()

    key = args.key

    config = init_config(key, 'config_bat.json')
    str_settings = generate_settings_in_str(config) if not args.quiet else ""

    # open file to cipher
    if args.file_path:
        file_path = args.file_path
        try:
            with open(file_path, 'r') as file_handle:
                ciphertext = cipher_file(file_handle, config)
        except FileNotFoundError:
            print("Couldn't find file to cipher using file_path.")
            exit()
    else:
        if sys.stdin.isatty():
            print(missing_input_msg)
            exit()
        ciphertext = cipher_text(plaintext, config)

    ciphertext = transform_ciphertext(ciphertext, str_settings)

    sys.stdout.write(ciphertext+"\n")
