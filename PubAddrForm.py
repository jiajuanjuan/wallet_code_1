# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qt_ui\PubAddrForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PubAddrForm(object):
    def setupUi(self, PubAddrForm):
        PubAddrForm.setObjectName("PubAddrForm")
        PubAddrForm.resize(492, 445)
        PubAddrForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8 = QtWidgets.QLineEdit(PubAddrForm)
        self.lineEdit_8.setGeometry(QtCore.QRect(20, 380, 411, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("border:0px;\n"
"border-radius:20px;\n"
"\n"
"background-color: rgb(230, 238, 255);")
        self.lineEdit_8.setText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label = QtWidgets.QLabel(PubAddrForm)
        self.label.setGeometry(QtCore.QRect(110, 80, 251, 231))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_8 = QtWidgets.QLabel(PubAddrForm)
        self.label_8.setGeometry(QtCore.QRect(140, 340, 211, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.closeenterpsw = QtWidgets.QPushButton(PubAddrForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(450, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.pushButton_35 = QtWidgets.QPushButton(PubAddrForm)
        self.pushButton_35.setGeometry(QtCore.QRect(430, 380, 41, 41))
        self.pushButton_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_35.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_35.setAutoFillBackground(False)
        self.pushButton_35.setStyleSheet("border:0px;")
        self.pushButton_35.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/pic/purplecopy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_35.setIcon(icon1)
        self.pushButton_35.setIconSize(QtCore.QSize(77, 77))
        self.pushButton_35.setAutoDefault(False)
        self.pushButton_35.setFlat(True)
        self.pushButton_35.setObjectName("pushButton_35")

        self.retranslateUi(PubAddrForm)
        QtCore.QMetaObject.connectSlotsByName(PubAddrForm)

    def retranslateUi(self, PubAddrForm):
        _translate = QtCore.QCoreApplication.translate
        PubAddrForm.setWindowTitle(_translate("PubAddrForm", "Form"))
        self.label_8.setText(_translate("PubAddrForm", "Your Public Address"))

import pic_rc
