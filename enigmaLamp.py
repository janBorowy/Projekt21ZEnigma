from PySide2.QtWidgets import QLabel


class enigmaLamp(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def light_up(self):
        self.setStyleSheet("background-color: yellow")

    def turn_off(self):
        self.setStyleSheet("")
