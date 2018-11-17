# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AccountForm(object):
    def setupUi(self, AccountForm):
        AccountForm.setObjectName("AccountForm")
        AccountForm.resize(609, 572)
        AccountForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Account = QtWidgets.QTableWidget(AccountForm)
        self.Account.setGeometry(QtCore.QRect(40, 70, 531, 391))
        self.Account.setStyleSheet("border:0px;\n"
"color: rgb(135, 0, 255);")
        self.Account.setObjectName("Account")
        self.Account.setColumnCount(2)
        self.Account.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Account.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Account.setHorizontalHeaderItem(1, item)
        self.label_15 = QtWidgets.QLabel(AccountForm)
        self.label_15.setGeometry(QtCore.QRect(10, 0, 271, 61))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(135, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.closeenterpsw = QtWidgets.QPushButton(AccountForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(570, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.pushButton_9 = QtWidgets.QPushButton(AccountForm)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 490, 291, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pushButton_9.setStyleSheet("background-color: rgb(135, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:25px;")
        self.pushButton_9.setFlat(True)
        self.pushButton_9.setObjectName("pushButton_9")

        self.retranslateUi(AccountForm)
        QtCore.QMetaObject.connectSlotsByName(AccountForm)

    def retranslateUi(self, AccountForm):
        _translate = QtCore.QCoreApplication.translate
        AccountForm.setWindowTitle(_translate("AccountForm", "Form"))
        item = self.Account.horizontalHeaderItem(0)
        item.setText(_translate("AccountForm", "Wallet Name"))
        item = self.Account.horizontalHeaderItem(1)
        item.setText(_translate("AccountForm", "Public Address"))
        self.label_15.setText(_translate("AccountForm", "Select Account"))
        self.pushButton_9.setText(_translate("AccountForm", "Select"))
		
import pic_rc
