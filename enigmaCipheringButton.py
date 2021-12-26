from PySide2.QtWidgets import QPushButton


class enigmaCipheringButton(QPushButton):
    def __init__(self, parent=None) -> None:
        super().__init__(parent=parent)
        self.clicked.connect(self.button_pressed)
        self.window = self.parent().parent()

    def button_pressed(self):
        self.window.update_ciphertext_browser(self.text())
        self.window.update_plaintext_browser(self.text())
        self.window.update_rotor_display()
