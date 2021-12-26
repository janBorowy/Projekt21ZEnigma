# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from enigmaCipheringButton import enigmaCipheringButton
from enigmaLamp import enigmaLamp


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1116, 577)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.rotor_B_display = QLabel(self.centralwidget)
        self.rotor_B_display.setObjectName(u"rotor_B_display")
        font = QFont()
        font.setPointSize(48)
        self.rotor_B_display.setFont(font)
        self.rotor_B_display.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rotor_B_display, 0, 3, 2, 1)

        self.rotor_A_display = QLabel(self.centralwidget)
        self.rotor_A_display.setObjectName(u"rotor_A_display")
        self.rotor_A_display.setFont(font)
        self.rotor_A_display.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rotor_A_display, 0, 5, 2, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CipherTextBrowser = QTextBrowser(self.centralwidget)
        self.CipherTextBrowser.setObjectName(u"CipherTextBrowser")

        self.horizontalLayout.addWidget(self.CipherTextBrowser)

        self.PlainTextBrowser = QTextBrowser(self.centralwidget)
        self.PlainTextBrowser.setObjectName(u"PlainTextBrowser")

        self.horizontalLayout.addWidget(self.PlainTextBrowser)


        self.gridLayout_3.addLayout(self.horizontalLayout, 5, 0, 1, 7)

        self.rotor_C_advance = QPushButton(self.centralwidget)
        self.rotor_C_advance.setObjectName(u"rotor_C_advance")

        self.gridLayout_3.addWidget(self.rotor_C_advance, 0, 2, 1, 1)

        self.rotor_A_advance = QPushButton(self.centralwidget)
        self.rotor_A_advance.setObjectName(u"rotor_A_advance")

        self.gridLayout_3.addWidget(self.rotor_A_advance, 0, 6, 1, 1)

        self.rotor_B_regress = QPushButton(self.centralwidget)
        self.rotor_B_regress.setObjectName(u"rotor_B_regress")
        font1 = QFont()
        font1.setPointSize(12)
        self.rotor_B_regress.setFont(font1)

        self.gridLayout_3.addWidget(self.rotor_B_regress, 1, 4, 3, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lamp_W = enigmaLamp(self.centralwidget)
        self.lamp_W.setObjectName(u"lamp_W")
        font2 = QFont()
        font2.setPointSize(20)
        self.lamp_W.setFont(font2)
        self.lamp_W.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_W, 0, 2, 1, 1)

        self.lamp_V = enigmaLamp(self.centralwidget)
        self.lamp_V.setObjectName(u"lamp_V")
        self.lamp_V.setFont(font2)
        self.lamp_V.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_V, 2, 8, 1, 1)

        self.lamp_N = enigmaLamp(self.centralwidget)
        self.lamp_N.setObjectName(u"lamp_N")
        self.lamp_N.setFont(font2)
        self.lamp_N.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_N, 2, 12, 1, 1)

        self.lamp_E = enigmaLamp(self.centralwidget)
        self.lamp_E.setObjectName(u"lamp_E")
        self.lamp_E.setFont(font2)
        self.lamp_E.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_E, 0, 4, 1, 1)

        self.lamp_R = enigmaLamp(self.centralwidget)
        self.lamp_R.setObjectName(u"lamp_R")
        self.lamp_R.setFont(font2)
        self.lamp_R.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_R, 0, 6, 1, 1)

        self.lamp_O = enigmaLamp(self.centralwidget)
        self.lamp_O.setObjectName(u"lamp_O")
        self.lamp_O.setFont(font2)
        self.lamp_O.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_O, 0, 16, 1, 1)

        self.lamp_P = enigmaLamp(self.centralwidget)
        self.lamp_P.setObjectName(u"lamp_P")
        self.lamp_P.setFont(font2)
        self.lamp_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_P, 2, 0, 1, 1)

        self.lamp_I = enigmaLamp(self.centralwidget)
        self.lamp_I.setObjectName(u"lamp_I")
        self.lamp_I.setFont(font2)
        self.lamp_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_I, 0, 14, 1, 1)

        self.lamp_Y = enigmaLamp(self.centralwidget)
        self.lamp_Y.setObjectName(u"lamp_Y")
        self.lamp_Y.setFont(font2)
        self.lamp_Y.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_Y, 2, 2, 1, 1)

        self.lamp_C = enigmaLamp(self.centralwidget)
        self.lamp_C.setObjectName(u"lamp_C")
        self.lamp_C.setFont(font2)
        self.lamp_C.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_C, 2, 6, 1, 1)

        self.lamp_X = enigmaLamp(self.centralwidget)
        self.lamp_X.setObjectName(u"lamp_X")
        self.lamp_X.setFont(font2)
        self.lamp_X.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_X, 2, 4, 1, 1)

        self.lamp_T = enigmaLamp(self.centralwidget)
        self.lamp_T.setObjectName(u"lamp_T")
        self.lamp_T.setFont(font2)
        self.lamp_T.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_T, 0, 8, 1, 1)

        self.lamp_L = enigmaLamp(self.centralwidget)
        self.lamp_L.setObjectName(u"lamp_L")
        self.lamp_L.setFont(font2)
        self.lamp_L.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_L, 2, 16, 1, 1)

        self.lamp_Q = enigmaLamp(self.centralwidget)
        self.lamp_Q.setObjectName(u"lamp_Q")
        self.lamp_Q.setFont(font2)
        self.lamp_Q.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_Q, 0, 0, 1, 1)

        self.lamp_S = enigmaLamp(self.centralwidget)
        self.lamp_S.setObjectName(u"lamp_S")
        self.lamp_S.setFont(font2)
        self.lamp_S.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_S, 1, 3, 1, 1)

        self.lamp_Z = enigmaLamp(self.centralwidget)
        self.lamp_Z.setObjectName(u"lamp_Z")
        self.lamp_Z.setFont(font2)
        self.lamp_Z.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_Z, 0, 10, 1, 1)

        self.lamp_F = enigmaLamp(self.centralwidget)
        self.lamp_F.setObjectName(u"lamp_F")
        self.lamp_F.setFont(font2)
        self.lamp_F.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_F, 1, 7, 1, 1)

        self.lamp_U = enigmaLamp(self.centralwidget)
        self.lamp_U.setObjectName(u"lamp_U")
        self.lamp_U.setFont(font2)
        self.lamp_U.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_U, 0, 12, 1, 1)

        self.lamp_K = enigmaLamp(self.centralwidget)
        self.lamp_K.setObjectName(u"lamp_K")
        self.lamp_K.setFont(font2)
        self.lamp_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_K, 1, 15, 1, 1)

        self.lamp_B = enigmaLamp(self.centralwidget)
        self.lamp_B.setObjectName(u"lamp_B")
        self.lamp_B.setFont(font2)
        self.lamp_B.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_B, 2, 10, 1, 1)

        self.lamp_D = enigmaLamp(self.centralwidget)
        self.lamp_D.setObjectName(u"lamp_D")
        self.lamp_D.setFont(font2)
        self.lamp_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_D, 1, 5, 1, 1)

        self.lamp_G = enigmaLamp(self.centralwidget)
        self.lamp_G.setObjectName(u"lamp_G")
        self.lamp_G.setFont(font2)
        self.lamp_G.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_G, 1, 9, 1, 1)

        self.lamp_J = enigmaLamp(self.centralwidget)
        self.lamp_J.setObjectName(u"lamp_J")
        self.lamp_J.setFont(font2)
        self.lamp_J.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_J, 1, 13, 1, 1)

        self.lamp_H = enigmaLamp(self.centralwidget)
        self.lamp_H.setObjectName(u"lamp_H")
        self.lamp_H.setFont(font2)
        self.lamp_H.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_H, 1, 11, 1, 1)

        self.lamp_A = enigmaLamp(self.centralwidget)
        self.lamp_A.setObjectName(u"lamp_A")
        self.lamp_A.setFont(font2)
        self.lamp_A.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_A, 1, 1, 1, 1)

        self.lamp_M = enigmaLamp(self.centralwidget)
        self.lamp_M.setObjectName(u"lamp_M")
        self.lamp_M.setFont(font2)
        self.lamp_M.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_M, 2, 14, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 6, 0, 1, 6)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setPointSize(16)
        self.label.setFont(font3)

        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)

        self.rotor_A_regress = QPushButton(self.centralwidget)
        self.rotor_A_regress.setObjectName(u"rotor_A_regress")
        self.rotor_A_regress.setFont(font1)

        self.gridLayout_3.addWidget(self.rotor_A_regress, 1, 6, 3, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 4, 0, 1, 1)

        self.rotor_C_regress = QPushButton(self.centralwidget)
        self.rotor_C_regress.setObjectName(u"rotor_C_regress")
        self.rotor_C_regress.setFont(font1)

        self.gridLayout_3.addWidget(self.rotor_C_regress, 1, 2, 3, 1)

        self.config_box = QGroupBox(self.centralwidget)
        self.config_box.setObjectName(u"config_box")
        self.config_box.setMinimumSize(QSize(0, 0))
        self.config_box.setMaximumSize(QSize(300, 279))
        self.rotor_A_wiring = QLabel(self.config_box)
        self.rotor_A_wiring.setObjectName(u"rotor_A_wiring")
        self.rotor_A_wiring.setGeometry(QRect(10, 20, 301, 21))
        self.rotor_B_wiring = QLabel(self.config_box)
        self.rotor_B_wiring.setObjectName(u"rotor_B_wiring")
        self.rotor_B_wiring.setGeometry(QRect(10, 40, 301, 21))
        self.rotor_C_wiring = QLabel(self.config_box)
        self.rotor_C_wiring.setObjectName(u"rotor_C_wiring")
        self.rotor_C_wiring.setGeometry(QRect(10, 60, 301, 21))
        self.plugboard = QLabel(self.config_box)
        self.plugboard.setObjectName(u"plugboard")
        self.plugboard.setGeometry(QRect(10, 160, 351, 16))
        self.plugboard.setMinimumSize(QSize(0, 0))
        self.reflector_wiring = QLabel(self.config_box)
        self.reflector_wiring.setObjectName(u"reflector_wiring")
        self.reflector_wiring.setGeometry(QRect(10, 140, 271, 16))
        self.rotor_A_turnover = QLabel(self.config_box)
        self.rotor_A_turnover.setObjectName(u"rotor_A_turnover")
        self.rotor_A_turnover.setGeometry(QRect(10, 80, 271, 16))
        self.rotor_B_turnover = QLabel(self.config_box)
        self.rotor_B_turnover.setObjectName(u"rotor_B_turnover")
        self.rotor_B_turnover.setGeometry(QRect(10, 100, 271, 16))
        self.rotor_C_turnover = QLabel(self.config_box)
        self.rotor_C_turnover.setObjectName(u"rotor_C_turnover")
        self.rotor_C_turnover.setGeometry(QRect(10, 120, 271, 16))

        self.gridLayout_3.addWidget(self.config_box, 0, 8, 6, 1)

        self.rotor_B_advance = QPushButton(self.centralwidget)
        self.rotor_B_advance.setObjectName(u"rotor_B_advance")

        self.gridLayout_3.addWidget(self.rotor_B_advance, 0, 4, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_A = enigmaCipheringButton(self.centralwidget)
        self.button_A.setObjectName(u"button_A")
        font4 = QFont()
        font4.setPointSize(16)
        font4.setItalic(False)
        self.button_A.setFont(font4)

        self.gridLayout.addWidget(self.button_A, 1, 0, 1, 2)

        self.button_B = enigmaCipheringButton(self.centralwidget)
        self.button_B.setObjectName(u"button_B")
        self.button_B.setFont(font4)

        self.gridLayout.addWidget(self.button_B, 2, 9, 1, 2)

        self.button_H = enigmaCipheringButton(self.centralwidget)
        self.button_H.setObjectName(u"button_H")
        self.button_H.setFont(font4)

        self.gridLayout.addWidget(self.button_H, 1, 10, 1, 2)

        self.button_Z = enigmaCipheringButton(self.centralwidget)
        self.button_Z.setObjectName(u"button_Z")
        self.button_Z.setEnabled(True)
        self.button_Z.setFont(font4)

        self.gridLayout.addWidget(self.button_Z, 0, 9, 1, 2)

        self.button_R = enigmaCipheringButton(self.centralwidget)
        self.button_R.setObjectName(u"button_R")
        self.button_R.setEnabled(True)
        self.button_R.setFont(font4)

        self.gridLayout.addWidget(self.button_R, 0, 5, 1, 2)

        self.button_K = enigmaCipheringButton(self.centralwidget)
        self.button_K.setObjectName(u"button_K")
        self.button_K.setFont(font4)

        self.gridLayout.addWidget(self.button_K, 1, 14, 1, 2)

        self.button_D = enigmaCipheringButton(self.centralwidget)
        self.button_D.setObjectName(u"button_D")
        self.button_D.setFont(font4)

        self.gridLayout.addWidget(self.button_D, 1, 4, 1, 2)

        self.button_Y = enigmaCipheringButton(self.centralwidget)
        self.button_Y.setObjectName(u"button_Y")
        self.button_Y.setFont(font4)

        self.gridLayout.addWidget(self.button_Y, 2, 1, 1, 2)

        self.button_L = enigmaCipheringButton(self.centralwidget)
        self.button_L.setObjectName(u"button_L")
        self.button_L.setFont(font4)

        self.gridLayout.addWidget(self.button_L, 2, 15, 1, 1)

        self.button_F = enigmaCipheringButton(self.centralwidget)
        self.button_F.setObjectName(u"button_F")
        self.button_F.setFont(font4)

        self.gridLayout.addWidget(self.button_F, 1, 6, 1, 2)

        self.button_T = enigmaCipheringButton(self.centralwidget)
        self.button_T.setObjectName(u"button_T")
        self.button_T.setEnabled(True)
        self.button_T.setFont(font4)

        self.gridLayout.addWidget(self.button_T, 0, 7, 1, 2)

        self.button_C = enigmaCipheringButton(self.centralwidget)
        self.button_C.setObjectName(u"button_C")
        self.button_C.setFont(font4)

        self.gridLayout.addWidget(self.button_C, 2, 5, 1, 2)

        self.button_U = enigmaCipheringButton(self.centralwidget)
        self.button_U.setObjectName(u"button_U")
        self.button_U.setEnabled(True)
        self.button_U.setFont(font4)

        self.gridLayout.addWidget(self.button_U, 0, 11, 1, 2)

        self.button_E = enigmaCipheringButton(self.centralwidget)
        self.button_E.setObjectName(u"button_E")
        self.button_E.setEnabled(True)
        self.button_E.setFont(font4)

        self.gridLayout.addWidget(self.button_E, 0, 3, 1, 2)

        self.button_I = enigmaCipheringButton(self.centralwidget)
        self.button_I.setObjectName(u"button_I")
        self.button_I.setEnabled(True)
        self.button_I.setFont(font4)

        self.gridLayout.addWidget(self.button_I, 0, 13, 1, 2)

        self.button_N = enigmaCipheringButton(self.centralwidget)
        self.button_N.setObjectName(u"button_N")
        self.button_N.setFont(font4)

        self.gridLayout.addWidget(self.button_N, 2, 11, 1, 2)

        self.button_X = enigmaCipheringButton(self.centralwidget)
        self.button_X.setObjectName(u"button_X")
        self.button_X.setFont(font4)

        self.gridLayout.addWidget(self.button_X, 2, 3, 1, 2)

        self.button_Q = enigmaCipheringButton(self.centralwidget)
        self.button_Q.setObjectName(u"button_Q")
        self.button_Q.setEnabled(True)
        self.button_Q.setFont(font4)

        self.gridLayout.addWidget(self.button_Q, 0, 0, 1, 1)

        self.button_G = enigmaCipheringButton(self.centralwidget)
        self.button_G.setObjectName(u"button_G")
        self.button_G.setFont(font4)

        self.gridLayout.addWidget(self.button_G, 1, 8, 1, 2)

        self.button_S = enigmaCipheringButton(self.centralwidget)
        self.button_S.setObjectName(u"button_S")
        self.button_S.setFont(font4)

        self.gridLayout.addWidget(self.button_S, 1, 2, 1, 2)

        self.button_O = enigmaCipheringButton(self.centralwidget)
        self.button_O.setObjectName(u"button_O")
        self.button_O.setEnabled(True)
        self.button_O.setFont(font4)

        self.gridLayout.addWidget(self.button_O, 0, 15, 1, 1)

        self.button_P = enigmaCipheringButton(self.centralwidget)
        self.button_P.setObjectName(u"button_P")
        self.button_P.setFont(font4)

        self.gridLayout.addWidget(self.button_P, 2, 0, 1, 1)

        self.button_V = enigmaCipheringButton(self.centralwidget)
        self.button_V.setObjectName(u"button_V")
        self.button_V.setFont(font4)

        self.gridLayout.addWidget(self.button_V, 2, 7, 1, 2)

        self.button_M = enigmaCipheringButton(self.centralwidget)
        self.button_M.setObjectName(u"button_M")
        self.button_M.setFont(font4)

        self.gridLayout.addWidget(self.button_M, 2, 13, 1, 2)

        self.button_J = enigmaCipheringButton(self.centralwidget)
        self.button_J.setObjectName(u"button_J")
        self.button_J.setFont(font4)

        self.gridLayout.addWidget(self.button_J, 1, 12, 1, 2)

        self.button_W = enigmaCipheringButton(self.centralwidget)
        self.button_W.setObjectName(u"button_W")
        self.button_W.setEnabled(True)
        self.button_W.setFont(font4)

        self.gridLayout.addWidget(self.button_W, 0, 1, 1, 2)


        self.gridLayout_3.addLayout(self.gridLayout, 7, 0, 1, 9)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 4, 3, 1, 2)

        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")

        self.gridLayout_3.addWidget(self.clear_button, 1, 7, 1, 1)

        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")

        self.gridLayout_3.addWidget(self.reset_button, 0, 7, 1, 1)

        self.rotor_C_display = QLabel(self.centralwidget)
        self.rotor_C_display.setObjectName(u"rotor_C_display")
        self.rotor_C_display.setFont(font)
        self.rotor_C_display.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rotor_C_display, 0, 1, 3, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1116, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.rotor_B_display.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.rotor_A_display.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.rotor_C_advance.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.rotor_A_advance.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.rotor_B_regress.setText(QCoreApplication.translate("MainWindow", u"\u2304", None))
        self.lamp_W.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.lamp_V.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lamp_N.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.lamp_E.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.lamp_R.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lamp_O.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.lamp_P.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.lamp_I.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.lamp_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.lamp_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.lamp_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lamp_T.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.lamp_L.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.lamp_Q.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.lamp_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.lamp_Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.lamp_F.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.lamp_U.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.lamp_K.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.lamp_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lamp_D.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.lamp_G.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lamp_J.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.lamp_H.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.lamp_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lamp_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rotor positions:", None))
        self.rotor_A_regress.setText(QCoreApplication.translate("MainWindow", u"\u2304", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ciphertext", None))
        self.rotor_C_regress.setText(QCoreApplication.translate("MainWindow", u"\u2304", None))
        self.config_box.setTitle(QCoreApplication.translate("MainWindow", u"Current configuration:", None))
        self.rotor_A_wiring.setText(QCoreApplication.translate("MainWindow", u"RotorA wiring:", None))
        self.rotor_B_wiring.setText(QCoreApplication.translate("MainWindow", u"RotorB wiring:", None))
        self.rotor_C_wiring.setText(QCoreApplication.translate("MainWindow", u"RotorC wiring:", None))
        self.plugboard.setText(QCoreApplication.translate("MainWindow", u"Plugboard:", None))
        self.reflector_wiring.setText(QCoreApplication.translate("MainWindow", u"Reflector_wiring:", None))
        self.rotor_A_turnover.setText(QCoreApplication.translate("MainWindow", u"RotorA turnover:", None))
        self.rotor_B_turnover.setText(QCoreApplication.translate("MainWindow", u"RotorB turnover:", None))
        self.rotor_C_turnover.setText(QCoreApplication.translate("MainWindow", u"RotorC turnover:", None))
        self.rotor_B_advance.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.button_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.button_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.button_H.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.button_Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.button_R.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.button_K.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.button_D.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.button_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.button_L.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.button_F.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.button_T.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.button_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.button_U.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.button_E.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.button_I.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.button_N.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.button_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.button_Q.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.button_G.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.button_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.button_O.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.button_P.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.button_V.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.button_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.button_J.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.button_W.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Plaintext", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.rotor_C_display.setText(QCoreApplication.translate("MainWindow", u"A", None))
    # retranslateUi

