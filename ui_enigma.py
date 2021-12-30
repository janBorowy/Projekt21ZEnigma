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
        MainWindow.resize(1117, 768)
        MainWindow.setMinimumSize(QSize(300, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.action_open = QAction(MainWindow)
        self.action_open.setObjectName(u"action_open")
        self.action_save_as = QAction(MainWindow)
        self.action_save_as.setObjectName(u"action_save_as")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, 0, -1)
        self.button_G = enigmaCipheringButton(self.centralwidget)
        self.button_G.setObjectName(u"button_G")
        font = QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.button_G.setFont(font)

        self.gridLayout.addWidget(self.button_G, 1, 10, 1, 2)

        self.button_K = enigmaCipheringButton(self.centralwidget)
        self.button_K.setObjectName(u"button_K")
        self.button_K.setFont(font)

        self.gridLayout.addWidget(self.button_K, 1, 16, 1, 2)

        self.button_R = enigmaCipheringButton(self.centralwidget)
        self.button_R.setObjectName(u"button_R")
        self.button_R.setEnabled(True)
        self.button_R.setFont(font)

        self.gridLayout.addWidget(self.button_R, 0, 7, 1, 2)

        self.button_F = enigmaCipheringButton(self.centralwidget)
        self.button_F.setObjectName(u"button_F")
        self.button_F.setFont(font)

        self.gridLayout.addWidget(self.button_F, 1, 8, 1, 2)

        self.button_C = enigmaCipheringButton(self.centralwidget)
        self.button_C.setObjectName(u"button_C")
        self.button_C.setFont(font)

        self.gridLayout.addWidget(self.button_C, 2, 7, 1, 2)

        self.button_D = enigmaCipheringButton(self.centralwidget)
        self.button_D.setObjectName(u"button_D")
        self.button_D.setFont(font)

        self.gridLayout.addWidget(self.button_D, 1, 6, 1, 2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_8, 2, 19, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_10, 2, 0, 1, 1)

        self.button_S = enigmaCipheringButton(self.centralwidget)
        self.button_S.setObjectName(u"button_S")
        self.button_S.setFont(font)

        self.gridLayout.addWidget(self.button_S, 1, 4, 1, 2)

        self.button_P = enigmaCipheringButton(self.centralwidget)
        self.button_P.setObjectName(u"button_P")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_P.sizePolicy().hasHeightForWidth())
        self.button_P.setSizePolicy(sizePolicy)
        self.button_P.setMaximumSize(QSize(16777215, 16777215))
        self.button_P.setFont(font)

        self.gridLayout.addWidget(self.button_P, 2, 1, 1, 2)

        self.button_E = enigmaCipheringButton(self.centralwidget)
        self.button_E.setObjectName(u"button_E")
        self.button_E.setEnabled(True)
        self.button_E.setFont(font)

        self.gridLayout.addWidget(self.button_E, 0, 5, 1, 2)

        self.button_Q = enigmaCipheringButton(self.centralwidget)
        self.button_Q.setObjectName(u"button_Q")
        self.button_Q.setEnabled(True)
        sizePolicy.setHeightForWidth(self.button_Q.sizePolicy().hasHeightForWidth())
        self.button_Q.setSizePolicy(sizePolicy)
        self.button_Q.setMaximumSize(QSize(16777215, 16777215))
        self.button_Q.setFont(font)

        self.gridLayout.addWidget(self.button_Q, 0, 1, 1, 2)

        self.button_Z = enigmaCipheringButton(self.centralwidget)
        self.button_Z.setObjectName(u"button_Z")
        self.button_Z.setEnabled(True)
        self.button_Z.setFont(font)

        self.gridLayout.addWidget(self.button_Z, 0, 11, 1, 2)

        self.button_H = enigmaCipheringButton(self.centralwidget)
        self.button_H.setObjectName(u"button_H")
        self.button_H.setFont(font)

        self.gridLayout.addWidget(self.button_H, 1, 12, 1, 2)

        self.button_U = enigmaCipheringButton(self.centralwidget)
        self.button_U.setObjectName(u"button_U")
        self.button_U.setEnabled(True)
        self.button_U.setFont(font)

        self.gridLayout.addWidget(self.button_U, 0, 13, 1, 2)

        self.button_A = enigmaCipheringButton(self.centralwidget)
        self.button_A.setObjectName(u"button_A")
        self.button_A.setFont(font)

        self.gridLayout.addWidget(self.button_A, 1, 2, 1, 2)

        self.button_I = enigmaCipheringButton(self.centralwidget)
        self.button_I.setObjectName(u"button_I")
        self.button_I.setEnabled(True)
        self.button_I.setMaximumSize(QSize(16777215, 16777215))
        self.button_I.setFont(font)

        self.gridLayout.addWidget(self.button_I, 0, 15, 1, 2)

        self.button_O = enigmaCipheringButton(self.centralwidget)
        self.button_O.setObjectName(u"button_O")
        self.button_O.setEnabled(True)
        self.button_O.setMaximumSize(QSize(100, 16777215))
        self.button_O.setFont(font)

        self.gridLayout.addWidget(self.button_O, 0, 17, 1, 2)

        self.button_V = enigmaCipheringButton(self.centralwidget)
        self.button_V.setObjectName(u"button_V")
        self.button_V.setFont(font)

        self.gridLayout.addWidget(self.button_V, 2, 9, 1, 2)

        self.button_N = enigmaCipheringButton(self.centralwidget)
        self.button_N.setObjectName(u"button_N")
        self.button_N.setFont(font)

        self.gridLayout.addWidget(self.button_N, 2, 13, 1, 2)

        self.button_Y = enigmaCipheringButton(self.centralwidget)
        self.button_Y.setObjectName(u"button_Y")
        self.button_Y.setFont(font)

        self.gridLayout.addWidget(self.button_Y, 2, 3, 1, 2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 0, 19, 1, 1)

        self.button_X = enigmaCipheringButton(self.centralwidget)
        self.button_X.setObjectName(u"button_X")
        self.button_X.setFont(font)

        self.gridLayout.addWidget(self.button_X, 2, 5, 1, 2)

        self.button_B = enigmaCipheringButton(self.centralwidget)
        self.button_B.setObjectName(u"button_B")
        self.button_B.setFont(font)

        self.gridLayout.addWidget(self.button_B, 2, 11, 1, 2)

        self.button_L = enigmaCipheringButton(self.centralwidget)
        self.button_L.setObjectName(u"button_L")
        self.button_L.setMaximumSize(QSize(100, 16777215))
        self.button_L.setFont(font)

        self.gridLayout.addWidget(self.button_L, 2, 17, 1, 2)

        self.button_T = enigmaCipheringButton(self.centralwidget)
        self.button_T.setObjectName(u"button_T")
        self.button_T.setEnabled(True)
        self.button_T.setFont(font)

        self.gridLayout.addWidget(self.button_T, 0, 9, 1, 2)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 0, 0, 1, 1)

        self.button_J = enigmaCipheringButton(self.centralwidget)
        self.button_J.setObjectName(u"button_J")
        self.button_J.setFont(font)

        self.gridLayout.addWidget(self.button_J, 1, 14, 1, 2)

        self.button_W = enigmaCipheringButton(self.centralwidget)
        self.button_W.setObjectName(u"button_W")
        self.button_W.setEnabled(True)
        self.button_W.setFont(font)

        self.gridLayout.addWidget(self.button_W, 0, 3, 1, 2)

        self.button_M = enigmaCipheringButton(self.centralwidget)
        self.button_M.setObjectName(u"button_M")
        self.button_M.setFont(font)

        self.gridLayout.addWidget(self.button_M, 2, 15, 1, 2)

        self.button_space = QPushButton(self.centralwidget)
        self.button_space.setObjectName(u"button_space")

        self.gridLayout.addWidget(self.button_space, 3, 5, 1, 10)


        self.gridLayout_5.addLayout(self.gridLayout, 6, 0, 1, 6)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setSizeConstraint(QLayout.SetFixedSize)
        self.ring_setting_B_advance = QPushButton(self.centralwidget)
        self.ring_setting_B_advance.setObjectName(u"ring_setting_B_advance")
        self.ring_setting_B_advance.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.ring_setting_B_advance, 0, 16, 1, 1)

        self.rotor_B_regress = QPushButton(self.centralwidget)
        self.rotor_B_regress.setObjectName(u"rotor_B_regress")
        self.rotor_B_regress.setMaximumSize(QSize(20, 16777215))
        font1 = QFont()
        font1.setPointSize(12)
        self.rotor_B_regress.setFont(font1)

        self.gridLayout_3.addWidget(self.rotor_B_regress, 1, 18, 1, 1)

        self.ring_setting_A_advance = QPushButton(self.centralwidget)
        self.ring_setting_A_advance.setObjectName(u"ring_setting_A_advance")
        self.ring_setting_A_advance.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.ring_setting_A_advance, 0, 26, 1, 1)

        self.ring_setting_A = QLabel(self.centralwidget)
        self.ring_setting_A.setObjectName(u"ring_setting_A")
        self.ring_setting_A.setMinimumSize(QSize(100, 0))
        self.ring_setting_A.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.ring_setting_A, 0, 20, 1, 5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 10, 1, 7)

        self.ring_setting_C_advance = QPushButton(self.centralwidget)
        self.ring_setting_C_advance.setObjectName(u"ring_setting_C_advance")
        self.ring_setting_C_advance.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.ring_setting_C_advance, 0, 6, 1, 1)

        self.rotor_A_display = QLabel(self.centralwidget)
        self.rotor_A_display.setObjectName(u"rotor_A_display")
        self.rotor_A_display.setMinimumSize(QSize(75, 0))
        self.rotor_A_display.setMaximumSize(QSize(75, 16777215))
        font2 = QFont()
        font2.setPointSize(48)
        self.rotor_A_display.setFont(font2)
        self.rotor_A_display.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rotor_A_display, 0, 27, 2, 1)

        self.rotor_A_regress = QPushButton(self.centralwidget)
        self.rotor_A_regress.setObjectName(u"rotor_A_regress")
        self.rotor_A_regress.setMaximumSize(QSize(20, 16777215))
        self.rotor_A_regress.setFont(font1)

        self.gridLayout_3.addWidget(self.rotor_A_regress, 1, 28, 1, 1)

        self.ring_setting_C_regress = QPushButton(self.centralwidget)
        self.ring_setting_C_regress.setObjectName(u"ring_setting_C_regress")
        self.ring_setting_C_regress.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.ring_setting_C_regress, 0, 5, 1, 1)

        self.rotor_C_regress = QPushButton(self.centralwidget)
        self.rotor_C_regress.setObjectName(u"rotor_C_regress")
        self.rotor_C_regress.setMaximumSize(QSize(20, 16777215))
        self.rotor_C_regress.setFont(font1)

        self.gridLayout_3.addWidget(self.rotor_C_regress, 1, 8, 1, 1)

        self.ring_setting_B = QLabel(self.centralwidget)
        self.ring_setting_B.setObjectName(u"ring_setting_B")
        self.ring_setting_B.setMinimumSize(QSize(100, 0))
        self.ring_setting_B.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.ring_setting_B, 0, 10, 1, 5)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_15, 0, 9, 1, 1)

        self.ring_setting_A_regress = QPushButton(self.centralwidget)
        self.ring_setting_A_regress.setObjectName(u"ring_setting_A_regress")
        self.ring_setting_A_regress.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.ring_setting_A_regress, 0, 25, 1, 1)

        self.rotor_B_advance = QPushButton(self.centralwidget)
        self.rotor_B_advance.setObjectName(u"rotor_B_advance")
        self.rotor_B_advance.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_3.addWidget(self.rotor_B_advance, 0, 18, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 20, 1, 7)

        self.rotor_C_display = QLabel(self.centralwidget)
        self.rotor_C_display.setObjectName(u"rotor_C_display")
        self.rotor_C_display.setMinimumSize(QSize(75, 0))
        self.rotor_C_display.setMaximumSize(QSize(75, 16777215))
        self.rotor_C_display.setFont(font2)
        self.rotor_C_display.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rotor_C_display, 0, 7, 2, 1)

        self.rotor_A_advance = QPushButton(self.centralwidget)
        self.rotor_A_advance.setObjectName(u"rotor_A_advance")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.rotor_A_advance.sizePolicy().hasHeightForWidth())
        self.rotor_A_advance.setSizePolicy(sizePolicy1)
        self.rotor_A_advance.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_3.addWidget(self.rotor_A_advance, 0, 28, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_17, 0, 29, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 1, 0, 1, 7)

        self.rotor_C_advance = QPushButton(self.centralwidget)
        self.rotor_C_advance.setObjectName(u"rotor_C_advance")
        self.rotor_C_advance.setMaximumSize(QSize(20, 16777215))

        self.gridLayout_3.addWidget(self.rotor_C_advance, 0, 8, 1, 1)

        self.ring_setting_B_regress = QPushButton(self.centralwidget)
        self.ring_setting_B_regress.setObjectName(u"ring_setting_B_regress")
        self.ring_setting_B_regress.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_3.addWidget(self.ring_setting_B_regress, 0, 15, 1, 1)

        self.rotor_B_display = QLabel(self.centralwidget)
        self.rotor_B_display.setObjectName(u"rotor_B_display")
        self.rotor_B_display.setMinimumSize(QSize(75, 0))
        self.rotor_B_display.setMaximumSize(QSize(75, 16777215))
        self.rotor_B_display.setFont(font2)
        self.rotor_B_display.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.rotor_B_display, 0, 17, 2, 1)

        self.ring_setting_C = QLabel(self.centralwidget)
        self.ring_setting_C.setObjectName(u"ring_setting_C")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ring_setting_C.sizePolicy().hasHeightForWidth())
        self.ring_setting_C.setSizePolicy(sizePolicy2)
        self.ring_setting_C.setMinimumSize(QSize(100, 0))
        self.ring_setting_C.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_3.addWidget(self.ring_setting_C, 0, 0, 1, 5)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_16, 0, 19, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 1, 0, 1, 6)

        self.gridLayout_7 = QHBoxLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.CipherTextBrowser = QTextBrowser(self.centralwidget)
        self.CipherTextBrowser.setObjectName(u"CipherTextBrowser")
        font3 = QFont()
        font3.setPointSize(18)
        self.CipherTextBrowser.setFont(font3)

        self.gridLayout_7.addWidget(self.CipherTextBrowser)

        self.PlainTextBrowser = QTextBrowser(self.centralwidget)
        self.PlainTextBrowser.setObjectName(u"PlainTextBrowser")
        self.PlainTextBrowser.setFont(font3)

        self.gridLayout_7.addWidget(self.PlainTextBrowser)


        self.gridLayout_5.addLayout(self.gridLayout_7, 3, 0, 2, 6)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.verticalSpacer_2, 4, 6, 1, 2)

        self.reset_button = QPushButton(self.centralwidget)
        self.reset_button.setObjectName(u"reset_button")
        self.reset_button.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_5.addWidget(self.reset_button, 2, 5, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_11, 2, 1, 1, 1)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(200, 0))
        self.label.setMaximumSize(QSize(16777215, 20))
        font4 = QFont()
        font4.setPointSize(16)
        self.label.setFont(font4)

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.config_box = QGroupBox(self.centralwidget)
        self.config_box.setObjectName(u"config_box")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.config_box.sizePolicy().hasHeightForWidth())
        self.config_box.setSizePolicy(sizePolicy3)
        self.config_box.setMinimumSize(QSize(250, 250))
        self.config_box.setMaximumSize(QSize(16777215, 300))
        self.gridLayout_4 = QGridLayout(self.config_box)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.rotor_A_turnover = QLabel(self.config_box)
        self.rotor_A_turnover.setObjectName(u"rotor_A_turnover")
        self.rotor_A_turnover.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.rotor_A_turnover, 5, 0, 1, 1)

        self.rotor_A_wiring = QLabel(self.config_box)
        self.rotor_A_wiring.setObjectName(u"rotor_A_wiring")
        self.rotor_A_wiring.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.rotor_A_wiring, 1, 0, 1, 1)

        self.rotor_C_turnover = QLabel(self.config_box)
        self.rotor_C_turnover.setObjectName(u"rotor_C_turnover")
        self.rotor_C_turnover.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.rotor_C_turnover, 7, 0, 1, 1)

        self.reflector_wiring = QLabel(self.config_box)
        self.reflector_wiring.setObjectName(u"reflector_wiring")
        self.reflector_wiring.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.reflector_wiring, 8, 0, 1, 1)

        self.rotor_B_turnover = QLabel(self.config_box)
        self.rotor_B_turnover.setObjectName(u"rotor_B_turnover")
        self.rotor_B_turnover.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.rotor_B_turnover, 6, 0, 1, 1)

        self.plugboard = QLabel(self.config_box)
        self.plugboard.setObjectName(u"plugboard")
        self.plugboard.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.plugboard, 9, 0, 1, 1)

        self.rotor_C_wiring = QLabel(self.config_box)
        self.rotor_C_wiring.setObjectName(u"rotor_C_wiring")
        self.rotor_C_wiring.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.rotor_C_wiring, 4, 0, 1, 1)

        self.rotor_B_wiring = QLabel(self.config_box)
        self.rotor_B_wiring.setObjectName(u"rotor_B_wiring")
        self.rotor_B_wiring.setMinimumSize(QSize(0, 30))

        self.gridLayout_4.addWidget(self.rotor_B_wiring, 2, 0, 1, 1)


        self.gridLayout_5.addWidget(self.config_box, 2, 6, 2, 2)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_6, 5, 6, 1, 2)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 2, 2, 1, 1)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_12, 2, 3, 1, 1)

        self.clear_button = QPushButton(self.centralwidget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_5.addWidget(self.clear_button, 2, 4, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lamp_Q = enigmaLamp(self.centralwidget)
        self.lamp_Q.setObjectName(u"lamp_Q")
        self.lamp_Q.setMinimumSize(QSize(30, 0))
        font5 = QFont()
        font5.setPointSize(20)
        self.lamp_Q.setFont(font5)
        self.lamp_Q.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_Q, 0, 0, 1, 1)

        self.lamp_V = enigmaLamp(self.centralwidget)
        self.lamp_V.setObjectName(u"lamp_V")
        self.lamp_V.setMinimumSize(QSize(30, 0))
        self.lamp_V.setFont(font5)
        self.lamp_V.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_V, 2, 8, 1, 1)

        self.lamp_C = enigmaLamp(self.centralwidget)
        self.lamp_C.setObjectName(u"lamp_C")
        self.lamp_C.setMinimumSize(QSize(30, 0))
        self.lamp_C.setFont(font5)
        self.lamp_C.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_C, 2, 6, 1, 1)

        self.lamp_Y = enigmaLamp(self.centralwidget)
        self.lamp_Y.setObjectName(u"lamp_Y")
        self.lamp_Y.setMinimumSize(QSize(30, 0))
        self.lamp_Y.setFont(font5)
        self.lamp_Y.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_Y, 2, 2, 1, 1)

        self.lamp_M = enigmaLamp(self.centralwidget)
        self.lamp_M.setObjectName(u"lamp_M")
        self.lamp_M.setMinimumSize(QSize(30, 0))
        self.lamp_M.setFont(font5)
        self.lamp_M.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_M, 2, 14, 1, 1)

        self.lamp_K = enigmaLamp(self.centralwidget)
        self.lamp_K.setObjectName(u"lamp_K")
        self.lamp_K.setMinimumSize(QSize(30, 0))
        self.lamp_K.setFont(font5)
        self.lamp_K.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_K, 1, 15, 1, 1)

        self.lamp_R = enigmaLamp(self.centralwidget)
        self.lamp_R.setObjectName(u"lamp_R")
        self.lamp_R.setMinimumSize(QSize(30, 0))
        self.lamp_R.setFont(font5)
        self.lamp_R.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_R, 0, 6, 1, 1)

        self.lamp_U = enigmaLamp(self.centralwidget)
        self.lamp_U.setObjectName(u"lamp_U")
        self.lamp_U.setMinimumSize(QSize(30, 0))
        self.lamp_U.setFont(font5)
        self.lamp_U.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_U, 0, 12, 1, 1)

        self.lamp_E = enigmaLamp(self.centralwidget)
        self.lamp_E.setObjectName(u"lamp_E")
        self.lamp_E.setMinimumSize(QSize(30, 0))
        self.lamp_E.setFont(font5)
        self.lamp_E.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_E, 0, 4, 1, 1)

        self.lamp_S = enigmaLamp(self.centralwidget)
        self.lamp_S.setObjectName(u"lamp_S")
        self.lamp_S.setMinimumSize(QSize(30, 0))
        self.lamp_S.setFont(font5)
        self.lamp_S.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_S, 1, 3, 1, 1)

        self.lamp_I = enigmaLamp(self.centralwidget)
        self.lamp_I.setObjectName(u"lamp_I")
        self.lamp_I.setMinimumSize(QSize(30, 0))
        self.lamp_I.setFont(font5)
        self.lamp_I.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_I, 0, 14, 1, 1)

        self.lamp_P = enigmaLamp(self.centralwidget)
        self.lamp_P.setObjectName(u"lamp_P")
        self.lamp_P.setMinimumSize(QSize(30, 0))
        self.lamp_P.setFont(font5)
        self.lamp_P.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_P, 2, 0, 1, 1)

        self.lamp_A = enigmaLamp(self.centralwidget)
        self.lamp_A.setObjectName(u"lamp_A")
        self.lamp_A.setMinimumSize(QSize(30, 0))
        self.lamp_A.setFont(font5)
        self.lamp_A.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_A, 1, 1, 1, 1)

        self.lamp_J = enigmaLamp(self.centralwidget)
        self.lamp_J.setObjectName(u"lamp_J")
        self.lamp_J.setMinimumSize(QSize(30, 0))
        self.lamp_J.setFont(font5)
        self.lamp_J.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_J, 1, 13, 1, 1)

        self.lamp_H = enigmaLamp(self.centralwidget)
        self.lamp_H.setObjectName(u"lamp_H")
        self.lamp_H.setMinimumSize(QSize(30, 0))
        self.lamp_H.setFont(font5)
        self.lamp_H.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_H, 1, 11, 1, 1)

        self.lamp_X = enigmaLamp(self.centralwidget)
        self.lamp_X.setObjectName(u"lamp_X")
        self.lamp_X.setMinimumSize(QSize(30, 0))
        self.lamp_X.setFont(font5)
        self.lamp_X.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_X, 2, 4, 1, 1)

        self.lamp_L = enigmaLamp(self.centralwidget)
        self.lamp_L.setObjectName(u"lamp_L")
        self.lamp_L.setMinimumSize(QSize(30, 0))
        self.lamp_L.setFont(font5)
        self.lamp_L.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_L, 2, 16, 1, 1)

        self.lamp_T = enigmaLamp(self.centralwidget)
        self.lamp_T.setObjectName(u"lamp_T")
        self.lamp_T.setMinimumSize(QSize(30, 0))
        self.lamp_T.setFont(font5)
        self.lamp_T.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_T, 0, 8, 1, 1)

        self.lamp_D = enigmaLamp(self.centralwidget)
        self.lamp_D.setObjectName(u"lamp_D")
        self.lamp_D.setMinimumSize(QSize(30, 0))
        self.lamp_D.setFont(font5)
        self.lamp_D.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_D, 1, 5, 1, 1)

        self.lamp_W = enigmaLamp(self.centralwidget)
        self.lamp_W.setObjectName(u"lamp_W")
        self.lamp_W.setMinimumSize(QSize(30, 0))
        self.lamp_W.setFont(font5)
        self.lamp_W.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_W, 0, 2, 1, 1)

        self.lamp_O = enigmaLamp(self.centralwidget)
        self.lamp_O.setObjectName(u"lamp_O")
        self.lamp_O.setMinimumSize(QSize(30, 0))
        self.lamp_O.setMaximumSize(QSize(30, 16777215))
        self.lamp_O.setFont(font5)
        self.lamp_O.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_O, 0, 16, 1, 1)

        self.lamp_G = enigmaLamp(self.centralwidget)
        self.lamp_G.setObjectName(u"lamp_G")
        self.lamp_G.setMinimumSize(QSize(30, 0))
        self.lamp_G.setFont(font5)
        self.lamp_G.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_G, 1, 9, 1, 1)

        self.lamp_B = enigmaLamp(self.centralwidget)
        self.lamp_B.setObjectName(u"lamp_B")
        self.lamp_B.setMinimumSize(QSize(30, 0))
        self.lamp_B.setFont(font5)
        self.lamp_B.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_B, 2, 10, 1, 1)

        self.lamp_F = enigmaLamp(self.centralwidget)
        self.lamp_F.setObjectName(u"lamp_F")
        self.lamp_F.setMinimumSize(QSize(30, 0))
        self.lamp_F.setFont(font5)
        self.lamp_F.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_F, 1, 7, 1, 1)

        self.lamp_N = enigmaLamp(self.centralwidget)
        self.lamp_N.setObjectName(u"lamp_N")
        self.lamp_N.setMinimumSize(QSize(30, 0))
        self.lamp_N.setFont(font5)
        self.lamp_N.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_N, 2, 12, 1, 1)

        self.lamp_Z = enigmaLamp(self.centralwidget)
        self.lamp_Z.setObjectName(u"lamp_Z")
        self.lamp_Z.setMinimumSize(QSize(30, 0))
        self.lamp_Z.setFont(font5)
        self.lamp_Z.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lamp_Z, 0, 10, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 5, 0, 1, 6)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_5, 6, 6, 1, 2)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1117, 20))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_save_as)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.action_open.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.action_save_as.setText(QCoreApplication.translate("MainWindow", u"Save as...", None))
        self.button_G.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.button_K.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.button_R.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.button_F.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.button_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.button_D.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.button_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.button_P.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.button_E.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.button_Q.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.button_Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.button_H.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.button_U.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.button_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.button_I.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.button_O.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.button_V.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.button_N.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.button_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.button_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.button_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.button_L.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.button_T.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.button_J.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.button_W.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.button_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.button_space.setText(QCoreApplication.translate("MainWindow", u"___", None))
        self.ring_setting_B_advance.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.rotor_B_regress.setText(QCoreApplication.translate("MainWindow", u"\u2304", None))
        self.ring_setting_A_advance.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.ring_setting_A.setText(QCoreApplication.translate("MainWindow", u"Ring setting:", None))
        self.ring_setting_C_advance.setText(QCoreApplication.translate("MainWindow", u">>", None))
        self.rotor_A_display.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.rotor_A_regress.setText(QCoreApplication.translate("MainWindow", u"\u2304", None))
        self.ring_setting_C_regress.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.rotor_C_regress.setText(QCoreApplication.translate("MainWindow", u"\u2304", None))
        self.ring_setting_B.setText(QCoreApplication.translate("MainWindow", u"Ring setting:", None))
        self.ring_setting_A_regress.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.rotor_B_advance.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.rotor_C_display.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.rotor_A_advance.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.rotor_C_advance.setText(QCoreApplication.translate("MainWindow", u"^", None))
        self.ring_setting_B_regress.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.rotor_B_display.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.ring_setting_C.setText(QCoreApplication.translate("MainWindow", u"Ring setting: ", None))
        self.reset_button.setText(QCoreApplication.translate("MainWindow", u"reset", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Ciphertext", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Rotor positions:", None))
        self.config_box.setTitle(QCoreApplication.translate("MainWindow", u"Current configuration:", None))
        self.rotor_A_turnover.setText(QCoreApplication.translate("MainWindow", u"RotorA turnover:", None))
        self.rotor_A_wiring.setText(QCoreApplication.translate("MainWindow", u"RotorA wiring:", None))
        self.rotor_C_turnover.setText(QCoreApplication.translate("MainWindow", u"RotorC turnover:", None))
        self.reflector_wiring.setText(QCoreApplication.translate("MainWindow", u"Reflector_wiring:", None))
        self.rotor_B_turnover.setText(QCoreApplication.translate("MainWindow", u"RotorB turnover:", None))
        self.plugboard.setText(QCoreApplication.translate("MainWindow", u"Plugboard:", None))
        self.rotor_C_wiring.setText(QCoreApplication.translate("MainWindow", u"RotorC wiring:", None))
        self.rotor_B_wiring.setText(QCoreApplication.translate("MainWindow", u"RotorB wiring:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Plaintext", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"clear", None))
        self.lamp_Q.setText(QCoreApplication.translate("MainWindow", u"Q", None))
        self.lamp_V.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.lamp_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.lamp_Y.setText(QCoreApplication.translate("MainWindow", u"Y", None))
        self.lamp_M.setText(QCoreApplication.translate("MainWindow", u"M", None))
        self.lamp_K.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.lamp_R.setText(QCoreApplication.translate("MainWindow", u"R", None))
        self.lamp_U.setText(QCoreApplication.translate("MainWindow", u"U", None))
        self.lamp_E.setText(QCoreApplication.translate("MainWindow", u"E", None))
        self.lamp_S.setText(QCoreApplication.translate("MainWindow", u"S", None))
        self.lamp_I.setText(QCoreApplication.translate("MainWindow", u"I", None))
        self.lamp_P.setText(QCoreApplication.translate("MainWindow", u"P", None))
        self.lamp_A.setText(QCoreApplication.translate("MainWindow", u"A", None))
        self.lamp_J.setText(QCoreApplication.translate("MainWindow", u"J", None))
        self.lamp_H.setText(QCoreApplication.translate("MainWindow", u"H", None))
        self.lamp_X.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lamp_L.setText(QCoreApplication.translate("MainWindow", u"L", None))
        self.lamp_T.setText(QCoreApplication.translate("MainWindow", u"T", None))
        self.lamp_D.setText(QCoreApplication.translate("MainWindow", u"D", None))
        self.lamp_W.setText(QCoreApplication.translate("MainWindow", u"W", None))
        self.lamp_O.setText(QCoreApplication.translate("MainWindow", u"O", None))
        self.lamp_G.setText(QCoreApplication.translate("MainWindow", u"G", None))
        self.lamp_B.setText(QCoreApplication.translate("MainWindow", u"B", None))
        self.lamp_F.setText(QCoreApplication.translate("MainWindow", u"F", None))
        self.lamp_N.setText(QCoreApplication.translate("MainWindow", u"N", None))
        self.lamp_Z.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi

