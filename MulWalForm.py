# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MulWalForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MulWalForm(object):
    def setupUi(self, MulWalForm):
        MulWalForm.setObjectName("MulWalForm")
        MulWalForm.resize(463, 444)
        MulWalForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_51 = QtWidgets.QLabel(MulWalForm)
        self.label_51.setGeometry(QtCore.QRect(30, 240, 121, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_51.setObjectName("label_51")
        self.line_38 = QtWidgets.QFrame(MulWalForm)
        self.line_38.setGeometry(QtCore.QRect(50, 190, 371, 16))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.lineEdit_7 = QtWidgets.QLineEdit(MulWalForm)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 280, 371, 31))
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
        self.label_15 = QtWidgets.QLabel(MulWalForm)
        self.label_15.setGeometry(QtCore.QRect(30, 30, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(135, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.label_52 = QtWidgets.QLabel(MulWalForm)
        self.label_52.setGeometry(QtCore.QRect(30, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_52.setObjectName("label_52")
        self.lineEdit_6 = QtWidgets.QLineEdit(MulWalForm)
        self.lineEdit_6.setGeometry(QtCore.QRect(50, 160, 371, 31))
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
        self.pushButton_9 = QtWidgets.QPushButton(MulWalForm)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 370, 291, 51))
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
        self.line_41 = QtWidgets.QFrame(MulWalForm)
        self.line_41.setGeometry(QtCore.QRect(50, 310, 371, 16))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.closeenterpsw = QtWidgets.QPushButton(MulWalForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(420, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")

        self.retranslateUi(MulWalForm)
        QtCore.QMetaObject.connectSlotsByName(MulWalForm)

    def retranslateUi(self, MulWalForm):
        _translate = QtCore.QCoreApplication.translate
        MulWalForm.setWindowTitle(_translate("MulWalForm", "Form"))
        self.label_51.setText(_translate("MulWalForm", "Wallet Name:"))
        self.label_15.setText(_translate("MulWalForm", "Wallet Info"))
        self.label_52.setText(_translate("MulWalForm", "Public Address:"))
        self.pushButton_9.setText(_translate("MulWalForm", "Save"))

import pic_rc
