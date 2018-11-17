# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RecieveForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ReceiveForm(object):
    def setupUi(self, ReceiveForm):
        ReceiveForm.setObjectName("ReceiveForm")
        ReceiveForm.resize(540, 537)
        ReceiveForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_6 = QtWidgets.QLineEdit(ReceiveForm)
        self.lineEdit_6.setGeometry(QtCore.QRect(180, 50, 261, 31))
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
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_7 = QtWidgets.QLabel(ReceiveForm)
        self.label_7.setGeometry(QtCore.QRect(450, 60, 51, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.line_38 = QtWidgets.QFrame(ReceiveForm)
        self.line_38.setGeometry(QtCore.QRect(180, 90, 271, 10))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.label_15 = QtWidgets.QLabel(ReceiveForm)
        self.label_15.setGeometry(QtCore.QRect(30, 40, 121, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(135, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.closeenterpsw = QtWidgets.QPushButton(ReceiveForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(500, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.label = QtWidgets.QLabel(ReceiveForm)
        self.label.setGeometry(QtCore.QRect(140, 140, 251, 231))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_8 = QtWidgets.QLineEdit(ReceiveForm)
        self.lineEdit_8.setGeometry(QtCore.QRect(60, 440, 431, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("border:0px;\n"
"border-radius:20px;\n"
"\n"
"background-color: rgb(230, 238, 255);")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_34 = QtWidgets.QPushButton(ReceiveForm)
        self.pushButton_34.setGeometry(QtCore.QRect(450, 440, 41, 41))
        self.pushButton_34.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_34.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_34.setAutoFillBackground(False)
        self.pushButton_34.setStyleSheet("border:0px;")
        self.pushButton_34.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/purplecopy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_34.setIcon(icon1)
        self.pushButton_34.setIconSize(QtCore.QSize(77, 77))
        self.pushButton_34.setAutoDefault(False)
        self.pushButton_34.setFlat(True)
        self.pushButton_34.setObjectName("pushButton_34")
        self.label_8 = QtWidgets.QLabel(ReceiveForm)
        self.label_8.setGeometry(QtCore.QRect(170, 400, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.retranslateUi(ReceiveForm)
        QtCore.QMetaObject.connectSlotsByName(ReceiveForm)

    def retranslateUi(self, ReceiveForm):
        _translate = QtCore.QCoreApplication.translate
        ReceiveForm.setWindowTitle(_translate("ReceiveForm", "Form"))
        self.lineEdit_6.setPlaceholderText(_translate("ReceiveForm", "Enter Account"))
        self.label_7.setText(_translate("ReceiveForm", "WTCT"))
        self.label_15.setText(_translate("ReceiveForm", "Recieve"))
        self.label_8.setText(_translate("ReceiveForm", "Your Public Address"))

import pic_rc
