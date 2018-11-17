# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qt_ui\PswForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PswForm(object):
    def setupUi(self, PswForm):
        PswForm.setObjectName("PswForm")
        PswForm.resize(467, 230)
        PswForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_15 = QtWidgets.QLabel(PswForm)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 331, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(135, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.closeenterpsw = QtWidgets.QPushButton(PswForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(430, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.pushButton_9 = QtWidgets.QPushButton(PswForm)
        self.pushButton_9.setGeometry(QtCore.QRect(70, 160, 141, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setStyleSheet("background-color: rgb(135, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(PswForm)
        self.pushButton_10.setGeometry(QtCore.QRect(260, 160, 141, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(135, 0, 255);\n"
"border-width:1px;\n"
"border-style:solid; \n"
"color: rgb(135, 0, 255);\n"
"border-radius:25px;")
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.line_33 = QtWidgets.QFrame(PswForm)
        self.line_33.setGeometry(QtCore.QRect(20, 130, 431, 10))
        self.line_33.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_33.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_33.setObjectName("line_33")
        self.turn2visible1_2 = QtWidgets.QPushButton(PswForm)
        self.turn2visible1_2.setGeometry(QtCore.QRect(410, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.turn2visible1_2.setFont(font)
        self.turn2visible1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.turn2visible1_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.turn2visible1_2.setAutoFillBackground(False)
        self.turn2visible1_2.setStyleSheet("border:0px;")
        self.turn2visible1_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.turn2visible1_2.setIcon(icon1)
        self.turn2visible1_2.setIconSize(QtCore.QSize(40, 40))
        self.turn2visible1_2.setFlat(True)
        self.turn2visible1_2.setObjectName("turn2visible1_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(PswForm)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 100, 381, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setToolTip("")
        self.lineEdit_6.setStatusTip("")
        self.lineEdit_6.setWhatsThis("")
        self.lineEdit_6.setAccessibleName("")
        self.lineEdit_6.setAccessibleDescription("")
        self.lineEdit_6.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(PswForm)
        QtCore.QMetaObject.connectSlotsByName(PswForm)

    def retranslateUi(self, PswForm):
        _translate = QtCore.QCoreApplication.translate
        PswForm.setWindowTitle(_translate("PswForm", "Form"))
        self.label_15.setText(_translate("PswForm", "Enter Login Password"))
        self.pushButton_9.setText(_translate("PswForm", "Confirm"))
        self.pushButton_10.setText(_translate("PswForm", "Quit"))
        self.lineEdit_6.setPlaceholderText(_translate("PswForm", "Enter Password Here"))

import pic_rc
