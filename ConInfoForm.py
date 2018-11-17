# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qt_ui\ConInfoForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ConInfoForm(object):
    def setupUi(self, ConInfoForm):
        ConInfoForm.setObjectName("ConInfoForm")
        ConInfoForm.resize(457, 424)
        ConInfoForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_15 = QtWidgets.QLabel(ConInfoForm)
        self.label_15.setGeometry(QtCore.QRect(20, 30, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(135, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.label_51 = QtWidgets.QLabel(ConInfoForm)
        self.label_51.setGeometry(QtCore.QRect(30, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_51.setObjectName("label_51")
        self.line_38 = QtWidgets.QFrame(ConInfoForm)
        self.line_38.setGeometry(QtCore.QRect(50, 180, 371, 16))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.lineEdit_7 = QtWidgets.QLineEdit(ConInfoForm)
        self.lineEdit_7.setGeometry(QtCore.QRect(50, 270, 371, 31))
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
        self.label_52 = QtWidgets.QLabel(ConInfoForm)
        self.label_52.setGeometry(QtCore.QRect(30, 110, 151, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_52.setObjectName("label_52")
        self.closeenterpsw = QtWidgets.QPushButton(ConInfoForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(410, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.lineEdit_6 = QtWidgets.QLineEdit(ConInfoForm)
        self.lineEdit_6.setGeometry(QtCore.QRect(50, 150, 371, 31))
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
        self.line_41 = QtWidgets.QFrame(ConInfoForm)
        self.line_41.setGeometry(QtCore.QRect(50, 300, 371, 16))
        self.line_41.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_41.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_41.setObjectName("line_41")
        self.pushButton_9 = QtWidgets.QPushButton(ConInfoForm)
        self.pushButton_9.setGeometry(QtCore.QRect(80, 350, 291, 51))
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

        self.retranslateUi(ConInfoForm)
        QtCore.QMetaObject.connectSlotsByName(ConInfoForm)

    def retranslateUi(self, ConInfoForm):
        _translate = QtCore.QCoreApplication.translate
        ConInfoForm.setWindowTitle(_translate("ConInfoForm", "Form"))
        self.label_15.setText(_translate("ConInfoForm", "Contact Info"))
        self.label_51.setText(_translate("ConInfoForm", "Name:"))
        self.label_52.setText(_translate("ConInfoForm", "Recipient Address:"))
        self.pushButton_9.setText(_translate("ConInfoForm", "Save"))

import pic_rc
