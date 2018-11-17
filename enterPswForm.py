# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qt_ui\enterPswForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_EnterPswForm(object):
    def setupUi(self, EnterPswForm):
        EnterPswForm.setObjectName("EnterPswForm")
        EnterPswForm.resize(436, 225)
        EnterPswForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_9 = QtWidgets.QPushButton(EnterPswForm)
        self.pushButton_9.setGeometry(QtCore.QRect(74, 160, 261, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setStyleSheet("background-color: rgb(135, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:18px;")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(EnterPswForm)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 100, 321, 31))
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
        self.line_38 = QtWidgets.QFrame(EnterPswForm)
        self.line_38.setGeometry(QtCore.QRect(40, 130, 371, 10))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.turn2visible1_2 = QtWidgets.QPushButton(EnterPswForm)
        self.turn2visible1_2.setGeometry(QtCore.QRect(370, 100, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.turn2visible1_2.setFont(font)
        self.turn2visible1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.turn2visible1_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.turn2visible1_2.setAutoFillBackground(False)
        self.turn2visible1_2.setStyleSheet("border:0px;")
        self.turn2visible1_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/02.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.turn2visible1_2.setIcon(icon)
        self.turn2visible1_2.setIconSize(QtCore.QSize(40, 40))
        self.turn2visible1_2.setFlat(True)
        self.turn2visible1_2.setObjectName("turn2visible1_2")
        self.label_15 = QtWidgets.QLabel(EnterPswForm)
        self.label_15.setGeometry(QtCore.QRect(14, 10, 281, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(135, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.closeenterpsw = QtWidgets.QPushButton(EnterPswForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(400, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon1)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")

        self.retranslateUi(EnterPswForm)
        QtCore.QMetaObject.connectSlotsByName(EnterPswForm)

    def retranslateUi(self, EnterPswForm):
        _translate = QtCore.QCoreApplication.translate
        EnterPswForm.setWindowTitle(_translate("EnterPswForm", "Form"))
        self.pushButton_9.setText(_translate("EnterPswForm", "Confirm"))
        self.label_15.setText(_translate("EnterPswForm", "   Enter Password"))

import pic_rc
