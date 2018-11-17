# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WalletInfoForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_WalletInfoForm(object):
    def setupUi(self, WalletInfoForm):
        WalletInfoForm.setObjectName("WalletInfoForm")
        WalletInfoForm.resize(489, 437)
        WalletInfoForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QtWidgets.QLineEdit(WalletInfoForm)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 130, 371, 31))
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
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.line_38 = QtWidgets.QFrame(WalletInfoForm)
        self.line_38.setGeometry(QtCore.QRect(60, 160, 371, 16))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.lineEdit_7 = QtWidgets.QLineEdit(WalletInfoForm)
        self.lineEdit_7.setGeometry(QtCore.QRect(60, 260, 371, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setToolTip("")
        self.lineEdit_7.setStatusTip("")
        self.lineEdit_7.setWhatsThis("")
        self.lineEdit_7.setAccessibleName("")
        self.lineEdit_7.setAccessibleDescription("")
        self.lineEdit_7.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_7.setFrame(False)
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_51 = QtWidgets.QLabel(WalletInfoForm)
        self.label_51.setGeometry(QtCore.QRect(40, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_51.setObjectName("label_51")
        self.line_41 = QtWidgets.QFrame(WalletInfoForm)
        self.line_41.setGeometry(QtCore.QRect(60, 290, 371, 16))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.label_15 = QtWidgets.QLabel(WalletInfoForm)
        self.label_15.setGeometry(QtCore.QRect(10, 10, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(135, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.closeenterpsw = QtWidgets.QPushButton(WalletInfoForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(450, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.pushButton_9 = QtWidgets.QPushButton(WalletInfoForm)
        self.pushButton_9.setGeometry(QtCore.QRect(100, 340, 291, 51))
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
        self.label_52 = QtWidgets.QLabel(WalletInfoForm)
        self.label_52.setGeometry(QtCore.QRect(40, 90, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_52.setObjectName("label_52")

        self.retranslateUi(WalletInfoForm)
        QtCore.QMetaObject.connectSlotsByName(WalletInfoForm)

    def retranslateUi(self, WalletInfoForm):
        _translate = QtCore.QCoreApplication.translate
        WalletInfoForm.setWindowTitle(_translate("WalletInfoForm", "Form"))
        self.label_51.setText(_translate("WalletInfoForm", "Name:"))
        self.label_15.setText(_translate("WalletInfoForm", "Wallet Info"))
        self.pushButton_9.setText(_translate("WalletInfoForm", "Save"))
        self.label_52.setText(_translate("WalletInfoForm", "Address:"))

import pic_rc
