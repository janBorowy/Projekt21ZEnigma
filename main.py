import sys

from PySide2.QtWidgets import QApplication, QMainWindow
from ui_enigma import Ui_MainWindow
import enigma_cipher
import enigma_io


class enigmaAppWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ciphertext = ''
        self.plaintext = ''
        self.letter_lit = None
        self.lamp_lit = None

        self.ui.clear_button.clicked.connect(self.clear_text_browsers)
        self.ui.reset_button.clicked.connect(self.reset_rotors)
        try:
            with open('config.json') as file_handle:
                self.config = enigma_io.read_config_from_json(file_handle)
        except Exception as e:
            print(e)
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
        ui.rotor_A_wiring.setText("Rotor A wiring: "
                                  + self.config.rotors[0].wiring)
        ui.rotor_B_wiring.setText("Rotor B wiring: "
                                  + self.config.rotors[1].wiring)
        ui.rotor_C_wiring.setText("Rotor C wiring: "
                                  + self.config.rotors[2].wiring)
        ui.rotor_A_turnover.setText("Rotor A turnover: "
                                    + self.config.rotors[0].turnover)
        ui.rotor_B_turnover.setText("Rotor B turnover: "
                                    + self.config.rotors[1].turnover)
        ui.rotor_C_turnover.setText("Rotor C turnover: "
                                    + self.config.rotors[2].turnover)
        ui.reflector_wiring.setText("Reflector wiring: "
                                    + self.config.reflector_map)
        ui.plugboard.setText("Plugboard: " + enigma_cipher.
                             create_plugboard_visual(self.config.plugs)
                             + " AA AA AA AA AA AA")


def guiMain(args):
    app = QApplication(args)
    window = enigmaAppWindow()
    window.show()

    return app.exec_()


if __name__ == '__main__':
    guiMain(sys.argv)
