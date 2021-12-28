import json
import sys

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
        self.update_rotor_display()

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

    def open_file(self):
        file_path = QFileDialog.getOpenFileName(self, 'Open file')

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


def guiMain(args):
    app = QApplication(args)
    window = enigmaAppWindow()
    window.show()

    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
