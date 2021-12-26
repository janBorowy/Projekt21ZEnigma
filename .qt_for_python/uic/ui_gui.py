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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(879, 649)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setEnabled(True)
        self.layoutWidget.setGeometry(QRect(30, 450, 770, 121))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_A = QPushButton(self.layoutWidget)
        self.button_A.setObjectName(u"button_A")
        font = QFont()
        font.setPointSize(16)
        font.setItalic(False)
        self.button_A.setFont(font)

        self.gridLayout.addWidget(self.button_A, 1, 0, 1, 2)

        self.button_B = QPushButton(self.layoutWidget)
        self.button_B.setObjectName(u"button_B")
        self.button_B.setFont(font)

        self.gridLayout.addWidget(self.button_B, 2, 9, 1, 2)

        self.button_H = QPushButton(self.layoutWidget)
        self.button_H.setObjectName(u"button_H")
        self.button_H.setFont(font)

        self.gridLayout.addWidget(self.button_H, 1, 10, 1, 2)

        self.button_Z = QPushButton(self.layoutWidget)
        self.button_Z.setObjectName(u"button_Z")
        self.button_Z.setEnabled(True)
        self.button_Z.setFont(font)

        self.gridLayout.addWidget(self.button_Z, 0, 9, 1, 2)

        self.button_R = QPushButton(self.layoutWidget)
        self.button_R.setObjectName(u"button_R")
        self.button_R.setEnabled(True)
        self.button_R.setFont(font)

        self.gridLayout.addWidget(self.button_R, 0, 5, 1, 2)

        self.button_K = QPushButton(self.layoutWidget)
        self.button_K.setObjectName(u"button_K")
        self.button_K.setFont(font)

        self.gridLayout.addWidget(self.button_K, 1, 14, 1, 2)

        self.button_D = QPushButton(self.layoutWidget)
        self.button_D.setObjectName(u"button_D")
        self.button_D.setFont(font)

        self.gridLayout.addWidget(self.button_D, 1, 4, 1, 2)

        self.button_Y = QPushButton(self.layoutWidget)
        self.button_Y.setObjectName(u"button_Y")
        self.button_Y.setFont(font)

        self.gridLayout.addWidget(self.button_Y, 2, 1, 1, 2)

        self.button_L = QPushButton(self.layoutWidget)
        self.button_L.setObjectName(u"button_L")
        self.button_L.setFont(font)

        self.gridLayout.addWidget(self.button_L, 2, 15, 1, 1)

        self.button_F = QPushButton(self.layoutWidget)
        self.button_F.setObjectName(u"button_F")
        self.button_F.setFont(font)

        self.gridLayout.addWidget(self.button_F, 1, 6, 1, 2)

        self.button_T = QPushButton(self.layoutWidget)
        self.button_T.setObjectName(u"button_T")
        self.button_T.setEnabled(True)
        self.button_T.setFont(font)

        self.gridLayout.addWidget(self.button_T, 0, 7, 1, 2)

        self.button_C = QPushButton(self.layoutWidget)
        self.button_C.setObjectName(u"button_C")
        self.button_C.setFont(font)

        self.gridLayout.addWidget(self.button_C, 2, 5, 1, 2)

        self.button_U = QPushButton(self.layoutWidget)
        self.button_U.setObjectName(u"button_U")
        self.button_U.setEnabled(True)
        self.button_U.setFont(font)

        self.gridLayout.addWidget(self.button_U, 0, 11, 1, 2)

        self.button_E = QPushButton(self.layoutWidget)
        self.button_E.setObjectName(u"button_E")
        self.button_E.setEnabled(True)
        self.button_E.setFont(font)

        self.gridLayout.addWidget(self.button_E, 0, 3, 1, 2)

        self.button_I = QPushButton(self.layoutWidget)
        self.button_I.setObjectName(u"button_I")
        self.button_I.setEnabled(True)
        self.button_I.setFont(font)

        self.gridLayout.addWidget(self.button_I, 0, 13, 1, 2)

        self.button_N = QPushButton(self.layoutWidget)
        self.button_N.setObjectName(u"button_N")
        self.button_N.setFont(font)

        self.gridLayout.addWidget(self.button_N, 2, 11, 1, 2)

        self.button_X = QPushButton(self.layoutWidget)
        self.button_X.setObjectName(u"button_X")
        self.button_X.setFont(font)

        self.gridLayout.addWidget(self.button_X, 2, 3, 1, 2)

        self.button_Q = QPushButton(self.layoutWidget)
        self.button_Q.setObjectName(u"button_Q")
        self.button_Q.setEnabled(True)
        self.button_Q.setFont(font)

        self.gridLayout.addWidget(self.button_Q, 0, 0, 1, 1)

        self.button_G = QPushButton(self.layoutWidget)
        self.button_G.setObjectName(u"button_G")
        self.button_G.setFont(font)

        self.gridLayout.addWidget(self.button_G, 1, 8, 1, 2)

        self.button_S = QPushButton(self.layoutWidget)
        self.button_S.setObjectName(u"button_S")
        self.button_S.setFont(font)

        self.gridLayout.addWidget(self.button_S, 1, 2, 1, 2)

        self.button_O = QPushButton(self.layoutWidget)
        self.button_O.setObjectName(u"button_O")
        self.button_O.setEnabled(True)
        self.button_O.setFont(font)

        self.gridLayout.addWidget(self.button_O, 0, 15, 1, 1)

        self.button_P = QPushButton(self.layoutWidget)
        self.button_P.setObjectName(u"button_P")
        self.button_P.setFont(font)

        self.gridLayout.addWidget(self.button_P, 2, 0, 1, 1)

        self.button_V = QPushButton(self.layoutWidget)
        self.button_V.setObjectName(u"button_V")
        self.button_V.setFont(font)

        self.gridLayout.addWidget(self.button_V, 2, 7, 1, 2)

        self.button_M = QPushButton(self.layoutWidget)
        self.button_M.setObjectName(u"button_M")
        self.button_M.setFont(font)

        self.gridLayout.addWidget(self.button_M, 2, 13, 1, 2)

        self.button_J = QPushButton(self.layoutWidget)
        self.button_J.setObjectName(u"button_J")
        self.button_J.setFont(font)

        self.gridLayout.addWidget(self.button_J, 1, 12, 1, 2)

        self.button_W = QPushButton(self.layoutWidget)
        self.button_W.setObjectName(u"button_W")
        self.button_W.setEnabled(True)
        self.button_W.setFont(font)

        self.gridLayout.addWidget(self.button_W, 0, 1, 1, 2)

        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(30, 20, 80, 23))
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 50, 531, 194))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.CipherTextBrowser = QTextBrowser(self.layoutWidget1)
        self.CipherTextBrowser.setObjectName(u"CipherTextBrowser")

        self.horizontalLayout.addWidget(self.CipherTextBrowser)

        self.PlainTextBrowser = QTextBrowser(self.layoutWidget1)
        self.PlainTextBrowser.setObjectName(u"PlainTextBrowser")

        self.horizontalLayout.addWidget(self.PlainTextBrowser)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 879, 20))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"clear", None))
    # retranslateUi

