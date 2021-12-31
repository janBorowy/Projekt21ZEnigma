import json
import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog,\
    QMessageBox
from ui_enigma import Ui_MainWindow
import enigma_cipher
import enigma_config_io
import os
from textwrap import wrap


class enigmaAppWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Enigma simulator")

        try:
            with open('config.json') as file_handle:
                self.config = enigma_config_io.\
                    read_config_from_json(file_handle)
                if isinstance(file_handle, str):
                    json.loads(file_handle)
        except ValueError:
            QMessageBox.warning(self, "Configuartion error",
                                "config.json file is corrupted.\n\
If the error persists, try deleting it.")
            exit()
        except enigma_config_io.MissingConfigKeyError:
            QMessageBox.warning(self, "Configuartion error",
                                "config.json is missing data.\n\
If the error persists, try deleting it.")
            exit()
        except FileNotFoundError:
            QMessageBox.information(self, "Configuration error",
                                    "config.json file not found, \
creating default")
            self.create_default_config_file()
            with open('config.json') as file_handle:
                self.config = enigma_config_io.\
                    read_config_from_json(file_handle)
        except enigma_cipher.InvalidLetterSettingSpecified:
            QMessageBox.warning(self, "Configuration error",
                                "Incorrect starting letter specified in \
config.json file")
            exit()
        except enigma_cipher.InvalidPlugboardError:
            QMessageBox.warning(self, "Configuration error",
                                "Invalid plugboard setting specified in \
config.json file")
        except enigma_cipher.InvalidTurnoverSettingSpecified:
            QMessageBox.warning(self, "Configuration error",
                                "Incorrect turnover setting specified in \
config.json file")
            exit()
        except enigma_cipher.InvalidWiringError:
            QMessageBox.warning(self, "Configuration error",
                                "Incorrect wiring specified in \
config.json file")
            exit()

        self.ciphertext = ''
        self.plaintext = ''
        self.letter_lit = None
        self.lamp_lit = self.ui.lamp_A

        self.ui.clear_button.clicked.connect(self.clear_text_browsers)
        self.ui.reset_button.clicked.connect(self.reset_rotors)
        self.ui.action_open.triggered.connect(self.open_file)
        self.ui.action_save_as.triggered.connect(self.save_file)
        self.ui.action_save_only.triggered.connect(self.save_only_cipher_file)
        self.ui.action_cipher_directly.\
            triggered.connect(self.save_cipher_directly)

        self.ui.button_space.clicked.connect(self.input_space)

        self.set_up_config_box()

        self.ui.rotor_A_advance.clicked.connect(lambda: self.advance_rotor(0))
        self.ui.rotor_A_regress.clicked.connect(lambda: self.regress_rotor(0))
        self.ui.rotor_B_advance.clicked.connect(lambda: self.advance_rotor(1))
        self.ui.rotor_B_regress.clicked.connect(lambda: self.regress_rotor(1))
        self.ui.rotor_C_advance.clicked.connect(lambda: self.advance_rotor(2))
        self.ui.rotor_C_regress.clicked.connect(lambda: self.regress_rotor(2))

        self.update_ring_setting_display()
        self.update_rotor_display()

        self.ui.ring_setting_A_advance.clicked.\
            connect(lambda: self.ring_setting_advance(0))
        self.ui.ring_setting_A_regress.clicked.\
            connect(lambda: self.ring_setting_regress(0))
        self.ui.ring_setting_B_advance.clicked.\
            connect(lambda: self.ring_setting_advance(1))
        self.ui.ring_setting_B_regress.clicked.\
            connect(lambda: self.ring_setting_regress(1))
        self.ui.ring_setting_C_advance.clicked.\
            connect(lambda: self.ring_setting_advance(2))
        self.ui.ring_setting_C_regress.clicked.\
            connect(lambda: self.ring_setting_regress(2))

    def update_rotor_display(self):
        self.ui.rotor_A_display.setText(self.config.rotors[0].top_letter)
        self.ui.rotor_B_display.setText(self.config.rotors[1].top_letter)
        self.ui.rotor_C_display.setText(self.config.rotors[2].top_letter)

    def advance_rotor(self, index):
        self.config.rotors[index].advance()
        self.update_rotor_display()

    def regress_rotor(self, index):
        self.config.rotors[index].regress()
        self.update_rotor_display()

    def update_ciphertext_browser(self, letter):
        if letter != " ":
            self.config.step()
            cipher_letter = enigma_cipher.cipher_character(self.config, letter)
            self.light_up_lamp(cipher_letter)
        else:
            cipher_letter = " "
        self.ciphertext += cipher_letter
        self.ui.CipherTextBrowser.setText(self.ciphertext)

    def update_plaintext_browser(self, letter):
        self.plaintext += letter
        self.ui.PlainTextBrowser.setText(self.plaintext)

    def clear_text_browsers(self):
        self.plaintext = ''
        self.ciphertext = ''
        self.ui.PlainTextBrowser.setText(self.plaintext)
        self.ui.CipherTextBrowser.setText(self.ciphertext)
        self.lamp_lit.turn_off()

    def reset_rotors(self):
        for rotor in self.config.rotors:
            rotor.top_letter = "A"
        for rotor in self.config.rotors:
            rotor.ring_setting = 0
        self.update_rotor_display()
        self.update_ring_setting_display()

    def light_up_lamp(self, letter):
        if self.lamp_lit:
            self.lamp_lit.turn_off()
            self.lamp_lit = getattr(self.ui, f'lamp_{letter}')
            self.lamp_lit.light_up()
        else:
            self.lamp_lit = getattr(self.ui, f'lamp_{letter}')
            self.lamp_lit.light_up()

    def set_up_config_box(self):
        ui = self.ui
        ui.rotor_A_wiring.setText("Rotor A wiring: \n"
                                  + self.config.rotors[0].wiring)
        ui.rotor_B_wiring.setText("Rotor B wiring: \n"
                                  + self.config.rotors[1].wiring)
        ui.rotor_C_wiring.setText("Rotor C wiring: \n"
                                  + self.config.rotors[2].wiring)
        ui.rotor_A_turnover.setText("Rotor A turnover: "
                                    + self.config.rotors[0].turnover)
        ui.rotor_B_turnover.setText("Rotor B turnover: "
                                    + self.config.rotors[1].turnover)
        ui.rotor_C_turnover.setText("Rotor C turnover: "
                                    + self.config.rotors[2].turnover)
        ui.reflector_wiring.setText("Reflector wiring: \n"
                                    + self.config.reflector_map)
        self.set_up_plugboard_text()

    def set_up_plugboard_text(self):
        if len(self.config.plugs) == 0:
            return
        text = "Plugboard: " + enigma_cipher.\
            create_plugboard_visual(self.config.plugs)
        if len(text) // 31 == 1:
            text = text[:31]+"\n                 "+text[31:]
        self.ui.plugboard.setText(text)

    def update_ring_setting_display(self):
        self.ui.ring_setting_A.setText("Ring setting: " +
                                       str(self.config.rotors[0].ring_setting))
        self.ui.ring_setting_B.setText("Ring setting: " +
                                       str(self.config.rotors[1].ring_setting))
        self.ui.ring_setting_C.setText("Ring setting: " +
                                       str(self.config.rotors[2].ring_setting))

    def ring_setting_advance(self, rotor_index):
        ring_setting = self.config.rotors[rotor_index].ring_setting
        ring_setting = ring_setting + 1 if ring_setting < 25 else 0
        self.config.rotors[rotor_index].ring_setting = ring_setting
        self.update_ring_setting_display()

    def ring_setting_regress(self, rotor_index):
        ring_setting = self.config.rotors[rotor_index].ring_setting
        ring_setting = ring_setting - 1 if ring_setting > 0 else 25
        self.config.rotors[rotor_index].ring_setting = ring_setting
        self.update_ring_setting_display()

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file')[0]
        self.ciphertext = ""
        self.plaintext = ""
        try:
            if os.path.getsize(file_path) > 5000:
                raise FileSizeError
            with open(file_path, 'r') as file_handle:
                data = file_handle.read().split("\n")
                for line in data:
                    line = enigma_cipher.transform_to_cipherable(line)
                    line = line+" "
                    self.plaintext += line
                    self.ciphertext += enigma_cipher.\
                        cipher_string(self.config, line)
            self.update_rotor_display()
            self.ui.CipherTextBrowser.setText(self.ciphertext)
            self.ui.PlainTextBrowser.setText(self.plaintext)
        except FileNotFoundError:
            return
        except FileSizeError:
            QMessageBox.warning(self, "File too big",
                                "Text files shouldn't be bigger than 5KB")

    def save_file(self):
        save_path = QFileDialog.getSaveFileName(self, "Save as...")[0]
        try:
            with open(save_path, 'w') as file_handle:
                data_plaintext = wrap(self.plaintext, 79)
                data_ciphertext = wrap(self.ciphertext, 79)
                data = ''
                for line in data_plaintext:
                    data += line+"\n"
                data += "-----------------\n"
                for line in data_ciphertext:
                    data += line+"\n"
                file_handle.write(data)
        except FileNotFoundError:
            return

    def save_only_cipher_file(self):
        save_path = QFileDialog.getSaveFileName(self, "Save as...")[0]
        try:
            with open(save_path, 'w') as file_handle:
                data = wrap(self.ciphertext, 79)
                data_str = ""
                for line in data:
                    data_str += line+"\n"
                file_handle.write(data_str)
        except FileNotFoundError:
            return

    def save_cipher_directly(self):
        # load
        str_settings = f'Ring settings: {str(self.config.rotors[2].ring_setting)} \
{str(self.config.rotors[1].ring_setting)} \
{str(self.config.rotors[0].ring_setting)} \
Rotors: {self.config.rotors[2].top_letter} \
{self.config.rotors[1].top_letter} \
{self.config.rotors[0].top_letter}'
        file_path = QFileDialog.getOpenFileName(self, 'Open file to cipher')[0]
        ciphertext = ""
        try:
            if os.path.getsize(file_path) > 10000000:
                raise FileSizeError
            with open(file_path, 'r') as file_handle:
                data = file_handle.read().split("\n")
                for line in data:
                    line = enigma_cipher.transform_to_cipherable(line)
                    line = line+" "
                    ciphertext += enigma_cipher.\
                        cipher_string(self.config, line)
            self.update_rotor_display()
        except FileNotFoundError:
            return
        except FileSizeError:
            QMessageBox.warning(self, "File too big",
                                "Text files ciphered directly \
                                shouldn't be bigger than 10MB")
        # save
        save_path = QFileDialog.getSaveFileName(self, "Save as...")[0]
        try:
            with open(save_path, 'w') as file_handle:
                data_save = wrap(ciphertext, 79)
                data_str = ""
                for line in data_save:
                    data_str += line+"\n"
                data_str += str_settings
                file_handle.write(data_str)
        except FileNotFoundError:
            pass

    def create_default_config_file(self):
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
        with open('config.json', 'w') as file_handle:
            data = json.dumps(data, indent=1)
            file_handle.write(data)

    def keyPressEvent(self, event):
        if event.key() == 16777248:
            self.input_space()
            return
        if event.text().isalpha():
            letter = str.upper(event.text())
            self.update_ciphertext_browser(letter)
            self.update_plaintext_browser(letter)
            self.update_rotor_display()

    def input_space(self):
        self.update_ciphertext_browser(" ")
        self.update_plaintext_browser(" ")


class FileSizeError(Exception):
    def __init__(self):
        super().__init__("File is too big.")


def guiMain(args):
    app = QApplication(args)
    window = enigmaAppWindow()
    window.show()

    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)