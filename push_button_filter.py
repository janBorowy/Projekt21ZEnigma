from PySide2.QtWidgets import QPushButton
from PySide2 import QtCore


class MyPushButton(QPushButton):
    def __init__(self, *args):
        QPushButton.__init__(self, *args)

    def event(self, event):
        if (event.type() == QtCore.QEvent.KeyPress)\
             and (event.key() == QtCore.Qt.Key_Space):
            print("foo")

            return True

        return QPushButton.event(self, event)
