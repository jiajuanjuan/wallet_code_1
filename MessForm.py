# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MessForm.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MessForm(object):
    def setupUi(self, MessForm):
        MessForm.setObjectName("MessForm")
        MessForm.resize(622, 546)
        MessForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_15 = QtWidgets.QLabel(MessForm)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("color: rgb(135, 0, 255);")
        self.label_15.setObjectName("label_15")
        self.closeenterpsw = QtWidgets.QPushButton(MessForm)
        self.closeenterpsw.setGeometry(QtCore.QRect(580, 0, 41, 31))
        self.closeenterpsw.setFocusPolicy(QtCore.Qt.NoFocus)
        self.closeenterpsw.setStyleSheet("border:0px;")
        self.closeenterpsw.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/pic/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeenterpsw.setIcon(icon)
        self.closeenterpsw.setFlat(True)
        self.closeenterpsw.setObjectName("closeenterpsw")
        self.line_38 = QtWidgets.QFrame(MessForm)
        self.line_38.setGeometry(QtCore.QRect(30, 170, 561, 16))
        self.line_38.setSizeIncrement(QtCore.QSize(0, 10))
        self.line_38.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_38.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_38.setObjectName("line_38")
        self.line_39 = QtWidgets.QFrame(MessForm)
        self.line_39.setGeometry(QtCore.QRect(30, 340, 561, 20))
        self.line_39.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_39.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_39.setObjectName("line_39")
        self.line_40 = QtWidgets.QFrame(MessForm)
        self.line_40.setGeometry(QtCore.QRect(30, 430, 561, 21))
        self.line_40.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_40.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_40.setObjectName("line_40")
        self.pushButton_9 = QtWidgets.QPushButton(MessForm)
        self.pushButton_9.setGeometry(QtCore.QRect(160, 470, 301, 51))
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
        self.label_51 = QtWidgets.QLabel(MessForm)
        self.label_51.setGeometry(QtCore.QRect(40, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_51.setFont(font)
        self.label_51.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_51.setObjectName("label_51")
        self.label_52 = QtWidgets.QLabel(MessForm)
        self.label_52.setGeometry(QtCore.QRect(40, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_52.setFont(font)
        self.label_52.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_52.setObjectName("label_52")
        self.label_53 = QtWidgets.QLabel(MessForm)
        self.label_53.setGeometry(QtCore.QRect(40, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_53.setFont(font)
        self.label_53.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_53.setObjectName("label_53")
        self.label_54 = QtWidgets.QLabel(MessForm)
        self.label_54.setGeometry(QtCore.QRect(40, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_54.setFont(font)
        self.label_54.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_54.setObjectName("label_54")
        self.label_55 = QtWidgets.QLabel(MessForm)
        self.label_55.setGeometry(QtCore.QRect(40, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_55.setFont(font)
        self.label_55.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_55.setObjectName("label_55")
        self.label_56 = QtWidgets.QLabel(MessForm)
        self.label_56.setGeometry(QtCore.QRect(40, 310, 91, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_56.setFont(font)
        self.label_56.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_56.setObjectName("label_56")
        self.label_57 = QtWidgets.QLabel(MessForm)
        self.label_57.setGeometry(QtCore.QRect(40, 400, 91, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_57.setFont(font)
        self.label_57.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_57.setObjectName("label_57")
        self.label_58 = QtWidgets.QLabel(MessForm)
        self.label_58.setGeometry(QtCore.QRect(40, 360, 111, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.label_58.setFont(font)
        self.label_58.setStyleSheet("color: rgb(100, 100, 100);")
        self.label_58.setObjectName("label_58")
        self.lineEdit_7 = QtWidgets.QLineEdit(MessForm)
        self.lineEdit_7.setGeometry(QtCore.QRect(150, 190, 431, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setFocusPolicy(QtCore.Qt.NoFocus)
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
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setPlaceholderText("")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(MessForm)
        self.lineEdit_6.setGeometry(QtCore.QRect(150, 70, 431, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_6.setMouseTracking(False)
        self.lineEdit_6.setFocusPolicy(QtCore.Qt.NoFocus)
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
        self.lineEdit_6.setText("")
        self.lineEdit_6.setFrame(False)
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_8 = QtWidgets.QLineEdit(MessForm)
        self.lineEdit_8.setGeometry(QtCore.QRect(150, 230, 431, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_8.setToolTip("")
        self.lineEdit_8.setStatusTip("")
        self.lineEdit_8.setWhatsThis("")
        self.lineEdit_8.setAccessibleName("")
        self.lineEdit_8.setAccessibleDescription("")
        self.lineEdit_8.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_8.setFrame(False)
        self.lineEdit_8.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setPlaceholderText("")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(MessForm)
        self.lineEdit_9.setGeometry(QtCore.QRect(150, 270, 431, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_9.setFont(font)
        self.lineEdit_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_9.setToolTip("")
        self.lineEdit_9.setStatusTip("")
        self.lineEdit_9.setWhatsThis("")
        self.lineEdit_9.setAccessibleName("")
        self.lineEdit_9.setAccessibleDescription("")
        self.lineEdit_9.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_9.setFrame(False)
        self.lineEdit_9.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setPlaceholderText("")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(MessForm)
        self.lineEdit_10.setGeometry(QtCore.QRect(150, 310, 431, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_10.setFont(font)
        self.lineEdit_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_10.setToolTip("")
        self.lineEdit_10.setStatusTip("")
        self.lineEdit_10.setWhatsThis("")
        self.lineEdit_10.setAccessibleName("")
        self.lineEdit_10.setAccessibleDescription("")
        self.lineEdit_10.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_10.setFrame(False)
        self.lineEdit_10.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setPlaceholderText("")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.textEdit = QtWidgets.QTextEdit(MessForm)
        self.textEdit.setGeometry(QtCore.QRect(150, 110, 431, 62))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.textEdit.setFocusPolicy(QtCore.Qt.NoFocus)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.lineEdit_11 = QtWidgets.QLineEdit(MessForm)
        self.lineEdit_11.setGeometry(QtCore.QRect(150, 400, 431, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_11.setToolTip("")
        self.lineEdit_11.setStatusTip("")
        self.lineEdit_11.setWhatsThis("")
        self.lineEdit_11.setAccessibleName("")
        self.lineEdit_11.setAccessibleDescription("")
        self.lineEdit_11.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_11.setFrame(False)
        self.lineEdit_11.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setPlaceholderText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.lineEdit_12 = QtWidgets.QLineEdit(MessForm)
        self.lineEdit_12.setGeometry(QtCore.QRect(150, 360, 431, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.lineEdit_12.setFont(font)
        self.lineEdit_12.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lineEdit_12.setToolTip("")
        self.lineEdit_12.setStatusTip("")
        self.lineEdit_12.setWhatsThis("")
        self.lineEdit_12.setAccessibleName("")
        self.lineEdit_12.setAccessibleDescription("")
        self.lineEdit_12.setStyleSheet("\n"
"QLineEdit[echoMode=\"2\"] {\n"
"    lineedit-password-character:42;\n"
"}\n"
"")
        self.lineEdit_12.setFrame(False)
        self.lineEdit_12.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setPlaceholderText("")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label = QtWidgets.QLabel(MessForm)
        self.label.setGeometry(QtCore.QRect(30, 70, 571, 381))
        self.label.setStyleSheet("background:transparent")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(MessForm)
        QtCore.QMetaObject.connectSlotsByName(MessForm)

    def retranslateUi(self, MessForm):
        _translate = QtCore.QCoreApplication.translate
        MessForm.setWindowTitle(_translate("MessForm", "Form"))
        self.label_15.setText(_translate("MessForm", "Message Info"))
        self.pushButton_9.setText(_translate("MessForm", "Confirm"))
        self.label_51.setText(_translate("MessForm", "Address From:"))
        self.label_52.setText(_translate("MessForm", "Value:"))
        self.label_53.setText(_translate("MessForm", "Id:"))
        self.label_54.setText(_translate("MessForm", "Address To:"))
        self.label_55.setText(_translate("MessForm", "Gas:"))
        self.label_56.setText(_translate("MessForm", "Gas Used:"))
        self.label_57.setText(_translate("MessForm", "Time:"))
        self.label_58.setText(_translate("MessForm", "Block Number:"))

import pic_rc
