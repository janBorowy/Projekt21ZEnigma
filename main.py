import json
import sys
import PySide2

from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog,\
    QMessageBox
from ui_enigma import Ui_MainWindow
import enigma_cipher
import enigma_io
import jsbeautifier


class enigmaAppWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        try:
            with open('config.json') as file_handle:
                self.config = enigma_io.read_config_from_json(file_handle)
                if isinstance(file_handle, str):
                    json.loads(file_handle)
        except ValueError:
            QMessageBox.warning(self, "Configuartion error",
                                "config.json file is corrupted.\n\
If the error persists, try deleting it.")
            exit()
        except enigma_io.MissingConfigKeyError:
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
                self.config = enigma_io.read_config_from_json(file_handle)
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

        self.set_up_config_box()

        self.ui.rotor_A_advance.clicked.connect(lambda: self.advance_rotor(0))
        self.ui.rotor_A_regress.clicked.connect(lambda: self.regress_rotor(0))
        self.ui.rotor_B_advance.clicked.connect(lambda: self.advance_rotor(1))
        self.ui.rotor_B_regress.clicked.connect(lambda: self.regress_rotor(1))
        self.ui.rotor_C_advance.clicked.connect(lambda: self.advance_rotor(2))
        self.ui.rotor_C_regress.clicked.connect(lambda: self.regress_rotor(2))

        self.update_ring_setting_display()

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
        self.config.step()
        cipher_letter = enigma_cipher.cipher_character(self.config, letter)
        self.ciphertext += cipher_letter
        self.light_up_lamp(cipher_letter)
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
        ciphertext = ""
        plaintext = ""
        with open(file_path, 'r') as file_handle:
            for line in file_handle:
                try:
                    enigma_cipher.check_cipher_string(line)
                except enigma_cipher.InvalidEnigmaCiphertextString:
                    QMessageBox.warning(self, "Invalid file error", "Invalid file given. \
Text files \
entered into enigma should \
only contain uppercase english alphabet letters.\n\
Symbols such as spaces and comas are foribdden.")
                    return
                plaintext += line
                ciphertext += enigma_cipher.cipher_string(self.config, line)
        self.clear_text_browsers()
        self.update_rotor_display()
        self.ui.CipherTextBrowser.setText(ciphertext)
        self.ui.PlainTextBrowser.setText(plaintext)

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

                "plugs": [["A", "Z"], ["C", "F"], ["P", "B"], ["K", "E"],
                          ["U", "G"], ["W", "N"], ["X", "Y"]]
        }
        with open('config.json', 'w') as file_handle:
            data = jsbeautifier.beautify(json.dumps(data))
            file_handle.write(data)

    def keyPressEvent(self, event: PySide2.QtGui.QKeyEvent):
        # if not len(event.text()) == 1:
        #     return
        if event.text().isalpha():
            letter = str.upper(event.text())
            self.update_ciphertext_browser(letter)
            self.update_plaintext_browser(letter)
            self.update_rotor_display()


def guiMain(args):
    app = QApplication(args)
    window = enigmaAppWindow()
    window.show()

    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
