# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\qt_ui\DeleteForm.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DeleteForm(object):
    def setupUi(self, DeleteForm):
        DeleteForm.setObjectName("DeleteForm")
        DeleteForm.resize(400, 215)
        DeleteForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_10 = QtWidgets.QPushButton(DeleteForm)
        self.pushButton_10.setGeometry(QtCore.QRect(220, 150, 111, 41))
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
"border-radius:15px;")
        self.pushButton_10.setFlat(False)
        self.pushButton_10.setObjectName("pushButton_10")
        self.label_15 = QtWidgets.QLabel(DeleteForm)
        self.label_15.setGeometry(QtCore.QRect(40, 60, 331, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_15.setObjectName("label_15")
        self.pushButton_9 = QtWidgets.QPushButton(DeleteForm)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 150, 111, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setStyleSheet("background-color: rgb(135, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:15px;")
        self.pushButton_9.setFlat(False)
        self.pushButton_9.setObjectName("pushButton_9")
        self.closeenterpsw = QtWidgets.QPushButton(DeleteForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(360, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")

        self.retranslateUi(DeleteForm)
        QtCore.QMetaObject.connectSlotsByName(DeleteForm)

    def retranslateUi(self, DeleteForm):
        _translate = QtCore.QCoreApplication.translate
        DeleteForm.setWindowTitle(_translate("DeleteForm", "Form"))
        self.pushButton_10.setText(_translate("DeleteForm", "Quit"))
        self.label_15.setText(_translate("DeleteForm", "Do you want to delete?"))
        self.pushButton_9.setText(_translate("DeleteForm", "Confirm"))

import pic_rc
