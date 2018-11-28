import re
from PyQt5 import QtPrintSupport
import subprocess
import sys
import eth_hash
# import ssl
# from typing import Type
from web3 import Web3
from web3 import HTTPProvider
import eth_utils
import Warning_Form
import Core_func
from web3.auto import w3
import json
import os
import webbrowser
import sys
import time
import shutil
import cytoolz._signatures
import cytoolz.utils
import qrcode
import requests
import sip
from datetime import datetime, timedelta
import time

import xml.dom.minidom
from eth_account import Account
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize, QTimer, QFile, QTextCodec
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QDialog, QFileDialog, QTableWidgetItem,
                             QLineEdit, QFrame, QAbstractItemView)
from PyQt5.QtGui import *
from PyQt5.QtCore import QCoreApplication
from Mainform_QT import *
from SendForm import Ui_SendForm
from RecieveForm import Ui_ReceiveForm
from MulWalForm import Ui_MulWalForm
from enterPswForm import Ui_EnterPswForm
from PubAddrForm import Ui_PubAddrForm
from NewContactForm import Ui_NewContactForm
from MessForm import Ui_MessForm
from PublishForm import Ui_publishForm
from AccountForm import Ui_AccountForm
from WalletInfoForm import Ui_WalletInfoForm
from ConInfoForm import Ui_ConInfoForm
from PswForm import Ui_PswForm
from SetPswForm import Ui_SetPswForm
from ChangePswForm import Ui_ChangePswForm
from PriKeyForm import Ui_PriKeyForm
from DeleteForm import Ui_DeleteForm
import subprocess
import xml.etree.ElementTree as ET
import matplotlib
# import matplotlib.pyplot as plt
import datetime
import hashlib
from ApplicationHelper import pathConfig
import pic_rc


matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

#判断当前是什么平台的模块
import platform
import MyXml
from ApplicationHelper import  ApplicationHelper,sortByTimeOfObj
from TransactionListHelper import  TransactionList, AccountTransactionsListEntity,AccountTransactionsEntity,AddressTransactionsEntity
from AddressLastBalanceEntity import HistoryBalanceHelper ,AddressBalanceEntity,BalanceEntity
from TransactionSendListHelper import  TransactionSendListHelper,AddressTransactionSendEntity,TransactionSendEntity
#sort函数的key参数可以传入一个比较函数，用这个模块将函数转成你key传入
import functools
class deleteform(QDialog, Ui_DeleteForm):
    def __init__(self,PRAE):
        super().__init__()
        self.ui = Ui_DeleteForm()
        self.ui.setupUi(self)
        self.publishform = publishform(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)  # .Dialog
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(lambda: self.closeform(PRAE))
        btnsave = self.ui.pushButton_9
        btnsave.clicked.connect(lambda: self.confirmpsw(PRAE))
        btnquit = self.ui.pushButton_10
        btnquit.clicked.connect(lambda: self.closeform(PRAE))
        self.passwordeye = 1
        self.row = 0
        self.wa = 0
        self.close()

    def show_w2(self, PRAE,row,wa):
        self.row = row
        self.wa = wa
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2, screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()
    def confirmpsw(self, PRAE):
        if self.wa == 1:
            ind = Core_func.QTableWidget.indexFromItem(
                ex.ui.multWallet, ex.ui.multWallet.item(self.row, 1))
            filename = pathConfig.keystoresPath + ind.data()[2:18] + ".keystore"

            addrentity = ex.walletroot.getElementsByTagName('WalletBaseEntity')[
                self.row]
            addrentity.parentNode.removeChild(addrentity)
            f = open(pathConfig.lastSettingPath + 'Wallets.xml', 'w')
            ex.walletdom.writexml(f, addindent=' ', newl='\n')
            f.close()

            if os.path.isfile(filename):
                os.remove(filename)
            print(ind.data())
            print(filename)
            print(ex.m_wallet.address)

            if ind.data() == ex.m_wallet.address or ex.ui.multWallet.rowCount()==1:
                ex.m_wallet.address = ''
                ex.ui.lineEdit_8.setText('')
                ex.ui.lineEdit_9.setText('')
                ex.ui.TransactionHistory.setRowCount(0)
                ex.ui.LogMessage.setRowCount(0)
                ex.ui.mywallet.setVisible(0)
                ex.ui.statistic.setVisible(0)
                ex.ui.message.setVisible(0)
                ex.ui.contact.setVisible(0)
                ex.pressbtn0()

            ex.ui.multWallet.removeRow(self.row)
        else:
            if (ex.ui.ContactsT.rowCount()-1) == 0:
                ex.ui.ContactsT.setRowCount(0)
                addrentity = ex.addrroot.getElementsByTagName('AddressEntity')[0]
                addrentity.parentNode.removeChild(addrentity)
                f = open(pathConfig.lastSettingPath +'test.xml', 'w')
                ex.addrdom.writexml(f, addindent=' ', newl='\n')
                f.close()
            else:
                ex.ui.ContactsT.removeRow(self.row)
                addrentity = ex.addrroot.getElementsByTagName('AddressEntity')[
                    self.row]
                addrentity.parentNode.removeChild(addrentity)
                f = open(pathConfig.lastSettingPath +'test.xml', 'w')
                ex.addrdom.writexml(f, addindent=' ', newl='\n')
                f.close()
        self.close()

    

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self, PRAE):
        self.close()

class pswform(QDialog, Ui_PswForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_PswForm()
        self.ui.setupUi(self)
        self.publishform = publishform(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)  # .Dialog
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(lambda: self.closeform(PRAE))
        btnsave = self.ui.pushButton_9
        btnsave.clicked.connect(lambda: self.confirmpsw(PRAE))
        btnquit = self.ui.pushButton_10
        btnquit.clicked.connect(lambda: self.closeform(PRAE))
        btnsee = self.ui.turn2visible1_2
        btnsee.clicked.connect(self.seepsw)
        self.passwordeye = 1
        self.close()
    def show_w2(self, PRAE):
        self.ui.lineEdit_6.clear()
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()
    def confirmpsw(self, PRAE):
        if len(self.ui.lineEdit_6.text()) < 6:
            self.publishform.show_w2(
                    'Please enter at least 6 characters', self)
        else:
            hl = hashlib.md5()
            hl.update(self.ui.lineEdit_6.text().encode(encoding='utf-8'))
            if PRAE.settingroot.getElementsByTagName('MinerP')[0].firstChild.data == hl.hexdigest():
                self.close()
            else:
                self.publishform.show_w2(
                    'invalid password', self)
    def seepsw(self):
        if self.passwordeye == 1:
            self.ui.lineEdit_6.setEchoMode(0)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/01.png"))
            self.passwordeye = 0
        else:
            self.ui.lineEdit_6.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/02.png"))
            self.passwordeye = 1
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()
    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()
    def closeform(self, PRAE):
        self.close()
        PRAE.close()
        sys.exit()


class changepswform(QDialog, Ui_ChangePswForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_ChangePswForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsave = self.ui.pushButton_9
        btnsave.clicked.connect(self.savechange)
        btnquit = self.ui.pushButton_35
        btnquit.clicked.connect(self.setloginpsw)
        btnsee = self.ui.turn2visible1_2
        btnsee.clicked.connect(self.seepsw)
        btnsee2 = self.ui.turn2visible1_3
        btnsee2.clicked.connect(self.seepsw2)
        btnsee3 = self.ui.turn2visible1_4
        btnsee3.clicked.connect(self.seepsw3)
        self.ui.lineEdit_6.setEnabled(1)
        self.ui.lineEdit_7.setEnabled(1)
        self.setable = 1
        self.passwordeye = 1
        self.passwordeye2 = 1
        self.passwordeye3 = 1
        self.publishform = publishform(self)
        self.close()

    def show_w2(self, PRAE):
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_8.clear()
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def setloginpsw(self):
        if self.setable == 0:
            self.ui.pushButton_35.setIcon(QIcon(":/pic/open2.png"))
            self.ui.lineEdit_6.setEnabled(1)
            self.ui.lineEdit_7.setEnabled(1)
            self.setable = 1
        else:
            self.ui.pushButton_35.setIcon(QIcon(":/pic/close2.png"))
            self.ui.lineEdit_6.setEnabled(0)
            self.ui.lineEdit_7.setEnabled(0)
            self.setable = 0

    def savechange(self):
        if self.setable == 0:
            if len(self.ui.lineEdit_8.text()) < 6:
                self.publishform.show_w2(
                    'Please enter at least 6 characters', self)
            else:
                hl = hashlib.md5()
                hl.update(self.ui.lineEdit_8.text().encode(encoding='utf-8'))
                if ex.settingroot.getElementsByTagName('MinerP')[0].firstChild.data == hl.hexdigest():
                    ex.settingroot.getElementsByTagName(
                        'MinerP')[0].firstChild.data = ' '
                    f = open(pathConfig.lastSettingPath +  'setting.xml', 'w')
                    ex.settingdom.writexml(f, addindent=' ', newl='\n')
                    f.close()
                    self.close()
                else:
                    self.publishform.show_w2(
                        'Please enter right password', self)
        else:
            if len(self.ui.lineEdit_8.text()) < 6:
                self.publishform.show_w2(
                    'Please enter at least 6 characters', self)
            elif self.ui.lineEdit_6.text() != self.ui.lineEdit_7.text():
                self.publishform.show_w2('Please enter same passwords', self)
            else:
                hl = hashlib.md5()
                hl.update(self.ui.lineEdit_8.text().encode(encoding='utf-8'))
                if ex.settingroot.getElementsByTagName('MinerP')[0].firstChild.data == hl.hexdigest():
                    h2 = hashlib.md5()
                    h2.update(self.ui.lineEdit_6.text().encode(
                        encoding='utf-8'))
                    ex.settingroot.getElementsByTagName(
                        'MinerP')[0].firstChild.data = h2.hexdigest()
                    f = open(pathConfig.lastSettingPath +  'setting.xml', 'w')
                    ex.settingdom.writexml(f, addindent=' ', newl='\n')
                    f.close()
                    self.close()
                else:
                    self.publishform.show_w2(
                        'Please enter right password', self)
        # self.close()

    def seepsw(self):
        if self.passwordeye == 1:
            self.ui.lineEdit_6.setEchoMode(0)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/01.png"))
            self.passwordeye = 0
        else:
            self.ui.lineEdit_6.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/02.png"))
            self.passwordeye = 1

    def seepsw2(self):
        if self.passwordeye2 == 1:
            self.ui.lineEdit_7.setEchoMode(0)
            self.ui.turn2visible1_3.setIcon(QIcon(":/pic/01.png"))
            self.passwordeye2 = 0
        else:
            self.ui.lineEdit_7.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_3.setIcon(QIcon(":/pic/02.png"))
            self.passwordeye2 = 1

    def seepsw3(self):
        if self.passwordeye3 == 1:
            self.ui.lineEdit_8.setEchoMode(0)
            self.ui.turn2visible1_4.setIcon(QIcon(":/pic/01.png"))
            self.passwordeye3 = 0
        else:
            self.ui.lineEdit_8.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_4.setIcon(QIcon(":/pic/02.png"))
            self.passwordeye3 = 1

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class prikeyform(QDialog, Ui_PriKeyForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_PriKeyForm()
        # self.ui.setupUi(self)
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        # self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btncopy = self.ui.pushButton_35
        btncopy.clicked.connect(self.copyaddr)
        # self.ui.lineEdit_6.changeEvent.connect(self.showqrcode)
        # self.ui.lineEdit_6.keyPressEvent(self,self.showqrcode)
        self.close()

    def show_w2(self, PRAE):
        self.showqrcode()
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def showqrcode(self):
        self.ui.lineEdit_8.setText(ex.m_wallet.privateKey)
        strAddressAndAmount = ex.m_wallet.privateKey  # + "," + value
        self.imgpub = qrcode.make(strAddressAndAmount)
        self.imgpub.save(pathConfig.keystoresPath + "private.png")
        self.ui.label.setPixmap(QPixmap(pathConfig.keystoresPath + "private.png"))
        self.ui.label.setAutoFillBackground(1)

    def copyaddr(self):
        self.clipboard_public_key = QApplication.clipboard()
        self.clipboard_public_key.setText(ex.m_wallet.privateKey)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class setpswform(QDialog, Ui_SetPswForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_SetPswForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsave = self.ui.pushButton_9
        btnsave.clicked.connect(self.savechange)
        btnquit = self.ui.pushButton_35
        btnquit.clicked.connect(self.setloginpsw)
        btnsee = self.ui.turn2visible1_2
        btnsee.clicked.connect(self.seepsw)
        btnsee2 = self.ui.turn2visible1_3
        btnsee2.clicked.connect(self.seepsw2)
        self.ui.lineEdit_6.setEnabled(0)
        self.ui.lineEdit_7.setEnabled(0)
        self.setable = 0
        self.passwordeye = 1
        self.passwordeye2 = 1
        self.publishform = publishform(self)

        self.close()

    def show_w2(self, PRAE):
        if ex.settingroot.getElementsByTagName('MinerP')[0].firstChild.data == ' ':
            self.ui.lineEdit_6.clear()
            self.ui.lineEdit_7.clear()
            screen = PRAE.geometry()
            size = self.geometry()
            self.move(screen.left() + (screen.width() - size.width()) / 2,
                      screen.top() + (screen.height() - size.height()) / 2)
            self.exec_()
        else:
            self.changepswform = changepswform(PRAE)
            self.changepswform.show_w2(PRAE)

    def setloginpsw(self):
        if self.setable == 0:
            self.ui.pushButton_35.setIcon(QIcon(":/pic/open2.png"))
            self.ui.lineEdit_6.setEnabled(1)
            self.ui.lineEdit_7.setEnabled(1)
            self.setable = 1
        else:
            self.ui.pushButton_35.setIcon(QIcon(":/pic/close2.png"))
            self.ui.lineEdit_6.setEnabled(0)
            self.ui.lineEdit_7.setEnabled(0)
            self.setable = 0

    def savechange(self):
        if len(self.ui.lineEdit_6.text()) < 6:
            self.publishform.show_w2(
                'Please enter at least 6 characters', self)
        elif self.ui.lineEdit_6.text() != self.ui.lineEdit_7.text():
            self.publishform.show_w2('Please enter same passwords', self)
        else:
            hl = hashlib.md5()
            hl.update(self.ui.lineEdit_6.text().encode(encoding='utf-8'))
            ex.settingroot.getElementsByTagName(
                'MinerP')[0].firstChild.data = hl.hexdigest()
            f = open(pathConfig.lastSettingPath +  'setting.xml', 'w')
            ex.settingdom.writexml(f, addindent=' ', newl='\n')
            f.close()
            self.close()

    def seepsw(self):
        if self.passwordeye == 1:
            self.ui.lineEdit_6.setEchoMode(0)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/01.png"))
            self.passwordeye = 0
        else:
            self.ui.lineEdit_6.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/02.png"))
            self.passwordeye = 1

    def seepsw2(self):
        if self.passwordeye2 == 1:
            self.ui.lineEdit_7.setEchoMode(0)
            self.ui.turn2visible1_3.setIcon(QIcon(":/pic/01.png"))
            self.passwordeye2 = 0
        else:
            self.ui.lineEdit_7.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_3.setIcon(QIcon(":/pic/02.png"))
            self.passwordeye2 = 1

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class enterpswform(QDialog, Ui_EnterPswForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_EnterPswForm()
        self.ui.setupUi(self)
        # self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.publishform = publishform(self)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnconfirm = self.ui.pushButton_9
        self.passwordeye = 1
        self.addr = '0'
        btnconfirm.clicked.connect(lambda: self.getprikey(
            self.addr, self.ui.lineEdit_6.text()))
        self.gotprikey = 0
        self.needtosend = 0
        btnsee = self.ui.turn2visible1_2
        btnsee.clicked.connect(self.seepsw)
        self.close()

    def show_w2(self, str, PRAE, send=0):
        self.addr = str
        self.ui.lineEdit_6.clear()
        self.gotprikey = 0
        if send == 1:
            self.needtosend = 1
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()
    def seepsw(self):
        if self.passwordeye == 1:
            self.ui.lineEdit_6.setEchoMode(0)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/01.png"))
            self.passwordeye = 0
        else:
            self.ui.lineEdit_6.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/02.png"))
            self.passwordeye = 1

    def getprikey(self, addr, password):
        #进行交易之前先判断nonce的值为0的话标识还没请求过这个值，则先进行nonce值的请求
        if ex.m_wallet.nonce == 0:
            retNonce =  Core_func.getAccountNonce(ex.m_wallet.address)
            if retNonce[0] == False:
                self.publishform.show_w2(retNonce[1], self)
                return 1
            ex.m_wallet.nonce = retNonce[1]


        print("getprikey" )
        print(addr, password)
        filename = pathConfig.keystoresPath +addr[2:18] + ".keystore"
        if os.path.isfile(filename):
            file = open(filename, 'r')
            content = file.readline()
        else:
            self.publishform.show_w2('Can not found your Keystore', self)
            self.close()
            return 1        
        try:
            self.prikey = w3.toHex(Account.decrypt(content, password))
        except Exception as err:
            self.publishform.show_w2('Please enter right password', self)
            self.close()
            return 1
        print(self.prikey)

        self.gotprikey = 1
        if self.needtosend == 1:
            ex.m_wallet.privateKey = self.prikey
            try:
                print("trans Value : "+  ex.Trans.value)
                ret = Core_func.Transaction_out(
                    ex.m_wallet.privateKey, ex.Trans.toaddr, ex.Trans.value, ex.Trans.Gas, ex.Trans.Gasprice,ex.m_wallet.nonce)
            except Exception as err:
                self.publishform.show_w2(err, self)
                return 1
            if ret[0] == True:
                ex.m_wallet.nonce = ret[1]
                tx_hash = ret[2]
                try:
                    TransactionSend = TransactionSendEntity(addressFrom = ex.m_wallet.address.lower(),gasPrice = ex.Trans.Gasprice,gas= ex.Trans.Gas,
                                                        value = ex.Trans.value,addressTo= ex.Trans.toaddr.lower(),nonce= ex.m_wallet.nonce)
                    TransactionSend.tx_hash = tx_hash
                    tslHelper = TransactionSendListHelper()
                    tslHelper.add(ex.m_wallet.address,TransactionSend)
                except Exception as err:
                    print("add tslHelper Error : "+ str(err))



                '''
                Core_func.addtranslistxml(ex.transdom, ex.transroot, addr, time.strftime('%Y-%m-%d', time.localtime(time.time())), addr, 'none',
                                          ex.Trans.toaddr, ex.Trans.Gasprice, ' ', ' ', ret[1],
                                          ex.Trans.Gas, ex.Trans.value, datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                                          'Send', 'Submitted')

                Core_func.addtranslistxml(ex.transdom, ex.transroot, ex.Trans.toaddr, time.strftime('%Y-%m-%d', time.localtime(time.time())), addr, 'none',
                                          ex.Trans.toaddr, ex.Trans.Gasprice, ' ', ' ', ret[1],
                                          ex.Trans.Gas, ex.Trans.value, datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S'),
                                          'Recieve', 'Submitted')
                '''
                # self.closeform()
                # self.publishform.show_w2('transaction successfully',self)

                ex.Trans.value = ''
                ex.Trans.Type = ''
                ex.Trans.Gas = ''
                ex.Trans.Gasprice = ''
                ex.Trans.toaddr = ''
                #ex.refresh()
                #ex.initchart()
                ex.m_wallet.nonce = ex.m_wallet.nonce+1
                self.publishform.show_w2('transaction succeed', self)
                self.closeform()
                # self.publishform.show_w2('transaction succeed', self)
            else:
                self.publishform.show_w2('transaction failed'+ ret[2] , self)
        else:
            ex.ui.lineEdit_9.setText(self.prikey)
            ex.m_wallet.privateKey = self.prikey
            ex.ui.pushButton_35.setIcon(QIcon(":/pic/01.png"))
            ex.ui.pushButton_43.setIcon(QIcon(":/pic/010.png"))
            ex.ui.lineEdit_9.setEchoMode(0)
            ex.privatekeyeye = 0
        self.needtosend = 0
        self.close()
        return 0

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() == Qt.LeftButton:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
        except Exception as err:
            pass

    def closeform(self):
        self.close()

class Figure_Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=2, dpi=100):
        fig = Figure(figsize=(width, height), dpi=70)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.x=[]
        self.y=[]
        self.balance = 0
        self.axes = fig.add_subplot(111)

    def testM(self):
        today_USD = Core_func.get_new_USD()

        y = [float(today_USD)]

        x = [31,30,29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        try:
            ret3 = Core_func.getTokenMarket()
        except Exception as err:
            y = [0]
            x = [0]
            self.axes.plot(x, y, 'r-', 1)
            self.axes.set_axis_off()
            return 0
        if ret3[0] == 1:
            for i in range(len(ret3[1])):
                y.append(float(ret3[1][i]['TokenPriceUSD']))
            self.axes.plot(x, y,'r-',1)
            self.axes.set_axis_off()
            return today_USD

    def testB(self,addr):
        if addr != '':
            try:
                ret3 = Core_func.getTransactionRecord_day(addr, '20')
            except Exception as err:
                self.y = [0]
                self.x = [0]
                self.axes.plot(self.x, self.y, 'r-', 1)
                self.axes.set_axis_off()
                return 0
            y = []
            x = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2,
                 1]
            for i in range(len(ret3[1])):
                y.append(float(ret3[1][i]['history_balance']))
            y.append(0)
            self.axes.plot(x, y, 'r-', 1)
            self.axes.set_axis_off()
            return  ret3[1][i]['history_balance']
            # ret3[1][i]['history_balance']
        else:
            y = [0]
            x = [0]
            self.axes.plot(x, y, 'r-', 1)
            self.axes.set_axis_off()
            return  0
        

    def testR(self,addr):
        if addr != '':
            try:
                ret3 = Core_func.getMiningRecord(addr)
            except Exception as err:
                y = [0]
                x = [0]
                self.axes.plot(x, y, 'r-', 1)
                self.axes.set_axis_off()
                return 0
            if len(ret3[1])!=0:
                y = []
                x = []
                totol = 0
                day_totol = 0
                j = 0

                time_s = datetime.datetime.strptime(
                    ret3[1][len(ret3[1])-1]['utc_timestamp'], "%Y-%m-%d %H:%M:%S")
                localtime = Core_func.utc2local(time_s)
                lastday = str(localtime.strftime('%Y-%m-%d %H:%M:%S'))[0:10]


                a = len(ret3[1])-1
                for i in range(len(ret3[1])):
                    time_s = Core_func.utc2local(datetime.datetime.strptime(
                        ret3[1][a-i]['utc_timestamp'], "%Y-%m-%d %H:%M:%S"))

                    if lastday != str(time_s)[0:10]:
                        lastday = str(time_s)[0:10]
                        x.append(j)
                        if day_totol >= totol:
                            totol = day_totol
                        y.append(day_totol)
                        j = j + 1
                        day_totol = int(ret3[1][i]['totol_reward'])
                        if i == len(ret3[1])-1:
                            x.append(j)
                            if day_totol >= totol:
                                totol = day_totol
                            y.append(day_totol)
                    else:
                        day_totol = day_totol + int(ret3[1][i]['totol_reward'])
                        if day_totol >= totol:
                                totol = day_totol
                        if i == a:
                            x.append(j)
                            if day_totol >= totol:
                                totol = day_totol
                            y.append(day_totol)

                if j == 0:
                    y = [0,day_totol]
                    x = [0,1]



                #y.append(0)
                #x.append(0)

                #print(ret3[1][2]['timestamp'][0:10])
                # self.axes.plot(x, y, 'r-', 1)
                self.axes.bar(x, y,fc='r')
                self.axes.set_axis_off()
                return (totol,j)
            else:
                y = [0]
                x = [0]
                self.axes.plot(x, y, 'r-', 1)
                self.axes.set_axis_off()
                return 0
        else:
            y = [0]
            x = [0]
            self.axes.plot(x, y, 'r-', 1)
            self.axes.set_axis_off()
            return 0

class conInfoform(QDialog, Ui_ConInfoForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_ConInfoForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.publishform = publishform(self)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsave = self.ui.pushButton_9
        self.Row = 0
        btnsave.clicked.connect(lambda: self.savechange(self.Row))

        self.close()

    def show_w2(self, row, PRAE):
        self.Row = row
        ind = Core_func.QTableWidget.indexFromItem(
            ex.ui.ContactsT, ex.ui.ContactsT.item(row, 1))
        self.ui.lineEdit_6.setText(ind.data())
        ind = Core_func.QTableWidget.indexFromItem(
            ex.ui.ContactsT, ex.ui.ContactsT.item(row, 0))
        self.ui.lineEdit_7.setText(ind.data())
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def savechange(self, row):
        ################
        # waiting to add checking same wallet already existed
        ################


        if self.ui.lineEdit_7.text() !='':
            newItemName = QTableWidgetItem(self.ui.lineEdit_7.text())
            ex.ui.ContactsT.setItem(row, 0, newItemName)
            Core_func.editaddressxml(
                ex.addrdom, ex.addrroot, self.ui.lineEdit_7.text(), row)
            self.close()
        else:
            self.publishform.show_w2('please enter the name', self) 

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class walletInfoform(QDialog, Ui_WalletInfoForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_WalletInfoForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsave = self.ui.pushButton_9
        self.Row = 0
        btnsave.clicked.connect(lambda: self.savechange(self.Row))
        self.close()

    def show_w2(self, PRAE, row):
        self.Row = row

        ind = Core_func.QTableWidget.indexFromItem(
            ex.ui.multWallet, ex.ui.multWallet.item(row, 1))
        self.ui.lineEdit_6.setText(ind.data())
        ind = Core_func.QTableWidget.indexFromItem(
            ex.ui.multWallet, ex.ui.multWallet.item(row, 0))
        self.ui.lineEdit_7.setText(ind.data())
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def savechange(self, row):
        ################
        # waiting to add checking same wallet already existed

        ################
        if self.ui.lineEdit_7.text() !='':
            newItemName = QTableWidgetItem(self.ui.lineEdit_7.text())
            ex.ui.multWallet.setItem(row, 0, newItemName)
            Core_func.editwalletxml(
                ex.walletdom, ex.walletroot, self.ui.lineEdit_7.text(), row)
            self.close()
        else:
            ind = Core_func.QTableWidget.indexFromItem(
                ex.ui.multWallet, ex.ui.multWallet.item(row, 1))
            newItemName = QTableWidgetItem(ind.data()[0:10])
            ex.ui.multWallet.setItem(row, 0, newItemName)
            Core_func.editwalletxml(
                ex.walletdom, ex.walletroot, ind.data()[0:10], row)
            self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class publishform(QDialog, Ui_publishForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_publishForm()
        self.ui.setupUi(self)
        # self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnconfirm = self.ui.pushButton_9
        btnconfirm.clicked.connect(self.closeform)
        self.close()

    def show_w2(self, str, PRAE):
        self.ui.textEdit.setText(str)
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class accountform(QDialog, Ui_AccountForm):
    def __init__(self, Paren):
        super().__init__()
        self.ui = Ui_AccountForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.ui.Account.setStyleSheet("color:#000000;border:0px;background-color: rgb(255, 255, 255);")
        self.ui.Account.horizontalHeader().setVisible(0)
        self.ui.Account.verticalHeader().setVisible(0)
        self.ui.Account.setShowGrid(0)
        self.ui.Account.horizontalHeader().setStretchLastSection(1)
        self.ui.Account.verticalHeader().setDefaultSectionSize(78)
        self.ui.Account.setColumnWidth(0, 150)
        self.ui.Account.setColumnWidth(1, 360)
        self.ui.Account.setSelectionMode(
            QAbstractItemView.NoSelection)
        self.ui.Account.setFrameShape(QFrame.NoFrame)
        self.ui.Account.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.Account.setSelectionBehavior(Core_func.QTableWidget.SelectRows)
        self.ui.Account.setFocusPolicy(Qt.NoFocus)
        self.ui.Account.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(lambda: self.closeform1(Paren))
        btnconfirm = self.ui.pushButton_9
        btnconfirm.clicked.connect(lambda: self.closeform(Paren))
        self.ui.Account.itemClicked.connect(self.choseaccount)
        self.close()

    def show_w2(self, PRAE):

        if os.path.isfile(pathConfig.lastSettingPath +'test.xml'):
            if len(ex.addrroot.getElementsByTagName('AddressEntity')) != 0:
                self.ui.Account.setRowCount(0)
                print('del contact')
                for AddressEntity in ex.addrroot.getElementsByTagName('AddressEntity'):
                    Rcount = self.ui.Account.rowCount()
                    self.ui.Account.setRowCount(Rcount + 1)

                    itemlist1 = AddressEntity.getElementsByTagName(
                        'AccountName')
                    item1 = itemlist1[0]
                    itemlist2 = AddressEntity.getElementsByTagName('Address')
                    item2 = itemlist2[0]

                    newItemname = QTableWidgetItem(item1.firstChild.data)
                    newItemaddr = QTableWidgetItem(item2.firstChild.data)

                    self.ui.Account.setItem(Rcount, 0, newItemname)
                    self.ui.Account.setItem(Rcount, 1, newItemaddr)
            else:
                self.ui.Account.setRowCount(0)
        else:
            print('')
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def choseaccount(self, QTableWidgetItem):
        # QTableWidgetItem.setForeground(QBrush(QColor(135, 0, 255)))
        # QTableWidgetItem.setForeground(QBrush(QColor(135, 0, 255)))
        
        try:
            row = Core_func.QTableWidget.indexFromItem(
                self.ui.Account, QTableWidgetItem).row()
            for i in range(self.ui.Account.rowCount()):
                if i==row:
                    self.ui.Account.item(i, 0).setForeground(QBrush(QColor(135, 0, 255)))
                    self.ui.Account.item(i, 1).setForeground(QBrush(QColor(135, 0, 255)))
                else:
                    self.ui.Account.item(i, 0).setForeground(QBrush(QColor(0, 0, 0)))
                    self.ui.Account.item(i, 1).setForeground(QBrush(QColor(0, 0, 0)))
            ind = Core_func.QTableWidget.indexFromItem(
                self.ui.Account, self.ui.Account.item(row, 1))
            ex.Trans.toaddr = ind.data()
        except Exception as err:
            self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() == Qt.LeftButton:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
        except Exception as err:
            pass

    def closeform(self, Paren):
        if ex.Trans.toaddr != '':
            Paren.ui.lineEdit_7.setText(ex.Trans.toaddr)
        self.close()

    def closeform1(self, Paren):
        # if ex.Trans.toaddr != '':
        #     Paren.ui.lineEdit_7.setText(ex.Trans.toaddr)
        self.close()


class mingwaform(QDialog, Ui_AccountForm):
    def __init__(self, Paren):
        super().__init__()
        self.ui = Ui_AccountForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        self.ui.Account.setStyleSheet("color:#000000;border:0px;background-color: rgb(255, 255, 255);")
        self.ui.Account.horizontalHeader().setVisible(0)
        self.ui.Account.verticalHeader().setVisible(0)
        self.ui.Account.setShowGrid(0)
        self.ui.Account.horizontalHeader().setStretchLastSection(1)
        self.ui.Account.verticalHeader().setDefaultSectionSize(78)
        self.ui.Account.setColumnWidth(0, 150)
        self.ui.Account.setColumnWidth(1, 360)

        self.ui.Account.setFrameShape(QFrame.NoFrame)
        self.ui.Account.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.Account.setSelectionBehavior(Core_func.QTableWidget.SelectRows)
        self.ui.Account.setFocusPolicy(Qt.NoFocus)
        self.ui.Account.setSelectionMode(
            QAbstractItemView.NoSelection)
        self.ui.Account.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(lambda: self.closeform1(Paren))
        self.publishform = publishform(self)
        btnconfirm = self.ui.pushButton_9
        btnconfirm.clicked.connect(lambda: self.closeform(Paren))
        self.ui.Account.itemClicked.connect(self.choseaccount)
        self.setwa = ''
        self.close()

    def show_w2(self, PRAE):
        if os.path.isfile(pathConfig.lastSettingPath +'Wallets.xml'):
            if len(ex.walletroot.getElementsByTagName('WalletBaseEntity')) != 0:
                self.ui.Account.setRowCount(0)
                for AddressEntity in ex.walletroot.getElementsByTagName('WalletBaseEntity'):
                    Rcount = self.ui.Account.rowCount()
                    self.ui.Account.setRowCount(Rcount + 1)

                    itemlist1 = AddressEntity.getElementsByTagName(
                        'AccountName')
                    item1 = itemlist1[0]
                    itemlist2 = AddressEntity.getElementsByTagName('Address')
                    item2 = itemlist2[0]

                    newItemname = QTableWidgetItem(item1.firstChild.data)
                    newItemaddr = QTableWidgetItem(item2.firstChild.data)

                    self.ui.Account.setItem(Rcount, 0, newItemname)
                    self.ui.Account.setItem(Rcount, 1, newItemaddr)
            else:
                self.ui.Account.setRowCount(0)
        else:
            print('')
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()
    def choseaccount(self, QTableWidgetItem):
        # QTableWidgetItem.setForeground(QBrush(QColor(135, 0, 255)))
        # QTableWidgetItem.setForeground(QBrush(QColor(135, 0, 255)))
        try:
            row = Core_func.QTableWidget.indexFromItem(self.ui.Account, QTableWidgetItem).row()
            for i in range(self.ui.Account.rowCount()):
                if i==row:
                    self.ui.Account.item(i, 0).setForeground(QBrush(QColor(135, 0, 255)))
                    self.ui.Account.item(i, 1).setForeground(QBrush(QColor(135, 0, 255)))
                else:
                    self.ui.Account.item(i, 0).setForeground(QBrush(QColor(0, 0, 0)))
                    self.ui.Account.item(i, 1).setForeground(QBrush(QColor(0, 0, 0)))
            ind = Core_func.QTableWidget.indexFromItem(
                self.ui.Account, self.ui.Account.item(row, 1))
            print('change')
            # ex.ui.lineEdit_7.setText(ind.data())
            self.setwa = ind.data()
        except Exception as err:
            print(err)
            self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        try:
            if event.buttons() == Qt.LeftButton:
                self.move(event.globalPos() - self.dragPosition)
                event.accept()
        except Exception as err:
            pass

    def closeform(self, Paren):
        if len(self.setwa)==42 and self.setwa[0:2]=='0x':
            ex.ui.lineEdit_7.setText(self.setwa)
        elif len(self.setwa)==40 and self.setwa[0:2]!='0x':
            # self.setwa = '0x' + self.setwa
            self.publishform.show_w2("Address without '0x'!", self)
        self.close()

    def closeform1(self, Paren):
        # if ex.Trans.toaddr != '':
        #     Paren.ui.lineEdit_7.setText(ex.Trans.toaddr)
        self.close()

class messform(QDialog, Ui_MessForm):
    def __init__(self, parent,entity):
        super().__init__()
        self.ui = Ui_MessForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnconfirm = self.ui.pushButton_9
        btnconfirm.clicked.connect(self.closeform)
        self.publishform = publishform(self)
        self.parentw = parent
        self.TransEntity = entity
        self.close()

    def show(self):
        self.ui.lineEdit_12.setText(str(self.TransEntity.blockNumber))
        self.ui.lineEdit_11.setText(self.TransEntity.utc_timestamp)
        self.ui.lineEdit_9.setText(str(self.TransEntity.gas))
        self.ui.lineEdit_10.setText(str(self.TransEntity.gasUsed))
        self.ui.lineEdit_8.setText(self.TransEntity.addressTo)
        self.ui.lineEdit_7.setText(self.TransEntity.addressFrom)
        self.ui.lineEdit_6.setText(str(self.TransEntity.value))
        self.ui.textEdit.setText(self.TransEntity.tx_hash)
        screen = self.parentw.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()



    def show_w2(self, QTableWidgetItem):
        QTableWidgetItem.setForeground(QBrush(QColor(0, 0, 0)))
        row = Core_func.QTableWidget.indexFromItem(
            ex.ui.LogMessage, QTableWidgetItem).row()
        ex.ui.LogMessage.item(row, 0).setForeground(QBrush(QColor(0, 0, 0)))
        ex.ui.LogMessage.item(row, 1).setForeground(QBrush(QColor(0, 0, 0)))
        ex.ui.LogMessage.item(row, 2).setForeground(QBrush(QColor(0, 0, 0)))

        # ret = Core_func.getTransactionRecord(self.m_wallet.address)
        # if ret[0] == 1:
        #     ret[1][row]

        ind = Core_func.QTableWidget.indexFromItem(
            ex.ui.LogMessage, ex.ui.LogMessage.item(row, 2))
        indtime = Core_func.QTableWidget.indexFromItem(
            ex.ui.LogMessage, ex.ui.LogMessage.item(row, 1))
        print(ind.data())
        print(ind.data().split('tx_hash')[1][1:])
        try:
            ret = Core_func.getTransactionInfo(
                ind.data().split('tx_hash')[1][1:])
            self.ui.lineEdit_12.setText(str(ret[1][0]['blockNumber']))
            self.ui.lineEdit_11.setText(indtime.data())
            self.ui.lineEdit_9.setText(str(ret[1][0]['gas']))
            self.ui.lineEdit_10.setText(str(ret[1][0]['gasUsed']))
            self.ui.lineEdit_8.setText(str(ret[1][0]['addressTo']))
            self.ui.lineEdit_7.setText(str(ret[1][0]['addressFrom']))
            self.ui.lineEdit_6.setText(str(ret[1][0]['value']))
            self.ui.textEdit.setText(str(ret[1][0]['tx_hash']))
            screen = self.parentw.geometry()
            size = self.geometry()
            self.move(screen.left() + (screen.width() - size.width()) / 2,
                      screen.top() + (screen.height() - size.height()) / 2)
            self.exec_()
        except Exception as err:
            self.publishform.show_w2(
                'get information failed,please try again', self)
            return 1

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()

class newcontactform(QDialog, Ui_NewContactForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_NewContactForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsave = self.ui.pushButton_9
        btnsave.clicked.connect(self.savechange)
        btnscan = self.ui.pushButton_36
        btnscan.setVisible(False)
        self.publishform = publishform(self)
        self.close()

    def show_w2(self, PRAE):
        self.ui.lineEdit_6.clear()
        self.ui.lineEdit_7.clear()
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def savechange(self):
        if len(self.ui.lineEdit_6.text().strip())==42 and self.ui.lineEdit_6.text().strip()[0:2]=='0x':
            try:
                if ex.ui.ContactsT.rowCount()==0:
                    if self.ui.lineEdit_7.text().strip()=='':
                        self.publishform.show_w2('please enter the name', self)
                        return
                    else:
                        ex.ui.ContactsT.setRowCount(1)
                        newItemAddr = QTableWidgetItem(self.ui.lineEdit_6.text().strip())
                        newItemName = QTableWidgetItem(self.ui.lineEdit_7.text().strip())
                        # ret = ex.buttonsdef(Rcount)
                        ex.ui.ContactsT.setItem(0, 1, newItemAddr)
                        ex.ui.ContactsT.setItem(0, 0, newItemName)

                        newItemdel = QTableWidgetItem('   delete   ')
                        newItemdel.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemdel.setFlags(QtCore.Qt.ItemIsEnabled)
                        newItemsend = QTableWidgetItem('    send    ')
                        newItemsend.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemsend.setFlags(QtCore.Qt.ItemIsEnabled)
                        newItemedit = QTableWidgetItem('    edit    ')
                        newItemedit.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemedit.setFlags(QtCore.Qt.ItemIsEnabled)

                        ex.ui.ContactsT.setItem(0, 2, newItemsend)
                        ex.ui.ContactsT.setItem(0, 3, newItemedit)
                        ex.ui.ContactsT.setItem(0, 4, newItemdel)

                        Core_func.addaddressxml(
                            ex.addrdom, ex.addrroot, self.ui.lineEdit_7.text(), self.ui.lineEdit_6.text())
                else:
                    for i in range(ex.ui.ContactsT.rowCount()):
                        ind = Core_func.QTableWidget.indexFromItem(
                            ex.ui.ContactsT, ex.ui.ContactsT.item(i, 1))
                        if self.ui.lineEdit_6.text() == ind.data():
                            print('Address already exist')
                            self.publishform.show_w2('Address already exist', self)
                            return
                        if i == ex.ui.ContactsT.rowCount()-1:
                            
                            if self.ui.lineEdit_7.text().strip()=='':
                                self.publishform.show_w2('please enter the name', self)
                                return
                            else:
                                Rcount = ex.ui.ContactsT.rowCount()
                                ex.ui.ContactsT.setRowCount(Rcount + 1)
                                newItemAddr = QTableWidgetItem(self.ui.lineEdit_6.text())
                                newItemName = QTableWidgetItem(self.ui.lineEdit_7.text())
                                # ret = ex.buttonsdef(Rcount)
                                ex.ui.ContactsT.setItem(Rcount, 1, newItemAddr)
                                ex.ui.ContactsT.setItem(Rcount, 0, newItemName)

                                newItemdel = QTableWidgetItem('   delete   ')
                                newItemdel.setForeground(QBrush(QColor(135, 0, 255)))
                                newItemdel.setFlags(QtCore.Qt.ItemIsEnabled)
                                newItemsend = QTableWidgetItem('    send    ')
                                newItemsend.setForeground(QBrush(QColor(135, 0, 255)))
                                newItemsend.setFlags(QtCore.Qt.ItemIsEnabled)
                                newItemedit = QTableWidgetItem('    edit    ')
                                newItemedit.setForeground(QBrush(QColor(135, 0, 255)))
                                newItemedit.setFlags(QtCore.Qt.ItemIsEnabled)

                                ex.ui.ContactsT.setItem(Rcount, 2, newItemsend)
                                ex.ui.ContactsT.setItem(Rcount, 3, newItemedit)
                                ex.ui.ContactsT.setItem(Rcount, 4, newItemdel)

                                Core_func.addaddressxml(
                                    ex.addrdom, ex.addrroot, self.ui.lineEdit_7.text(), self.ui.lineEdit_6.text())
                self.close()
            except Exception as err:
                pass
        elif len(self.ui.lineEdit_6.text().strip())==40 and self.ui.lineEdit_6.text().strip()[0:2]!='0x':
            self.publishform.show_w2("Address without '0x'", self)
        else:
            self.publishform.show_w2('Please check address', self)
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class pubaddrForm(QDialog, Ui_PubAddrForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_PubAddrForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        # self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btncopy = self.ui.pushButton_35
        btncopy.clicked.connect(self.copyaddr)
        # self.ui.lineEdit_6.changeEvent.connect(self.showqrcode)
        # self.ui.lineEdit_6.keyPressEvent(self,self.showqrcode)
        self.close()

    def show_w2(self, PRAE):
        self.showqrcode()
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def showqrcode(self):
        self.ui.lineEdit_8.setText(ex.m_wallet.address)
        strAddressAndAmount = ex.m_wallet.address  # + "," + value
        self.imgpub = qrcode.make(strAddressAndAmount)
        self.imgpub.save(pathConfig.keystoresPath + "recieve.png")
        self.ui.label.setPixmap(QPixmap(pathConfig.keystoresPath + "recieve.png"))
        self.ui.label.setAutoFillBackground(1)

    def copyaddr(self):
        self.clipboard_public_key = QApplication.clipboard()
        self.clipboard_public_key.setText(ex.m_wallet.address)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class mulwalform(QDialog, Ui_MulWalForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_MulWalForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsave = self.ui.pushButton_9
        btnsave.clicked.connect(self.savechange)
        self.close()

    def show_w2(self, PRAE):
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def savechange(self):
        
        ex.m_wallet.accountname = self.ui.lineEdit_7.text().strip()
        self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class recieveform(QDialog, Ui_ReceiveForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_ReceiveForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btncopy = self.ui.pushButton_34
        btncopy.clicked.connect(self.copyaddr)
        self.ui.lineEdit_6.textChanged.connect(self.showqrcode)
        self.ui.lineEdit_6.setValidator(QDoubleValidator())
        # self.ui.lineEdit_6.changeEvent.connect(self.showqrcode)
        # self.ui.lineEdit_6.keyPressEvent(self,self.showqrcode)
        self.close()

    def showqrcode(self):
        self.ui.lineEdit_8.setText(ex.m_wallet.address)
        value = self.ui.lineEdit_6.text()
        strAddressAndAmount = ex.m_wallet.address   + "," + value
        self.imgpub = qrcode.make(strAddressAndAmount)
        self.imgpub.save(pathConfig.keystoresPath + "recieve.png")
        self.ui.label.setPixmap(QPixmap(pathConfig.keystoresPath + "recieve.png"))
        self.ui.label.setAutoFillBackground(1)

    def show_w2(self, PRAE):
        self.showqrcode()
        screen = PRAE.geometry()
        size = self.geometry()
        self.move(screen.left() + (screen.width() - size.width()) / 2,
                  screen.top() + (screen.height() - size.height()) / 2)
        self.exec_()

    def copyaddr(self):
        self.clipboard_public_key = QApplication.clipboard()
        self.clipboard_public_key.setText(ex.m_wallet.address)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.close()


class sendform(QDialog, Ui_SendForm):
    def __init__(self, PRAE):
        super().__init__()
        self.ui = Ui_SendForm()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.CustomizeWindowHint)
        btnc = self.ui.closeenterpsw
        btnc.clicked.connect(self.closeform)
        btnsend = self.ui.pushButton_9
        btnsend.clicked.connect(self.showenterphrase)
        self.accountform = accountform(self)
        self.publishform = publishform(self)
        btncont = self.ui.pushButton_34
        btncont.clicked.connect(lambda: self.accountform.show_w2(self))

        btnscan = self.ui.pushButton_36
        btnscan.setVisible(False)

        self.ui.radioButton.toggle()
        self.ui.radioButton.toggled.connect(self.change2Eco)
        self.ui.radioButton.setChecked(0)
        self.ui.radioButton_2.toggle()
        self.ui.radioButton_2.toggled.connect(self.change2Sta)
        self.ui.radioButton_2.setChecked(True)
        self.ui.radioButton_2.isChecked()
        self.ui.radioButton_3.toggle()
        self.ui.radioButton_3.toggled.connect(self.change2Qui)
        self.ui.radioButton_3.setChecked(0)
        self.ui.radioButton_4.toggle()
        self.ui.radioButton_4.toggled.connect(self.change2Cus)
        self.ui.radioButton_4.setChecked(0)
        self.ui.lineEdit_6.setValidator(QDoubleValidator())
        self.ui.lineEdit_8.setValidator(QDoubleValidator())
        self.ui.lineEdit_9.setValidator(QDoubleValidator())
        self.close()

    def change2Eco(self):
        if self.ui.radioButton.isChecked():
            self.ui.lineEdit_8.setText('60000')
            self.ui.lineEdit_9.setText('0.000000018')
            self.ui.lineEdit_8.setEnabled(0)
            self.ui.lineEdit_9.setEnabled(0)

    def change2Sta(self):
        if self.ui.radioButton_2.isChecked():
            self.ui.lineEdit_8.setText('200000')
            self.ui.lineEdit_9.setText('0.000000036')
            self.ui.lineEdit_8.setEnabled(0)
            self.ui.lineEdit_9.setEnabled(0)

    def change2Qui(self):
        if self.ui.radioButton_3.isChecked():
            self.ui.lineEdit_8.setText('1000000')
            self.ui.lineEdit_9.setText('0.000000072')
            self.ui.lineEdit_8.setEnabled(0)
            self.ui.lineEdit_9.setEnabled(0)

    def change2Cus(self):
        if self.ui.radioButton_4.isChecked():
            self.ui.lineEdit_8.clear()
            self.ui.lineEdit_9.clear()
            self.ui.lineEdit_8.setPlaceholderText('Enter Gas Limit')
            self.ui.lineEdit_9.setPlaceholderText('Enter Gas Price')
            self.ui.lineEdit_8.setEnabled(1)
            self.ui.lineEdit_9.setEnabled(1)

    def show_w2(self, PRAE):
        print('open send1')
        self.ui.radioButton_2.setChecked(True)
        self.ui.lineEdit_7.clear()
        self.ui.label_52.setText(' ')
        if ex.m_wallet.address == '' :
            self.publishform.show_w2('Please Choose A Wallet', self)
            self.close()

        else:
            try:
                print('open send2')
                balance = requests.get(
                    "https://waltonchain.net:18950/api/getBalance/" + ex.m_wallet.address).json()
                a = str(balance)
                self.ui.label_52.setText(a.split(',')[1][11:] + 'WTCT')
                # self.ui.lineEdit_7.setText(ex.m_wallet.address)
                self.ui.lineEdit_7.clear()

                screen = PRAE.geometry()
                size = self.geometry()
                self.move(screen.left() + (screen.width() - size.width()) / 2,
                          screen.top() + (screen.height() - size.height()) / 2)
                self.exec_()
            except Exception as err:
                ex.refreshTop()
                print('without network send1')
                self.ui.lineEdit_7.clear()
                self.ui.lineEdit_6.clear()
                screen = PRAE.geometry()
                size = self.geometry()
                self.move(screen.left() + (screen.width() - size.width()) / 2,
                          screen.top() + (screen.height() - size.height()) / 2)
                print('without network send2')
                self.publishform.show_w2('Network connect failed', self)
                print('without network send3')
                self.close()


    def show_w3(self, PRAE, row):
        self.ui.lineEdit_7.clear()
        self.ui.radioButton_2.setChecked(True)
        self.ui.label_52.setText(' ')
        try:
            print('contact send')
            ind = Core_func.QTableWidget.indexFromItem(
                    ex.ui.ContactsT, ex.ui.ContactsT.item(row, 1))
            self.ui.lineEdit_7.setText(ind.data())
            if ex.m_wallet.address == '':
                self.publishform.show_w2('Please Choose A Wallet', self)
                self.close()
            else:
                balance = requests.get(
                    "https://waltonchain.net:18950/api/getBalance/" + ex.m_wallet.address).json()
                a = str(balance)
                self.ui.label_52.setText(a.split(',')[1][11:] + 'WTCT')
                screen = PRAE.geometry()
                size = self.geometry()
                self.move(screen.left() + (screen.width() - size.width()) / 2,
                          screen.top() + (screen.height() - size.height()) / 2)
                self.exec_()
        except Exception as err:
            # ex.syncstatus = 0
            ex.refreshTop()
            self.ui.lineEdit_7.clear()
            self.ui.lineEdit_6.clear()
            # self.close()
            screen = PRAE.geometry()
            size = self.geometry()
            self.move(screen.left() + (screen.width() - size.width()) / 2,
                      screen.top() + (screen.height() - size.height()) / 2)
            self.publishform.show_w2('Network connect failed', self)
            self.exec_()


    def showenterphrase(self):
        try:
            #if ex.peers == 0:
            #    self.publishform.show_w2("peers connected is 0!", self)
             #   return
            ex.Trans.value = self.ui.lineEdit_6.text().strip()
            ex.Trans.Type = 'Send'
            ex.Trans.Gas = self.ui.lineEdit_8.text().strip()
            ex.Trans.Gasprice = self.ui.lineEdit_9.text().strip()
            if len(self.ui.lineEdit_7.text().strip())==42 and self.ui.lineEdit_7.text().strip()[0:2]=='0x':
                ex.Trans.toaddr = self.ui.lineEdit_7.text().strip()
            elif len(self.ui.lineEdit_7.text().strip())==40 and self.ui.lineEdit_7.text().strip()[0:2]!='0x':
                self.publishform.show_w2("Address without '0x'!", self)
                return
            else:
                self.publishform.show_w2("please enter a right address", self)
                return
            if ex.Trans.toaddr == ex.m_wallet.address:
                self.publishform.show_w2("Can not send to yourself!", self)
                return
            balance = requests.get(
                "https://waltonchain.net:18950/api/getBalance/" + ex.m_wallet.address).json()['Balance']
            if float(balance) <= 0:
                self.publishform.show_w2("The sum of amount must be more than 0!", self)
                return

            if float(ex.Trans.Gas) < 30000:
                self.publishform.show_w2("Gas limit must be more than 30000!", self)
                return

            if float(ex.Trans.Gasprice) < 0.000000018:
                self.publishform.show_w2("Gas price must be more than " + '0.000000018' + "!", self)
                return

            if self.ui.lineEdit_6.text().strip() == '' or self.ui.lineEdit_6.text().strip() == '0':
                self.publishform.show_w2("Please Enter Account!", self)
                return

            if float(ex.Trans.value) + float(ex.Trans.Gas) * float(ex.Trans.Gasprice) > float(balance) :
                self.publishform.show_w2("You don't have enough coins!", self)
                return
            self.enterpswform = enterpswform(self)
            print('enter')
            self.enterpswform.show_w2(ex.ui.lineEdit_8.text(), self, 1)
        except Exception as err:
            print("showenterphrase Error : " + str(err))
            pass
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            QApplication.postEvent(self, Core_func.QEvent(174))
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()

    def closeform(self):
        self.ui.lineEdit_7.clear()
        self.ui.lineEdit_6.clear()
        self.accountform.closeform(self)
        self.close()


class Example(QDialog, QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.init()

        # 起线程请求当前最新的块号
    #获取最新的块号
    def getLastBlock(self):
        if self.lastBlockGetting == False:
            self.lastBlockGetting = True
            from updata import getLastBlockThread
            self.getLastBlockThread = getLastBlockThread()
            self.getLastBlockThread.getLastBlockfinishSignal.connect(self.resetLastBlockThreadFlag)
            self.getLastBlockThread.start()

    def resetLastBlockThreadFlag(self,result):
        if result[0] == True:
            ApplicationHelper.lastBlock = result[1]
        self.lastBlockGetting = False

    ############################MyWallet 页的处理###################################################
    #每次显示MyWallet那一个table页的时候都初始化一下页面的信息 包括（余额，交易记录，交易记录上面的刷新时间，地址，密钥）
    def initMyWallet(self):
        if self.m_wallet.address == '':
            return
        #根据当前的钱包保存在配置文件中的数据先刷新界面
        self.refreshMWLocalData()
        #启动线程联网刷新市场数据
        self.getMWMarket()
        #启动一个线程去联网刷新余额，交易记录，nonce 等信息
        self.getMWTransactionListData()
        #启动一个线程联网刷新20天的交易信息
        self.getMWHistoryBalance()

    #根据保存的配置文件里面的记录进行刷新
    def refreshMWLocalData(self):
        #刷新交易信息
        self.showTransactions()
        #刷新余额变化趋势
        self.showBalance()

    #ui刷新余额折线图
    def showBalance(self):
        hbHelper = HistoryBalanceHelper()
        addressEntity = hbHelper.find(self.m_wallet.address)
        # 获取到多少天的余额记录
        iCount = len(addressEntity.HistoryBalanceList)

        graphicscene = QtWidgets.QGraphicsScene()
        dr = Figure_Canvas()
        graphicscene.addWidget(dr)
        # 有两个页面都要显示余额的数据，同时处理
        ##我的钱包页面中的余额
        self.ui.graphicsView.setScene(graphicscene)
        # 数据统计里面的余额
        self.ui.graphicsView_5.setScene(graphicscene)
        # 代表当前文件中没有该账号的20天余额记录
        if addressEntity.address == "" or iCount < 1:
            # 我的钱包页面中的余额
            self.ui.lineEdit_36.setText('')
            self.ui.lineEdit_37.setText('')
            self.ui.label_32.setPixmap(QPixmap(":/pic/GPoint.png"))
            self.ui.lineEdit_35.setText('Current: ' + '  WTCT')
            # 数据统计里面的余额
            self.ui.lineEdit_41.setText('')
            self.ui.lineEdit_42.setText('')
            # 绘制折线图的对象
            dr.y = [0]
            dr.x = [0]
            dr.axes.plot(dr.x, dr.y, 'r-', 1)
            dr.axes.set_axis_off()
            self.ui.graphicsView.show()
            self.ui.graphicsView_5.show()
            return

        dr.y = []
        dr.x = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]


        endEntity = addressEntity.HistoryBalanceList[0]
        startEntity = addressEntity.HistoryBalanceList[iCount-1]

        try:
            #跟新y轴的值
            for i in range(iCount):
                bEntity = addressEntity.HistoryBalanceList[i]
                dr.y.append(float(bEntity.history_balance))
            #绘制曲线
            dr.axes.plot(dr.x, dr.y, 'r-', 1)
            dr.axes.set_axis_off()
            self.ui.graphicsView.show()
            self.ui.graphicsView_5.show()
            #更新一些其他控件的内容

            strTimeStart = startEntity.utc_timestamp.split(" ")[0]
            strTimeEnd = endEntity.utc_timestamp.split(" ")[0]
         
            #我的钱包页面中的余额
            self.ui.lineEdit_36.setText(strTimeStart)
            self.ui.lineEdit_37.setText(strTimeEnd)
            self.ui.lineEdit_35.setText('Current: ' + str( int(endEntity.history_balance) / (10 ** 9)) + ' WTCT')
            if ( endEntity.history_balance / (10 ** 9)) < 5000:
                self.ui.label_32.setPixmap(QPixmap(":/pic/GPoint.png"))
            else:
                self.ui.label_32.setPixmap(QPixmap(":/pic/PPonit.png"))

            self.ui.lineEdit_41.setText(strTimeStart)
            self.ui.lineEdit_42.setText(strTimeEnd)
        except Exception as err:
            #出错就先不更新
            print("Error : " + str(err))
    #结合 transSendList和 transList 得到所有要显示的交易记录
    def getAllTransactions(self):
        # 有交易则 刷新交易记录上方 updata的时间
        transList = []
        #在translist中找到当前要显示的钱包地址的所有交易记录
        tHelper = TransactionList()
        addressEntity = tHelper.find(self.m_wallet.address)
        self.ui.lineEdit_31.setText(addressEntity.UpdateTime)
        #addressEntity 的length为0代表重来没有过交易信息，更不可能有转出信息（新创建的账户是没有钱的）
        if len(addressEntity.AccountTransactionsEntityList)==0:
            return  (False,transList)
        
        #将所有交易都放入列表中
        for i in range(len(addressEntity.AccountTransactionsEntityList)):
            transList.append(addressEntity.AccountTransactionsEntityList[i])

        #在transsendlist中找到当前要显示的钱包地址的所有交易记录
        tsHelper = TransactionSendListHelper()
        addressSendEntity = tsHelper.find(self.m_wallet.address)
        for i in range(len(addressSendEntity.TransactionSendList)):
            transSendEntity = addressSendEntity.TransactionSendList[i]
            #Success 代表在translist中已经有了，transSendlist中的数据就不需要了,所以在不是success的情况下就添加进去
            if transSendEntity.blockType != ApplicationHelper.transSuccess:
                AccountTransEntity = AccountTransactionsEntity()
                AccountTransEntity.setValue(transSendEntity)
                transList.append(AccountTransEntity)
        #返回之前对list按照 对象的时间属性进行排序
        if len(transList) > 1:
            transList.sort(key=functools.cmp_to_key(sortByTimeOfObj.date_compare),reverse=True)
        return (True,transList)
    #ui刷新交易记录
    def showTransactions(self):
        #清空
        self.ui.TransactionHistory.clear()
        #获取到所有交易记录
        result = self.getAllTransactions()
        if result[0] == False:
            self.ui.TransactionHistory.setRowCount(0)
            self.resetTraHisrefreshBtn()
            return

        allTransList = result[1]

        #跟新每一笔交易
        #根据当前钱包的交易记录数给tablewidget设置合适的行
        iCount = len(allTransList)
        #当前该地址没有数据则清空记录返回
        if iCount < 1:
            self.ui.TransactionHistory.setRowCount(0)
            self.resetTraHisrefreshBtn()
            return
        #设置新的行数
        self.ui.TransactionHistory.setRowCount(iCount+1)

        for i in range(iCount):
            accountTransEntity = allTransList[i]
            #设备每条记录是转出还是转入的图标
            item = QTableWidgetItem()
            #记录是转出还是转入 "-" 还是"+"
            transValue = ""
            #记录与之发生交易的账户，转出是addressTo 转入是addressFrom
            relatedAddress = ""
            if accountTransEntity.transType == ApplicationHelper.transSend:
                dela = QtGui.QIcon(":/pic/send3.png")
                item.setIcon(dela)
                transValue = '-' + str( accountTransEntity.value) + 'WTCT'
                relatedAddress = accountTransEntity.addressTo
            else:
                dela = QtGui.QIcon(":/pic/recieve3.png")
                item.setIcon(dela)
                transValue = '+' + str(accountTransEntity.value) + 'WTCT'
                relatedAddress = accountTransEntity.addressFrom
            #考虑应该要上锁，这个属于成员变量，如果仅刷新数据和线程请求完刷新数据同时操作可能有问题
            # 赋值给tableWidget的item
            self.ui.TransactionHistory.setItem(i, 0, item)
            self.ui.TransactionHistory.setItem(i, 1, QTableWidgetItem(accountTransEntity.utc_timestamp))
            self.ui.TransactionHistory.setItem(i, 2, QTableWidgetItem(relatedAddress))
            self.ui.TransactionHistory.setItem(i, 3, QTableWidgetItem(accountTransEntity.blockType))
            self.ui.TransactionHistory.setItem(i, 4, QTableWidgetItem(transValue))
            #更新我的钱包页面 刷新按钮的状态
        self.resetTraHisrefreshBtn()

    #联网获得市场信息
    def getMWMarket(self):
        #调用联网获取市场数据的方法，成功则进行刷新，否则不刷新
        pass

    # 联网刷新交易信息
    def getMWTransactionListData(self):
        #如果当前最新块号没有获取到则再次获取最新块号，只有有了最新块号才能请求到交易是否成功
        if ApplicationHelper.lastBlock == 0 :
            #进行最新块号的获取，并返回
            return
        #如果当前没有正在获取交易信息，则开启线程进行数据获取
        if self.transactionListGetting == False:
            self.transactionListGetting = True
            from updata import getTransactionDataThread
            self.getTransactionDataThread = getTransactionDataThread(self.m_wallet.address)
            self.getTransactionDataThread.getTransfinishSignal.connect(self.resetTransactionThreadFlag)
            self.getTransactionDataThread.start()

    #获取交易信息的线程结束信号的槽函数
    def resetTransactionThreadFlag(self, result,nonce):
        if result == True:
            #self.m_wallet.nonce = nonce
            self.showTransactions()
        self.transactionListGetting = False

    #联网获取近20天的余额变化
    def getMWHistoryBalance(self):
        if self.historyBalanceGetting == False:
            self.historyBalanceGetting = True
            from updata import getHistoryBalanceThread
            self.getHistoryBalanceThread = getHistoryBalanceThread(self.m_wallet.address)
            self.getHistoryBalanceThread.getBalancefinishSignal.connect(self.resetHistoryBalanceThreadFlag)
            self.getHistoryBalanceThread.start()

    #获取交易信息的线程结束信号的槽函数
    def resetHistoryBalanceThreadFlag(self, result):
        if result == True:
            self.showBalance()
        self.historyBalanceGetting = False

    ########################################################################################
    #######################更新Message 页签的内容###########################################
    def initMessage(self):
        self.refreshMeassageData()

        # 根据MyWallet的交易信息刷新Message页面

    def refreshMeassageData(self):
        try:
            # 清除原本tablewidget里面的内容
            self.ui.LogMessage.clear()
            # 反序列化，将文件内容转成对象
            tHelper = TransactionList()
            addressEntity = tHelper.find(self.m_wallet.address)
            iCount = len(addressEntity.AccountTransactionsEntityList)
            # addressEntity 的length为0代表重来没有过交易信息
            if iCount == 0:
                return
            # 设置显示message的条数
            self.ui.LogMessage.setRowCount(iCount + 1)
            print("iCount  = " + str(iCount))
            for i in range(iCount):
                accountTransEntity = addressEntity.AccountTransactionsEntityList[i]
                strContent = 'From:' + accountTransEntity.addressFrom.lower() + '\n' + 'To:' + accountTransEntity.addressTo.lower() + '\n' + 'Value:' + str(
                    accountTransEntity.value)
                print(str(i) + " = " + strContent)
                entityItem = QTableWidgetItem()
                entityItem.setData(0, accountTransEntity)
                self.ui.LogMessage.setItem(i, 0, QTableWidgetItem(accountTransEntity.transType))
                self.ui.LogMessage.setItem(i, 1, QTableWidgetItem(accountTransEntity.utc_timestamp))
                self.ui.LogMessage.setItem(i, 2, QTableWidgetItem(strContent))
                self.ui.LogMessage.setItem(i, 3, entityItem)

                # 除了显示的内容之外，一行保存一个对象，用来查看详细信息

        except Exception as err :
            print("refreshMeassageData Error : "+ str(err))

    def showMessageDetails(self):
        print("itemclick")
        try:
            currentItem = self.ui.LogMessage.currentItem()
            iRow = currentItem.row()
            transEntityItem = self.ui.LogMessage.item(iRow, 3)
            transEntity = transEntityItem.data(0)
            messformDialog = messform(self, transEntity)
            messformDialog.show()
        except Exception as err :
            print("showMessageDetails Error : " + str(err) )


    ########################################################################################




    def choosebtn(self, QTableWidgetItem):
        row = Core_func.QTableWidget.indexFromItem(
            self.ui.ContactsT, QTableWidgetItem).row()
        col = Core_func.QTableWidget.indexFromItem(
            self.ui.ContactsT, QTableWidgetItem).column()
        print(row, col)
        if col == 4:
            self.delcontact(row)
        if col == 3:
            self.editcontact(row)
        if col == 2:
            self.sendcontact(row)

    def walletbtn(self, QTableWidgetItem):
        row = Core_func.QTableWidget.indexFromItem(
            self.ui.multWallet, QTableWidgetItem).row()
        col = Core_func.QTableWidget.indexFromItem(
            self.ui.multWallet, QTableWidgetItem).column()
        print(row, col)
        if col == 5:
            self.savekey(row,0)
        if col == 4:
            self.delWallet(row)
        if col == 3:
            self.editwallet(row)
        if col == 2:
            self.openwallet(row,0)

    def buttonsdef(self, row):

        mwOpen = QPushButton(self)  # type: QPushButton
        mwOpen.setStyleSheet(''' border:0px; ''')
        mwOpen.setIcon(QIcon(":/pic/open1233.png"))
        mwOpen.setIconSize(QSize(80, 60))
        mwOpen.clicked.connect(lambda: self.openwallet(row,0))

        mwEdit = QPushButton(self)  # type: QPushButton
        mwEdit.setStyleSheet(''' border:0px; ''')
        mwEdit.setIcon(QIcon(":/pic/editA.png"))
        mwEdit.setIconSize(QSize(80, 60))
        mwEdit.clicked.connect(lambda: self.editwallet(row))

        mwDelete = QPushButton(self)  # type: QPushButton
        mwDelete.setStyleSheet(''' border:0px; ''')
        mwDelete.setIcon(QIcon(":/pic/deleteA.png"))
        mwDelete.setIconSize(QSize(80, 60))
        mwDelete.clicked.connect(lambda: self.delWallet(row))

        mwSaveKey = QPushButton(self)  # type: QPushButton
        mwSaveKey.setStyleSheet(''' border:0px; ''')
        mwSaveKey.setIcon(QIcon(":/pic/saveA.png"))
        mwSaveKey.setIconSize(QSize(70, 50))
        mwSaveKey.clicked.connect(lambda: self.savekey(row))

        consend = QPushButton(self)  # type: QPushButton
        consend.setStyleSheet(''' border:0px; ''')
        consend.setIcon(QIcon(":/pic/sendA.png"))
        consend.setIconSize(QSize(80, 60))
        consend.clicked.connect(lambda: self.sendcontact(row))

        conedit = QPushButton(self)  # type: QPushButton
        conedit.setStyleSheet(''' border:0px; ''')
        conedit.setIcon(QIcon(":/pic/editA.png"))
        conedit.setIconSize(QSize(80, 60))
        conedit.clicked.connect(lambda: self.editcontact(row))

        return (mwOpen, mwEdit, mwDelete, mwSaveKey, consend, conedit)

    def openWalletByAddress(self,address):
        self.setToolBoxVisible(True)
        self.ui.lineEdit_8.setText(address)
        self.pressbtn1()
        self.initMyWallet()

        '''
        try:
            self.m_wallet.nonce = requests.get(
                "https://waltonchain.net:18950/api/getSendTransactionNonce/" + address).json()[
                "send_nonce"]
        except Exception as err:
            print("Error: " + str(err))
        finally:
            self.initchart()
            self.ui.lineEdit_9.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_35.setIcon(QIcon(":/pic/08.png"))
            self.pressbtn1()
            self.refreshTop()
            self.privatekeyeye = 1
            self.ui.LogMessage.setRowCount(0)
            self.ui.TransactionHistory.setRowCount(0)
            self.refresh()
        '''


    def openwallet(self, row,new):
        if new == 0:
            ind = Core_func.QTableWidget.indexFromItem(
                self.ui.multWallet, self.ui.multWallet.item(row, 1))
            self.m_wallet.address = ind.data()
        self.openWalletByAddress(self.m_wallet.address)


    def editwallet(self, row):
        self.walletInfoform = walletInfoform(self)
        self.walletInfoform.show_w2(self, row)

    def delcontact(self, row):
        self.deleteform = deleteform(self)
        self.deleteform.show_w2(self,row,0)
        
    def sendcontact(self, row):
        print(row)
        self.sendform = sendform(self)
        self.sendform.show_w3(self, row)

    def editcontact(self, row):
        print(row)
        self.conInfoform = conInfoform(self)
        self.conInfoform.show_w2(row, self)

    # shift Pages tool btn

    def pressbtn1(self):
        self.setToolBoxNoHeighlight()
        self.ui.mywallet.setIcon(QIcon(":/pic/mywallet1.png"))
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.tabWidget.setCurrentIndex(0)
        self.ui.NewWalletstacked.setCurrentIndex(0)

        self.ui.lineEdit_23.setEchoMode(QLineEdit.Password)
        self.ui.pushButton_40.setIcon(QIcon(":/pic/08.png"))
        self.prieye = 1
        self.ui.pushButton_21.setIcon(QIcon(":/pic/disvispri.png"))
        self.ui.lineEdit_21.setEchoMode(QLineEdit.Password)
        self.ui.pushButton_41.setIcon(QIcon(":/pic/08.png"))
        self.passwordeye = 1
        self.ui.lineEdit_8.setText(self.m_wallet.address)
        if self.m_wallet.privateKey == '':
            if self.m_wallet.address != '':
                self.ui.lineEdit_9.setText(
                    '******************************************************************')
        else:
            self.ui.lineEdit_9.setText(self.m_wallet.privateKey)


    def pressbtn2(self):
        self.setToolBoxNoHeighlight()
        self.ui.statistic.setIcon(QIcon(":/pic/statistics1.png"))
        self.ui.stackedWidget.setCurrentIndex(2)

    def pressbtn3(self):
        self.setToolBoxNoHeighlight()
        self.ui.message.setIcon(QIcon(":/pic/message1.png"))
        self.ui.stackedWidget.setCurrentIndex(3)
        #展现message页面的时候，都去重新初始化一个这个页面的数据
        self.initMessage()

    def pressbtn4(self):
        self.setToolBoxNoHeighlight()
        self.ui.contact.setIcon(QIcon(":/pic/contact1.png"))
        self.ui.stackedWidget.setCurrentIndex(4)

    def pressbtn5(self):
        self.setToolBoxNoHeighlight()
        self.ui.mining.setIcon(QIcon(":/pic/mining1.png"))
        self.ui.stackedWidget.setCurrentIndex(5)

    def pressbtn6(self):
        self.setToolBoxNoHeighlight()
        self.ui.mw.setIcon(QIcon(":/pic/mw1.png"))
        self.ui.stackedWidget.setCurrentIndex(6)

    def pressbtn0(self):
        self.setToolBoxNoHeighlight()
        self.ui.cw.setIcon(QIcon(":/pic/cw1.png"))
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.importstack.setCurrentIndex(0)
        '''
        self.ui.lineEdit_23.setEchoMode(QLineEdit.Password)
        self.ui.pushButton_40.setIcon(QIcon(":/pic/08.png"))
        self.prieye = 1
        self.ui.pushButton_21.setIcon(QIcon(":/pic/disvispri.png"))
        self.ui.lineEdit_21.setEchoMode(QLineEdit.Password)
        self.ui.pushButton_41.setIcon(QIcon(":/pic/08.png"))
        self.passwordeye = 1
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_4.clear()
        '''

    def pressCreatNewWallet(self):
        self.ui.importstack.setCurrentIndex(1)
        self.ui.lineEdit_5.clear()
        self.ui.lineEdit_4.clear()

    def pressimportbykeystore(self):
        self.ui.importstack.setCurrentIndex(4)
        self.ui.lineEdit_26.clear()
        self.ui.lineEdit_6.clear()

    def presspressimportbyPri(self):
        self.ui.importstack.setCurrentIndex(2)
        self.ui.lineEdit_20.clear()
        self.ui.lineEdit_18.clear()
        self.ui.lineEdit_19.clear()

    def presspressimportbyMnem(self):
        self.ui.importstack.setCurrentIndex(3)
        self.ui.lineEdit_15.clear()
        self.ui.lineEdit_16.clear()
        self.ui.lineEdit_17.clear()

    def pressback2import(self):
        self.ui.importstack.setCurrentIndex(0)

    def generateKey(self):
        try:
            if len(self.ui.lineEdit_4.text().strip()) < 6:
                self.publishform.show_w2(
                    'Please enter at least 6 characters', self)
            elif self.ui.lineEdit_4.text().strip() != self.ui.lineEdit_5.text().strip():
                self.publishform.show_w2('Passphrases do not match', self)
            else:
                print("generateKey")
                ret = Core_func.Generate_Three_Key(
                    self.ui.lineEdit_4.text().strip(), self.ui.lineEdit_5.text().strip())
                print("jjj1_keystore_3")
                if ret[0] == 1:
                    print("jjj1_keystore_ret[0] == 1 ")
                    self.ui.stackedWidget.setCurrentIndex(1)
                    self.ui.tabWidget.setCurrentIndex(0)
                    self.ui.lineEdit_21.setText(self.ui.lineEdit_4.text().strip())
                    self.ui.lineEdit_22.setText(ret[1][0])
                    self.ui.lineEdit_23.setText(ret[1][1])
                    self.ui.lineEdit_25.setText(ret[1][0][0:10])
                    # self.ui.lineEdit_24.setText(ret[1][3])
                    encrypted = ret[1][2]
                    #self.m_wallet = Wallet
                    self.m_wallet.password = self.ui.lineEdit_4.text()
                    self.m_wallet.address = ret[1][0]
                    self.m_wallet.privateKey = ret[1][1]
                    self.m_wallet.accountname = self.ui.lineEdit_25.text()
                    # self.m_wallet.mnem = ret[1][3]
                    self.addWallet()
                    self.ui.lineEdit_8.setText(ret[1][0])
                    self.ui.lineEdit_9.setText(ret[1][1])
                    DataKeystore = pathConfig.keystoresPath +ret[1][0][2:18]+".keystore"
                    print("jjj1_keystore")
                    print(DataKeystore)
                    print("jjj2_keystore")
                    fh = open(DataKeystore, "w")
                    fh.write(str(encrypted))
                    fh.close()
                    self.m_wallet.filename = DataKeystore
                    self.imgpub = qrcode.make(self.m_wallet.address)
                    self.imgpub.save(pathConfig.keystoresPath + "public.png")
                    self.ui.label_10.setPixmap(QPixmap(pathConfig.keystoresPath + "public.png"))
                    self.ui.label_10.setAutoFillBackground(1)
                    self.imgpri = qrcode.make(ret[1][1])
                    self.imgpri.save(pathConfig.keystoresPath + "private.png")
                    self.ui.NewWalletstacked.setCurrentIndex(1)
                    self.setToolBoxNoHeighlight()
                else:
                    self.publishform.show_w2('error', self)
        except Exception as err:
            self.publishform.show_w2('generate failed', self)

    def importsecret(self):
        try:
            if len(self.ui.lineEdit_18.text().strip())<6:
                self.publishform.show_w2('Passphrases less than 6 characters', self)
            elif self.ui.lineEdit_18.text().strip() == self.ui.lineEdit_19.text().strip():
                enterpri = self.ui.lineEdit_20.text()
                a = enterpri.strip()
                if len(a) == 66 and a[0:2]=='0x':
                    a = a[2:]
                    ret = Core_func.Import_From_Private(
                        a, self.ui.lineEdit_19.text().strip())
                    if ret[0] == 1:
                        if len(self.walletroot.getElementsByTagName('WalletBaseEntity'))>0:
                            for i in range(len(self.walletroot.getElementsByTagName('WalletBaseEntity'))):
                                AddressTransactionsEntity = self.walletroot.getElementsByTagName(
                                    'WalletBaseEntity')[i]
                                if ret[1] == AddressTransactionsEntity.getElementsByTagName('Address')[
                                    0].firstChild.data:
                                    self.publishform.show_w2('Already Exists',self)
                                    return 1
                        self.m_wallet.password = self.ui.lineEdit_18.text().strip()
                        self.m_wallet.address = ret[1]
                        self.m_wallet.privateKey = self.ui.lineEdit_20.text().strip()
                        self.m_wallet.accountname = ret[1][0:10]
                        self.m_wallet.address = ret[1]
                        encrypted = ret[2]
                        DataKeystore = pathConfig.keystoresPath + ret[1][2:18] + ".keystore"
                        fh = open(DataKeystore, "w")
                        fh.write(str(encrypted))
                        fh.close()
                        self.m_wallet.filename = DataKeystore
                        self.addWallet()
                        self.ui.lineEdit_8.setText(ret[1])
                        self.ui.lineEdit_9.setText(self.ui.lineEdit_20.text())
                        self.imgpub = qrcode.make(self.m_wallet.address)
                        self.imgpub.save(pathConfig.keystoresPath + "public.png")
                        self.ui.stackedWidget.setCurrentIndex(1)
                        self.ui.tabWidget.setCurrentIndex(0)
                        self.ui.NewWalletstacked.setCurrentIndex(0)
                elif len(a) == 64 and a[0:2]!='0x':
                    ret = Core_func.Import_From_Private(
                        a, self.ui.lineEdit_19.text().strip())
                    if ret[0] == 1:
                        if len(self.walletroot.getElementsByTagName('WalletBaseEntity'))>0:
                            for i in range(len(self.walletroot.getElementsByTagName('WalletBaseEntity'))):
                                AddressTransactionsEntity = self.walletroot.getElementsByTagName(
                                    'WalletBaseEntity')[i]
                                if ret[1] == AddressTransactionsEntity.getElementsByTagName('Address')[
                                    0].firstChild.data:
                                    self.publishform.show_w2('Already Exists',self)
                                    return 1
                        self.m_wallet.password = self.ui.lineEdit_18.text().strip()
                        self.m_wallet.address = ret[1]
                        self.m_wallet.privateKey = self.ui.lineEdit_20.text().strip()
                        self.m_wallet.accountname = ret[1][0:10]
                        self.m_wallet.address = ret[1]
                        encrypted = ret[2]
                        DataKeystore = pathConfig.keystoresPath + ret[1][2:18] + ".keystore"
                        fh = open(DataKeystore, "w")
                        fh.write(str(encrypted))
                        fh.close()
                        self.m_wallet.filename = DataKeystore
                        self.addWallet()
                        self.ui.lineEdit_8.setText(ret[1])
                        self.ui.lineEdit_9.setText(self.ui.lineEdit_20.text())
                        self.imgpub = qrcode.make(self.m_wallet.address)
                        self.imgpub.save(pathConfig.keystoresPath + "public.png")
                        self.ui.stackedWidget.setCurrentIndex(1)
                        self.ui.tabWidget.setCurrentIndex(0)
                        self.ui.NewWalletstacked.setCurrentIndex(0)
                    else:
                        self.publishform.show_w2(
                            'Please enter right password', self)
                else:
                    self.publishform.show_w2('Private Key is illegal', self)
            else:
                self.publishform.show_w2('Passphrases do not match', self)
        except Exception as err:
            self.publishform.show_w2(str(err), self)

    def importmnemonic(self):
        ret = Core_func.Import_mnemonic(self.ui.lineEdit_15.text(
        ), self.ui.lineEdit_16.text(), self.ui.lineEdit_17.text())
        if ret[0] == 1:

            encrypted = ret[1][2]
            # self.m_wallet = Wallet
            self.m_wallet.password = self.ui.lineEdit_15.text().strip()
            self.m_wallet.address = ret[1][0]
            self.m_wallet.privateKey = ret[1][1]
            self.m_wallet.accountname = ret[1][0:10]
            ret1 = self.addWallet()
            if ret1 != 1:
                self.ui.lineEdit_8.setText(ret[1][0])
                self.ui.lineEdit_9.setText(ret[1][1])
                DataKeystore = pathConfig.keystoresPath +ret[1][0][2:18] + ".keystore"
                fh = open(DataKeystore, "w")
                fh.write(str(encrypted))
                fh.close()
                self.m_wallet.filename = DataKeystore
                self.imgpub = qrcode.make(self.m_wallet.address)
                self.imgpub.save(pathConfig.keystoresPath + "public.png")
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.tabWidget.setCurrentIndex(0)
                self.ui.NewWalletstacked.setCurrentIndex(0)
        else:
            self.publishform.show_w2('error', self)

    def importfile(self):
        filename, _ = QFileDialog.getOpenFileName(
            self, 'Open File', os.getenv('HOME'))


        self.ui.lineEdit_26.setText(filename)

    def importKetstore(self):
        try:
            fh = ''
            if self.ui.lineEdit_26.text() != '':
                if QFile.exists(self.ui.lineEdit_26.text()):
                    fh = QFile(self.ui.lineEdit_26.text())

                if not fh.open(QFile.ReadOnly):
                    QtGui.qApp.quit()

                data = fh.readAll()
                codec = QTextCodec.codecForUtfText(data)
                content = codec.toUnicode(data)
                print(content)
                if self.ui.lineEdit_26.text()[-5:] == 'store':
                    enterpri = self.ui.lineEdit_20.text()
                    enterpri.strip()
                    if len(self.ui.lineEdit_6.text().strip()) >= 6:
                        ret = Core_func.Import_Keystore(self.ui.lineEdit_6.text().strip(), content)
                        #登录成功
                        if ret[0] == 1:
                            if len(self.walletroot.getElementsByTagName('WalletBaseEntity'))>0:
                                for i in range(len(self.walletroot.getElementsByTagName('WalletBaseEntity'))):
                                    AddressTransactionsEntity = self.walletroot.getElementsByTagName(
                                        'WalletBaseEntity')[i]
                                    if ret[1][0] == AddressTransactionsEntity.getElementsByTagName('Address')[
                                        0].firstChild.data:
                                        self.publishform.show_w2('Already Exists',self)
                                        return 1
                            self.m_wallet.password = self.ui.lineEdit_6.text()
                            self.m_wallet.address = ret[1][0]
                            print(len(self.m_wallet.address))
                            self.m_wallet.privateKey = ret[1][1]
                            self.m_wallet.accountname = ret[1][0][0:10]
                            encrypted = ret[2]
                            DataKeystore =  pathConfig.keystoresPath + ret[1][0][2:18] + ".keystore"
                            fh = open(DataKeystore, "w")
                            fh.write(str(encrypted))
                            fh.close()
                            self.m_wallet.filename = DataKeystore
                            self.addWallet()

                            self.ui.lineEdit_8.setText(ret[1][0])
                            self.ui.lineEdit_9.setText(ret[1][1])
                            self.imgpub = qrcode.make(self.m_wallet.address)
                            self.imgpub.save(pathConfig.keystoresPath + "public.png")
                            self.ui.stackedWidget.setCurrentIndex(1)
                            self.ui.tabWidget.setCurrentIndex(0)
                            self.ui.NewWalletstacked.setCurrentIndex(0)

                        else:
                            self.publishform.show_w2(
                                'Please enter right password', self)
                    else:
                        self.publishform.show_w2(
                            'Please enter at least 6 characters', self)
                else:
                    self.publishform.show_w2('Please choose a right Keystore', self)
            else:
                self.publishform.show_w2('Please choose a right Keystore', self)
        except Exception as err:
            self.publishform.show_w2('import failed', self)
    
    def seepassword(self):
        if self.passwordeye == 1:
            self.ui.lineEdit_21.setEchoMode(0)
            self.ui.lineEdit_21.setText(self.m_wallet.password)
            self.ui.pushButton_41.setIcon(QIcon(":/pic/01.png"))
            self.passwordeye = 0
        else:
            self.ui.lineEdit_21.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_41.setIcon(QIcon(":/pic/08.png"))
            self.passwordeye = 1

    def seeprivatekey(self):
        if self.privatekeyeye == 1:
            self.enterpswform = enterpswform(self)
            self.enterpswform.show_w2(self.ui.lineEdit_8.text(), self)
            print(self.ui.lineEdit_8.text())
            # self.ui.lineEdit_9.setText(self.m_wallet.privateKey)

        else:
            self.ui.lineEdit_9.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_35.setIcon(QIcon(":/pic/08.png"))
            self.ui.pushButton_43.setIcon(QIcon(":/pic/QRC.png"))
            self.privatekeyeye = 1

    def seeprivateqrcode(self):
        if self.privatekeyeye == 0:
            self.imgpub = qrcode.make(self.ui.lineEdit_9.text())
            self.imgpub.save(pathConfig.keystoresPath + "private.png")
            self.prikeyform = prikeyform(self)
            self.prikeyform.show_w2(self)

    def seeprikey(self):
        if self.prieye == 1:
            self.ui.lineEdit_23.setEchoMode(0)
            self.ui.lineEdit_23.setText(self.m_wallet.privateKey)
            self.ui.pushButton_40.setIcon(QIcon(":/pic/01.png"))
            self.prieye = 0
            self.ui.pushButton_21.setIcon(QIcon(pathConfig.keystoresPath + "private.png"))
        else:
            self.ui.lineEdit_23.setEchoMode(QLineEdit.Password)
            self.ui.pushButton_40.setIcon(QIcon(":/pic/08.png"))
            self.prieye = 1
            # self.ui.label_11.setPixmap(QPixmap(":/pic/disvispri.png"))
            self.ui.pushButton_21.setIcon(QIcon(":/pic/disvispri.png"))

    def isExistWalletInMultiWallets(self):
        for i in range(self.ui.multWallet.rowCount()):
            itemData = Core_func.QTableWidget.indexFromItem(self.ui.multWallet, self.ui.multWallet.item(i, 1))
            if self.m_wallet.address == itemData.data():
                return True
        return False


    #向multi wallet 里面添加钱包，并将新增的数据写入配置文件
    def addWallet(self):
        #先判断该钱包在multiwallet页面是否已经存在，若不存在则添加，否则不操作
        if self.isExistWalletInMultiWallets() == False:
            Rcount = self.ui.multWallet.rowCount()
            self.ui.multWallet.setRowCount(Rcount + 1)
            newItemAddr = QTableWidgetItem(self.m_wallet.address)
            newItemName = QTableWidgetItem(self.m_wallet.accountname)
            self.ui.multWallet.setItem(Rcount, 1, newItemAddr)
            self.ui.multWallet.setItem(Rcount, 0, newItemName)
            newItemdel = QTableWidgetItem('   Delete   ')
            newItemdel.setForeground(QBrush(QColor(135, 0, 255)))
            newItemdel.setFlags(QtCore.Qt.ItemIsEnabled)
            newItemopen = QTableWidgetItem('    Open    ')
            newItemopen.setForeground(QBrush(QColor(135, 0, 255)))
            newItemopen.setFlags(QtCore.Qt.ItemIsEnabled)

            newItemedit = QTableWidgetItem('    Edit    ')
            newItemedit.setForeground(QBrush(QColor(135, 0, 255)))
            newItemedit.setFlags(QtCore.Qt.ItemIsEnabled)

            newItemsave = QTableWidgetItem('  Save key  ')
            newItemsave.setForeground(QBrush(QColor(135, 0, 255)))
            newItemsave.setFlags(QtCore.Qt.ItemIsEnabled)

            self.ui.multWallet.setItem(Rcount, 2, newItemopen)
            self.ui.multWallet.setItem(Rcount, 3, newItemedit)
            self.ui.multWallet.setItem(Rcount, 4, newItemdel)
            self.ui.multWallet.setItem(Rcount, 5, newItemsave)
            #界面钱包添加好了之后再将信息保存到配置文件中
            #获取key文件的路径
            DataKeystore = pathConfig.keystoresPath + self.m_wallet.address[2:18] + ".keystore"
            #添加到保存钱包信息的文件中去
            Core_func.addwalletxml(
                self.walletdom, self.walletroot, self.m_wallet.accountname, self.m_wallet.address, DataKeystore)

            #将该钱包的交易信息保存到trans.xml文件中
            if len(self.transroot.getElementsByTagName('AddressTransactionsEntity')) == 0:
                Core_func.addtransaddrxml(self.transdom, self.transroot, self.m_wallet.address,
                                          time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            else:
                for i in range(len(self.transroot.getElementsByTagName('AddressTransactionsEntity'))):
                    AddressTransactionsEntity = self.transroot.getElementsByTagName(
                        'AddressTransactionsEntity')[i]
                    if self.m_wallet.address == AddressTransactionsEntity.getElementsByTagName('Address')[
                        0].firstChild.data:
                        break
                    if i == len(self.transroot.getElementsByTagName('AddressTransactionsEntity')) - 1:
                        Core_func.addtransaddrxml(self.transdom, self.transroot, self.m_wallet.address,
                                                  time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            #导入钱包成功之后打开新导入的钱包
            self.openwallet(Rcount, 1)






    def delWallet(self, row):
        self.deleteform = deleteform(self)
        self.deleteform.show_w2(self,row,1)

    def savekey(self, row, new):
        if new == 0:
            ind = Core_func.QTableWidget.indexFromItem(
                self.ui.multWallet, self.ui.multWallet.item(row, 1))
            filename = pathConfig.keystoresPath + ind.data()[2:18] + ".keystore"
            if os.path.isfile(filename):
                file_object = open(filename)
                all_the_text = file_object.read()

                fsave_keystore = QFileDialog.getSaveFileName(self, 'Save Your Keystore File', '.',
                                                            'keystore(*.keystore)')
                if fsave_keystore[0]:
                    file_save_keystore = open(fsave_keystore[0], 'w')
                    with file_save_keystore:
                        data = file_save_keystore.write(all_the_text)
        else:
            filename = pathConfig.keystoresPath + self.m_wallet.address[2:18] + ".keystore"
            if os.path.isfile(filename):
                file_object = open(filename)
                all_the_text = file_object.read()

                fsave_keystore = QFileDialog.getSaveFileName(self, 'Save Your Keystore File', '.',
                                                            'keystore(*.keystore)')
                if fsave_keystore[0]:
                    file_save_keystore = open(fsave_keystore[0], 'w')
                    with file_save_keystore:
                        data = file_save_keystore.write(all_the_text)
                # file_save_keystore

    def savename(self):
        if self.ui.lineEdit_25.text().strip()=='':
            self.publishform.show_w2('please enter the name', self)
            return
        else:
            self.m_wallet.accountname = self.ui.lineEdit_25.text().strip()
        Rcount = self.ui.multWallet.rowCount()
        self.ui.multWallet.setRowCount(Rcount)
        newItemAddr = QTableWidgetItem(self.m_wallet.address)
        newItemName = QTableWidgetItem(self.m_wallet.accountname)
        self.ui.multWallet.setItem(Rcount-1, 1, newItemAddr)
        self.ui.multWallet.setItem(Rcount-1, 0, newItemName)
        newItemdel = QTableWidgetItem('   Delete   ')
        newItemdel.setForeground(QBrush(QColor(135, 0, 255)))
        newItemdel.setFlags(QtCore.Qt.ItemIsEnabled)
        newItemopen = QTableWidgetItem('    Open    ')
        newItemopen.setForeground(QBrush(QColor(135, 0, 255)))
        newItemopen.setFlags(QtCore.Qt.ItemIsEnabled)

        newItemedit = QTableWidgetItem('    Edit    ')
        newItemedit.setForeground(QBrush(QColor(135, 0, 255)))
        newItemedit.setFlags(QtCore.Qt.ItemIsEnabled)

        newItemsave = QTableWidgetItem('  Save key  ')
        newItemsave.setForeground(QBrush(QColor(135, 0, 255)))
        newItemsave.setFlags(QtCore.Qt.ItemIsEnabled)

        self.ui.multWallet.setItem(Rcount-1, 2, newItemopen)
        self.ui.multWallet.setItem(Rcount-1, 3, newItemedit)
        self.ui.multWallet.setItem(Rcount-1, 4, newItemdel)
        self.ui.multWallet.setItem(Rcount-1, 5, newItemsave)

        Core_func.editwalletxml(
            self.walletdom, self.walletroot, self.m_wallet.accountname, Rcount-1)
        self.publishform.show_w2('Saved successfully', self)

    def copyPublicKey(self):
        self.clipboard_public_key = QApplication.clipboard()
        self.clipboard_public_key.setText(self.m_wallet.address)

    def copymnemword(self):
        self.clipboard_public_key = QApplication.clipboard()
        self.clipboard_public_key.setText(self.m_wallet.mnem)

    def toreddit(self):
        webbrowser.open('https://www.reddit.com/r/waltonchain/')

    def totwitter(self):
        webbrowser.open('https://twitter.com/Waltonchain')

    def totme(self):
        webbrowser.open('https://t.me/waltonchain_en')

    def tostack(self):
        webbrowser.open(
            'https://join.slack.com/t/waltonchain/shared_invite/enQtMjgxMDcxNzU5MDEwLWI1ZTc3MDZlNmI4ZjA1YjhiMDEzN2VlZmY2M2EzNmM4Yjg1NjFjYjlmNTcxOGVlMGRiNWE2M2NlYTg2MWNmNWQ')

    def seepass1(self):
        if self.pass1eye == 1:
            PASS = self.ui.lineEdit_4.text()
            self.ui.lineEdit_4.setEchoMode(0)
            self.ui.lineEdit_4.setText(PASS)
            self.ui.turn2visible1.setIcon(QIcon(":/pic/01.png"))
            self.pass1eye = 0
        else:
            self.ui.lineEdit_4.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1.setIcon(QIcon(":/pic/02.png"))
            self.pass1eye = 1

    def seepass2(self):
        if self.pass2eye == 1:
            PASS = self.ui.lineEdit_5.text()
            self.ui.lineEdit_5.setEchoMode(0)
            self.ui.lineEdit_5.setText(PASS)
            self.ui.turn2visible2.setIcon(QIcon(":/pic/01.png"))
            self.pass2eye = 0
        else:
            self.ui.lineEdit_5.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible2.setIcon(QIcon(":/pic/02.png"))
            self.pass2eye = 1

    def seepri1(self):
        if self.pri1eye == 1:
            # time.sleep(5)
            PASS = self.ui.lineEdit_20.text()
            self.ui.lineEdit_20.setEchoMode(0)
            self.ui.lineEdit_20.setText(PASS)
            self.ui.turn2visible1_9.setIcon(QIcon(":/pic/01.png"))
            self.pri1eye = 0
        else:
            self.ui.lineEdit_20.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_9.setIcon(QIcon(":/pic/02.png"))
            self.pri1eye = 1

    def seephrs1(self):
        if self.phrs1eye == 1:
            PASS = self.ui.lineEdit_18.text()
            self.ui.lineEdit_18.setEchoMode(0)
            self.ui.lineEdit_18.setText(PASS)
            self.ui.turn2visible1_8.setIcon(QIcon(":/pic/01.png"))
            self.phrs1eye = 0
        else:
            self.ui.lineEdit_18.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_8.setIcon(QIcon(":/pic/02.png"))
            self.phrs1eye = 1

    def seephrs2(self):
        if self.phrs1eye == 1:
            PASS = self.ui.lineEdit_19.text()
            self.ui.lineEdit_19.setEchoMode(0)
            self.ui.lineEdit_19.setText(PASS)
            self.ui.turn2visible2_5.setIcon(QIcon(":/pic/01.png"))
            self.phrs1eye = 0
        else:
            self.ui.lineEdit_19.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible2_5.setIcon(QIcon(":/pic/02.png"))
            self.phrs1eye = 1

    def seepassK(self):
        if self.passKeye == 1:
            PASS = self.ui.lineEdit_6.text()
            self.ui.lineEdit_6.setEchoMode(0)
            self.ui.lineEdit_6.setText(PASS)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/01.png"))
            self.passKeye = 0
        else:
            self.ui.lineEdit_6.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_2.setIcon(QIcon(":/pic/02.png"))
            self.passKeye = 1

    def seemnem1(self):
        if self.mnemeye == 1:
            PASS = self.ui.lineEdit_17.text()
            self.ui.lineEdit_17.setEchoMode(0)
            self.ui.lineEdit_17.setText(PASS)
            self.ui.turn2visible1_7.setIcon(QIcon(":/pic/01.png"))
            self.mnemeye = 0
        else:
            self.ui.lineEdit_17.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_7.setIcon(QIcon(":/pic/02.png"))
            self.mnemeye = 1

    def seephrm1(self):
        if self.phrm1eye == 1:
            PASS = self.ui.lineEdit_15.text()
            self.ui.lineEdit_15.setEchoMode(0)
            self.ui.lineEdit_15.setText(PASS)
            self.ui.turn2visible1_6.setIcon(QIcon(":/pic/01.png"))
            self.phrm1eye = 0
        else:
            self.ui.lineEdit_15.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible1_6.setIcon(QIcon(":/pic/02.png"))
            self.phrm1eye = 1

    def seephrm2(self):
        if self.phrm2eye == 1:
            PASS = self.ui.lineEdit_16.text()
            self.ui.lineEdit_16.setEchoMode(0)
            self.ui.lineEdit_16.setText(PASS)
            self.ui.turn2visible2_4.setIcon(QIcon(":/pic/01.png"))
            self.phrm2eye = 0
        else:
            self.ui.lineEdit_16.setEchoMode(QLineEdit.Password)
            self.ui.turn2visible2_4.setIcon(QIcon(":/pic/02.png"))
            self.phrm2eye = 1

    def purple2black(self):
        print(self.ui.LogMessage.rowCount())
        for i in range(self.ui.LogMessage.rowCount()):  # self.lastblacknum,
            self.ui.LogMessage.item(i, 0).setForeground(
                QBrush(QColor(0, 0, 0)))
            self.ui.LogMessage.item(i, 1).setForeground(
                QBrush(QColor(0, 0, 0)))
            self.ui.LogMessage.item(i, 2).setForeground(
                QBrush(QColor(0, 0, 0)))

        self.lastblacknum = self.ui.LogMessage.rowCount()

    def startmining(self):
        try:
            if self.startstop == 1:
                if not(len(self.ui.lineEdit_7.text().strip())== 42 and self.ui.lineEdit_7.text().strip()[0:2]=='0x'):
                    self.publishform.show_w2('Please enter a right address', self)
                elif len(self.w3.admin.peers) == 0:
                    self.publishform.show_w2('need peers connected', self)
                else:
                    self.startstop = 0
                    self.miningtatus = 1
                    self.refreshTop()
                    self.ui.pushButton_30.setStyleSheet("border-width: 1px;"
                                                        "border-color: rgb(135, 0, 255);"
                                                        "background-color: rgb(135, 0, 255);"
                                                        "color: rgb(255, 255, 255);"
                                                        "border-radius:20px;"
                                                        "border-style:solid; ")
                    self.ui.pushButton_30.setText('Stop Mining')
                    ######################################

                    ######################################
                    self.ui.radioButton.setEnabled(0)
                    self.ui.radioButton_2.setEnabled(0)
                    self.ui.radioButton_3.setEnabled(0)
                    self.ui.radioButton_4.setEnabled(0)
                    self.ui.radioButton_5.setEnabled(0)
                    self.ui.radioButton_6.setEnabled(0)
                    self.ui.lineEdit_7.setEnabled(0)
                    self.ui.pushButton_29.setEnabled(0)
                    self.ui.horizontalSlider.setEnabled(0)
                    if self.cpumode == 1:
                        try:
                            self.w3.miner.setEtherBase(
                                self.ui.lineEdit_7.text().strip())
                            self.w3.miner.start(self.cpures)
                            print(self.cpures)
                            self.ui.lineEdit_10.setText(
                                str(Core_func.getDifficulty()[1][0][1]))
                            r = Core_func.getTransactionRecord_day(self.ui.lineEdit_7.text(), '2')[
                                1][0]['history_balance']
                            if (int(r))/(10**9) < 5000:
                                self.ui.lineEdit_12.setText('2')
                            else:
                                self.ui.lineEdit_12.setText('3')
                            self.ui.lineEdit_11.setText(str(self.w3.eth.hashrate))
                        except Exception as err:
                            # self.w3.miner.stop()
                            self.refreshmininfo()
                            self.startstop = 0
                            self.miningtatus = 0
                            self.publishform.show_w2('check your network', self)
                            self.startmining()
                            
                    else:
                        print('gpu')
            else:
                self.startstop = 1
                self.miningtatus = 0
                self.w3.miner.stop()
                self.refreshTop()
                self.ui.lineEdit_11.setText('0')
                ######################################


                ######################################
                self.ui.pushButton_30.setStyleSheet("border-width: 1px;"
                                                    "border-color: rgb(135, 0, 255);"
                                                    "background-color: rgb(255, 255, 255);"
                                                    "color: rgb(135, 0, 255);"
                                                    "border-radius:20px;"
                                                    "border-style:solid; ")
                self.ui.pushButton_30.setText('Start Mining')
                self.ui.radioButton.setEnabled(1)
                # self.ui.radioButton_2.setEnabled(1)
                self.ui.radioButton_3.setEnabled(1)
                self.ui.radioButton_4.setEnabled(1)
                self.ui.radioButton_5.setEnabled(1)
                self.ui.radioButton_6.setEnabled(1)
                self.ui.lineEdit_7.setEnabled(1)
                self.ui.pushButton_29.setEnabled(1)
                self.ui.horizontalSlider.setEnabled(1)
        except Exception as err:
            self.publishform.show_w2(str(err), self)

    def changecpu(self):
        self.ui.radioButton_3.setEnabled(1)
        self.ui.radioButton_4.setEnabled(1)
        self.ui.radioButton_5.setEnabled(1)
        self.ui.radioButton_6.setEnabled(1)
        self.ui.horizontalSlider.setEnabled(1)
        self.cpumode = 1

    def changegpu(self):
        self.ui.radioButton_3.setEnabled(0)
        self.ui.radioButton_4.setEnabled(0)
        self.ui.radioButton_5.setEnabled(0)
        self.ui.radioButton_6.setEnabled(0)
        self.ui.horizontalSlider.setEnabled(0)
        self.cpumode = 0

    def changereg(self):
        print('change1')
        self.cpures = 1
        if not self.ui.horizontalSlider.value() == 1:
            
            self.ui.horizontalSlider.setValue(1)
            self.ui.horizontalSlider.setVisible(0)
            self.ui.horizontalSlider.setVisible(1)
            print('change11')
        print('change2')

    def changefast(self):
        self.cpures = 2
        if not self.ui.horizontalSlider.value() == 2:
            self.ui.horizontalSlider.setValue(2)
            self.ui.horizontalSlider.setVisible(0)
            self.ui.horizontalSlider.setVisible(1)

    def changesfast(self):
        self.cpures = 3
        if not self.ui.horizontalSlider.value() == 3:
            self.ui.horizontalSlider.setValue(3)
            self.ui.horizontalSlider.setVisible(0)
            self.ui.horizontalSlider.setVisible(1)

    def changeefast(self):
        self.cpures = 4
        if not self.ui.horizontalSlider.value() == 4:
            self.ui.horizontalSlider.setValue(4)
            self.ui.horizontalSlider.setVisible(0)
            self.ui.horizontalSlider.setVisible(1)

    def changespeed(self, a):

        if a == 1:
            if self.ui.radioButton_4.isChecked() == False:
                print('set 11111')
                self.ui.radioButton_4.setChecked(True)
        if a == 2:
            if self.ui.radioButton_3.isChecked() == False:

                self.ui.radioButton_3.setChecked(True)
        if a == 3:
            if self.ui.radioButton_6.isChecked() == False:
                self.ui.radioButton_6.setChecked(True)
        if a == 4:
            if self.ui.radioButton_5.isChecked() == False:
                self.ui.radioButton_5.setChecked(True)

    def operate(self):
        # self.refresh()
        print('tick')

    def refresh(self):
        return
        try:
            if os.path.isfile(pathConfig.lastSettingPath +'test.xml'):
                print('refresh1')
                if len(self.transroot.getElementsByTagName('AddressTransactionsEntity'))>=0:
                    print('refresh2')
                    try:
                        self.newblock = Core_func.getLatestBlock()[1]
                    except Exception as err:
                        self.refreshTop()
                        return 1
                    for AddressTransactionsEntity in self.transroot.getElementsByTagName('AddressTransactionsEntity'):
                        if AddressTransactionsEntity.getElementsByTagName('Address')[0].firstChild.data == self.m_wallet.address:
                            if len(AddressTransactionsEntity.getElementsByTagName('TransactionList')) > 0:
                                TransactionList = AddressTransactionsEntity.getElementsByTagName('TransactionList')[
                                    0]

                                if len(TransactionList.getElementsByTagName('AccountTransactionsEntity')) == 0:
                                    ret = Core_func.getTransactionRecord(
                                        self.m_wallet.address)
                                    if ret[0] == 1:
                                        self.ui.TransactionHistory.setRowCount(0)

                                        for i in range(len(ret[1])):
                                            Transrow = self.ui.TransactionHistory.rowCount()
                                            self.ui.TransactionHistory.setRowCount(
                                                Transrow+1)
                                            if int(self.newblock) - int(ret[1][i]['blockNumber']) > 11:
                                                newItemblockType = QTableWidgetItem(
                                                    'Success')
                                            else:
                                                print(int(self.newblock))
                                                print('my block:'+str(int(ret[1][i]['blockNumber'])))
                                                if (int(self.newblock) - int(ret[1][i]['blockNumber'])) >= 0:
                                                    newItemblockType = QTableWidgetItem(
                                                        str(int(self.newblock) - int(ret[1][i]['blockNumber']))+'/12')
                                                else:
                                                    newItemblockType = QTableWidgetItem(
                                                        '0/12')
                                            if self.m_wallet.address.lower() == ret[1][i]['addressFrom']:
                                                item = QTableWidgetItem()
                                                dela = QtGui.QIcon(':/pic/send3.png')
                                                item.setIcon(dela)
                                                newItemvalue = QTableWidgetItem(
                                                    '-' + str(ret[1][i]['value']) + 'WTCT')
                                                newItemtoaddr = QTableWidgetItem(
                                                    ret[1][i]['addressTo'])
                                            else:
                                                item = QTableWidgetItem()
                                                dela = QtGui.QIcon(':/pic/recieve3.png')
                                                item.setIcon(dela)
                                                newItemtoaddr = QTableWidgetItem(
                                                    ret[1][i]['addressFrom'])
                                                newItemvalue = QTableWidgetItem(
                                                    str(ret[1][i]['value']) + 'WTCT')
                                            time_s = datetime.datetime.strptime(
                                                ret[1][i]['utc_timestamp'], "%Y-%m-%d %H:%M:%S")
                                            localtime = Core_func.utc2local(time_s)
                                            newItemTime = QTableWidgetItem(
                                                localtime.strftime('%Y-%m-%d %H:%M:%S'))
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 0, item)
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 1, newItemTime)
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 2, newItemtoaddr)
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 3, newItemblockType)
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 4, newItemvalue)
                                else:
                                    ret = Core_func.getTransactionRecord(
                                        self.m_wallet.address)
                                    self.ui.TransactionHistory.setRowCount(0)
                                    print(len(TransactionList.getElementsByTagName('AccountTransactionsEntity')))
                                    curi=0
                                    for i in range(len(TransactionList.getElementsByTagName('AccountTransactionsEntity'))):
                                        print(i)
                                        AccountTransactionsEntity = TransactionList.getElementsByTagName(
                                            'AccountTransactionsEntity')[curi]
                                        if ret[0] == 1:
                                            for j in range(len(ret[1])):
                                                if ret[1][j]['tx_hash'] == AccountTransactionsEntity.getElementsByTagName('tx_hash')[0].firstChild.data:
                                                    AccountTransactionsEntity.parentNode.removeChild(
                                                        AccountTransactionsEntity)
                                                    break
                                                if j == len(ret[1])-1:
                                                    curi=curi+1
                                            
                                    f = open(pathConfig.lastSettingPath +'test.xml', 'w')
                                    self.transdom.writexml(f, addindent=' ', newl='\n')
                                    f.close()
                                    print(
                                        'submit:  '+str(len(TransactionList.getElementsByTagName('AccountTransactionsEntity'))))
                                    a = range(len(TransactionList.getElementsByTagName(
                                        'AccountTransactionsEntity')))
                                    for i in range(len(TransactionList.getElementsByTagName(
                                        'AccountTransactionsEntity'))):
                                        print('sub+'+str(i))
                                        AccountTransactionsEntity = TransactionList.getElementsByTagName(
                                            'AccountTransactionsEntity')[i]
                                        self.ui.TransactionHistory.insertRow(0)
                                        utc_times = AccountTransactionsEntity.getElementsByTagName('utc_timestamp')[
                                            0].childNodes
                                        time_s = datetime.datetime.strptime(
                                            utc_times[0].nodeValue, "%Y-%m-%d %H:%M:%S")
                                        localtime = Core_func.utc2local(time_s)
                                        newItemtime = QTableWidgetItem(
                                            localtime.strftime('%Y-%m-%d %H:%M:%S'))
                                        newItemblockType = QTableWidgetItem('Submitted')
                                        if AccountTransactionsEntity.getElementsByTagName('transType')[0].firstChild.data == 'Send':
                                            newItemvalue = QTableWidgetItem(
                                                '-' + AccountTransactionsEntity.getElementsByTagName('value')[
                                                    0].firstChild.data + 'WTCT')
                                            item = QTableWidgetItem()
                                            dela = QtGui.QIcon(':/pic/send3.png')
                                            item.setIcon(dela)
                                            newItemtoaddr = QTableWidgetItem(
                                                AccountTransactionsEntity.getElementsByTagName('addressTo')[0].firstChild.data)

                                        else:
                                            item = QTableWidgetItem()
                                            dela = QtGui.QIcon(':/pic/recieve3.png')
                                            item.setIcon(dela)
                                            newItemtoaddr = QTableWidgetItem(
                                                AccountTransactionsEntity.getElementsByTagName('addressFrom')[
                                                    0].firstChild.data)
                                            newItemvalue = QTableWidgetItem(
                                                AccountTransactionsEntity.getElementsByTagName('value')[0].firstChild.data + 'WTCT')
                                        self.ui.TransactionHistory.setItem(0, 0, item)
                                        self.ui.TransactionHistory.setItem(
                                            0, 1, newItemtime)
                                        self.ui.TransactionHistory.setItem(
                                            0, 2, newItemtoaddr)
                                        self.ui.TransactionHistory.setItem(
                                            0, 3, newItemblockType)
                                        self.ui.TransactionHistory.setItem(
                                            0, 4, newItemvalue)
                                        print('refresh sub')
                                    ret = Core_func.getTransactionRecord(
                                        self.m_wallet.address)
                                    if ret[0] == 1:
                                        for i in range(len(ret[1])):
                                            Transrow = self.ui.TransactionHistory.rowCount()
                                            self.ui.TransactionHistory.setRowCount(
                                                Transrow+1)
                                            if int(self.newblock) - int(ret[1][i]['blockNumber']) > 11:
                                                newItemblockType = QTableWidgetItem(
                                                    'Success')
                                            else:
                                                if (int(self.newblock) - int(ret[1][i]['blockNumber'])) >= 0:
                                                    newItemblockType = QTableWidgetItem(
                                                        str(int(self.newblock) - int(ret[1][i]['blockNumber']))+'/12')
                                                else:
                                                    newItemblockType = QTableWidgetItem(
                                                        '0/12')
                                            if self.m_wallet.address.lower() == ret[1][i]['addressFrom']:
                                                item = QTableWidgetItem()
                                                dela = QtGui.QIcon(':/pic/send3.png')
                                                item.setIcon(dela)
                                                newItemvalue = QTableWidgetItem(
                                                    '-' + str(ret[1][i]['value']) + 'WTCT')
                                                newItemtoaddr = QTableWidgetItem(
                                                    ret[1][i]['addressTo'])
                                            else:
                                                item = QTableWidgetItem()
                                                dela = QtGui.QIcon(':/pic/recieve3.png')
                                                item.setIcon(dela)
                                                newItemtoaddr = QTableWidgetItem(
                                                    ret[1][i]['addressFrom'])
                                                newItemvalue = QTableWidgetItem(
                                                    str(ret[1][i]['value']) + 'WTCT')
                                            time_s = datetime.datetime.strptime(
                                                ret[1][i]['utc_timestamp'], "%Y-%m-%d %H:%M:%S")
                                            localtime = Core_func.utc2local(time_s)
                                            newItemTime = QTableWidgetItem(
                                                localtime.strftime('%Y-%m-%d %H:%M:%S'))
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 0, item)
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 1, newItemTime)
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 2, newItemtoaddr)
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 3, newItemblockType)
                                            self.ui.TransactionHistory.setItem(
                                                Transrow, 4, newItemvalue)
                    if self.ui.TransactionHistory.rowCount()==0:
                        ret = Core_func.getTransactionRecord(
                                    self.m_wallet.address)
                        if ret[0] == 1:
                            self.ui.TransactionHistory.setRowCount(0)

                            for i in range(len(ret[1])):
                                Transrow = self.ui.TransactionHistory.rowCount()
                                self.ui.TransactionHistory.setRowCount(
                                    Transrow + 1)
                                if int(self.newblock) - int(ret[1][i]['blockNumber']) > 11:
                                    newItemblockType = QTableWidgetItem(
                                        'Success')
                                else:
                                    print(int(self.newblock))
                                    print('my block:' + str(int(ret[1][i]['blockNumber'])))
                                    if (int(self.newblock) - int(ret[1][i]['blockNumber'])) >= 0:
                                        newItemblockType = QTableWidgetItem(
                                            str(int(self.newblock) - int(ret[1][i]['blockNumber'])) + '/12')
                                    else:
                                        newItemblockType = QTableWidgetItem(
                                            '0/12')
                                if self.m_wallet.address.lower() == ret[1][i]['addressFrom']:
                                    item = QTableWidgetItem()
                                    dela = QtGui.QIcon(':/pic/send3.png')
                                    item.setIcon(dela)
                                    newItemvalue = QTableWidgetItem(
                                        '-' + str(ret[1][i]['value']) + 'WTCT')
                                    newItemtoaddr = QTableWidgetItem(
                                        ret[1][i]['addressTo'])
                                else:
                                    item = QTableWidgetItem()
                                    dela = QtGui.QIcon(':/pic/recieve3.png')
                                    item.setIcon(dela)
                                    newItemtoaddr = QTableWidgetItem(
                                        ret[1][i]['addressFrom'])
                                    newItemvalue = QTableWidgetItem(
                                        str(ret[1][i]['value']) + 'WTCT')
                                time_s = datetime.datetime.strptime(
                                    ret[1][i]['utc_timestamp'], "%Y-%m-%d %H:%M:%S")
                                localtime = Core_func.utc2local(time_s)
                                newItemTime = QTableWidgetItem(
                                    localtime.strftime('%Y-%m-%d %H:%M:%S'))
                                self.ui.TransactionHistory.setItem(
                                    Transrow, 0, item)
                                self.ui.TransactionHistory.setItem(
                                    Transrow, 1, newItemTime)
                                self.ui.TransactionHistory.setItem(
                                    Transrow, 2, newItemtoaddr)
                                self.ui.TransactionHistory.setItem(
                                    Transrow, 3, newItemblockType)
                                self.ui.TransactionHistory.setItem(
                                    Transrow, 4, newItemvalue)
            self.ui.lineEdit_31.setText(time.strftime(
                '%Y/%m/%d %H:%M:%S', time.localtime(time.time())))
            # self.initchart()
            self.refreshlog()
        except Exception as err:
            # self.publishform.show_w2('please check your network',self)
            # self.syncstatus = 0
            # self.peers = 0
            self.refreshTop()

    def refreshlog(self):
        return
        try:
            print(self.ui.LogMessage.rowCount())
            ret = Core_func.getTransactionRecord(self.m_wallet.address)
            if ret[0] == 1:
                if self.ui.LogMessage.rowCount() == 0:
                    for i in range(len(ret[1])):
                        logrowcount = self.ui.LogMessage.rowCount()
                        self.ui.LogMessage.setRowCount(logrowcount+1)
                        newItemContent = QTableWidgetItem(
                            'From:' + ret[1][i]['addressFrom'] + '\n' + 'To:' +
                            ret[1][i]['addressTo'] + '\n' + 'Value:' +
                            str(ret[1][i]['value']) + '                                                                                                                                                                             ' + '\n' + 'tx_hash:' +
                            ret[1][i]['tx_hash'])
                        if self.m_wallet.address.lower() == ret[1][i]['addressFrom']:
                            newItemType = QTableWidgetItem('Send')
                        else:
                            newItemType = QTableWidgetItem('Recieve')
                        time_s = datetime.datetime.strptime(
                            ret[1][i]['utc_timestamp'], "%Y-%m-%d %H:%M:%S")
                        localtime = Core_func.utc2local(time_s)
                        newItemTime = QTableWidgetItem(
                            localtime.strftime('%Y-%m-%d %H:%M:%S'))
                        self.ui.LogMessage.setItem(logrowcount, 0, newItemType)
                        self.ui.LogMessage.setItem(logrowcount, 1, newItemTime)
                        self.ui.LogMessage.setItem(logrowcount, 2, newItemContent)
                else:
                    ind = Core_func.QTableWidget.indexFromItem(
                        self.ui.LogMessage, self.ui.LogMessage.item(0, 2))
                    print(ind.data().split('tx_hash')[1][1:])
                    self.foundmeslog = 0
                    for i in range(len(ret[1])):
                        if ret[1][i]['tx_hash'] == ind.data().split('tx_hash')[1][1:]:
                            self.foundmeslog = i
                            break
                        if i == 19:
                            self.ui.LogMessage.setRowCount(0)
                            for i in range(len(ret[1])):
                                logrowcount = self.ui.LogMessage.rowCount()
                                self.ui.LogMessage.setRowCount(logrowcount + 1)
                                newItemContent = QTableWidgetItem(
                                    'From:' + ret[1][i]['addressFrom'] + '\n' + 'To:' +
                                    ret[1][i]['addressTo'] + '\n' + 'Value:' +
                                    str(ret[1][i]['value']) + '                                                                                                                                                                           ' + '\n' + 'tx_hash:' +
                                    ret[1][i]['tx_hash'])
                                if self.m_wallet.address.lower() == ret[1][i]['addressFrom']:
                                    newItemType = QTableWidgetItem('Send')
                                else:
                                    newItemType = QTableWidgetItem('Recieve')
                                time_s = datetime.datetime.strptime(
                                    ret[1][i]['utc_timestamp'], "%Y-%m-%d %H:%M:%S")
                                localtime = Core_func.utc2local(time_s)
                                newItemTime = QTableWidgetItem(
                                    localtime.strftime('%Y-%m-%d %H:%M:%S'))
                                self.ui.LogMessage.setItem(
                                    logrowcount, 0, newItemType)
                                self.ui.LogMessage.setItem(
                                    logrowcount, 1, newItemTime)
                                self.ui.LogMessage.setItem(
                                    logrowcount, 2, newItemContent)
                    a = range(self.foundmeslog)
                    for i in reversed(a):
                        self.ui.LogMessage.insertRow(0)
                        newItemContent = QTableWidgetItem(
                            'From:' + ret[1][i]['addressFrom'] + '\n' + 'To:' +
                            ret[1][i]['addressTo'] + '\n' + 'Value:' +
                            str(ret[1][i]['value']) + '                                                                                                                                                                                    ' + '\n' + 'tx_hash:' +
                            ret[1][i]['tx_hash'])
                        if self.m_wallet.address.lower() == ret[1][i]['addressFrom']:
                            newItemType = QTableWidgetItem('Send')
                        else:
                            newItemType = QTableWidgetItem('Recieve')
                        time_s = datetime.datetime.strptime(
                            ret[1][i]['utc_timestamp'], "%Y-%m-%d %H:%M:%S")
                        localtime = Core_func.utc2local(time_s)
                        newItemTime = QTableWidgetItem(
                            localtime.strftime('%Y-%m-%d %H:%M:%S'))
                        self.ui.LogMessage.setItem(0, 0, newItemType)
                        self.ui.LogMessage.setItem(0, 1, newItemTime)
                        self.ui.LogMessage.setItem(0, 2, newItemContent)
        except Exception as err:
            # self.publishform.show_w2('please check your network',self)
            # self.syncstatus = 0
            self.refreshTop()
        

    def refreshTop(self):
        try:
            self.peers = len(self.w3.admin.peers)
            if self.peers == 0:
                self.syncstatus = 0
                self.miningtatus = 0
                self.ui.lineEdit_11.setText('0')
                return 0
            else:
                if str(self.w3.eth.syncing) == 'False':
                    self.syncstatus = 1
                try:
                    #r1 = requests.get("https://waltonchain.net:18950/api/getGasPrice").json()
                    #print('jj peers= '+str(self.peers))
                    if self.waite_net == 1:
                        self.initMarket()
                        self.initmap()
                        self.initchart()
                        self.refreshmininfo()

                        self.waite_net = 0
                    if self.waite_miningtatus == 1:
                        self.miningtatus = 1
                        self.waite_miningtatus = 0
                    if self.miningtatus == 1:
                        self.ui.lineEdit_11.setText(str(self.w3.eth.hashrate))
                except Exception as err:
                    self.syncstatus = 0
                    self.peers = 0
                    self.waite_net = 1
                    if self.miningtatus == 1:
                        self.ui.lineEdit_11.setText('0')
                        self.miningtatus = 0
                        self.waite_miningtatus = 1
            self.UpdateTopGUI()
        except Exception as err:
            print("Error :" + err)
            self.syncstatus = 0
            self.peers = 0
            self.waite_net = 1
            if self.miningtatus == 1:
                self.ui.lineEdit_11.setText('0')
                self.miningtatus = 0
                self.waite_miningtatus = 1
            self.UpdateTopGUI()
            subprocess.Popen('walton.exe', shell=True)
            #print('j1 once walton')
    
    def initMarket(self):
        try:
            drMarket = Figure_Canvas()
            ret2 = drMarket.testM()
            nowtime = datetime.datetime.now()
            detaday = datetime.timedelta(days=31)
            da_days = nowtime - detaday
            graphicsceneM = QtWidgets.QGraphicsScene()
            graphicsceneM.addWidget(drMarket)
            self.ui.graphicsView_2.setScene(graphicsceneM)  #
            self.ui.graphicsView_2.show()
            self.ui.lineEdit_39.setText(str(ret2) + ' USD')
    
            self.ui.lineEdit_38.setText(da_days.strftime('%Y-%m-%d'))
            self.ui.lineEdit_40.setText(nowtime.strftime('%Y-%m-%d'))
    
            retM = Core_func.getTokenMarket()
            if retM[0] == 1:
                closing = retM[1][len(retM[1]) - 1]['TokenPriceUSD']
                opening = retM[1][0]['TokenPriceUSD']
                lowest = retM[1][0]['TokenPriceUSD']
                highest = retM[1][0]['TokenPriceUSD']
                for i in range(len(retM[1])):
                    d = retM[1][i]['TokenPriceUSD']
                    if lowest > d:
                        lowest = d
                    if highest < d:
                        highest = d
                self.ui.lineEdit_27.setText(str(highest))
                self.ui.lineEdit_28.setText(str(lowest))
                self.ui.lineEdit_29.setText(str(opening))
                self.ui.lineEdit_30.setText(str(closing))
        except Exception as err:
            pass

    def initMingres(self):
        try:
            if len(self.ui.lineEdit_7.text().strip())== 42 and self.ui.lineEdit_7.text().strip()[0:2]=='0x':
                drR = Figure_Canvas()
                ret4 = drR.testR(self.ui.lineEdit_7.text().strip())
                graphicsceneR = QtWidgets.QGraphicsScene()
                graphicsceneR.addWidget(drR)
                self.ui.graphicsView_6.setScene(graphicsceneR)
                self.ui.graphicsView_6.show()
                if self.ui.lineEdit_7.text().strip() == '':
                    self.ui.lineEdit_43.setText('')
                    self.ui.lineEdit_44.setText('')
                    self.ui.lineEdit_45.setText('')
                else:
                    ret3 = Core_func.getMiningRecord(self.ui.lineEdit_7.text().strip())
                    miningnum = len(ret3[1])
                    
                    self.ui.lineEdit_43.setText('')
                    self.ui.lineEdit_44.setText('')
                    self.ui.lineEdit_45.setText('')
                    self.ui.lineEdit_46.setText('')
                    if miningnum != 0 and ret3[0]==1:
                        if ret4[1] == 0:
                            time_end = datetime.datetime.strptime(ret3[1][0]['timestamp'], "%Y-%m-%d %H:%M:%S")
                            self.ui.lineEdit_46.setText(time_end.strftime('%Y-%m-%d'))
                        else:
                            time_start = datetime.datetime.strptime(ret3[1][miningnum - 1]['timestamp'], "%Y-%m-%d %H:%M:%S")
                            time_end = datetime.datetime.strptime(ret3[1][0]['timestamp'], "%Y-%m-%d %H:%M:%S")
                            self.ui.lineEdit_43.setText(time_start.strftime('%Y-%m-%d'))
                            self.ui.lineEdit_44.setText(time_end.strftime('%Y-%m-%d'))
                        self.ui.lineEdit_45.setText(str(ret4[0]))
            elif len(self.ui.lineEdit_7.text().strip())!= 0:
                self.publishform.show_w2('invalid address',self)
        except Exception as err:
            # self.publishform.show_w2('please check your network',self)
            # self.syncstatus = 0
            # self.peers = 0
            self.refreshTop()

    def UpdateTopGUI(self):
        if self.syncstatus == 0:
            self.ui.toolButton_25.setText(' Syncing')
            self.ui.toolButton_25.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_25.setIcon(QIcon(":/pic/grayqukuai.png"))
            self.ui.toolButton_21.setText(' Syncing')
            self.ui.toolButton_21.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_21.setIcon(QIcon(":/pic/grayqukuai.png"))
            self.ui.toolButton_28.setText(' Syncing')
            self.ui.toolButton_28.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_28.setIcon(QIcon(":/pic/grayqukuai.png"))
            self.ui.toolButton_37.setText(' Syncing')
            self.ui.toolButton_37.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_37.setIcon(QIcon(":/pic/grayqukuai.png"))
            self.ui.toolButton_39.setText(' Syncing')
            self.ui.toolButton_39.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_39.setIcon(QIcon(":/pic/grayqukuai.png"))
            self.ui.toolButton_31.setText(' Syncing')
            self.ui.toolButton_31.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_31.setIcon(QIcon(":/pic/grayqukuai.png"))
            self.ui.toolButton_34.setText(' Syncing')
            self.ui.toolButton_34.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_34.setIcon(QIcon(":/pic/grayqukuai.png"))
        else:
            self.ui.toolButton_25.setText(' Completed')
            self.ui.toolButton_25.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_25.setIcon(QIcon(":/pic/puperqukuai.png"))
            self.ui.toolButton_21.setText(' Completed')
            self.ui.toolButton_21.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_21.setIcon(QIcon(":/pic/puperqukuai.png"))
            self.ui.toolButton_28.setText(' Completed')
            self.ui.toolButton_28.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_28.setIcon(QIcon(":/pic/puperqukuai.png"))
            self.ui.toolButton_31.setText(' Completed')
            self.ui.toolButton_31.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_31.setIcon(QIcon(":/pic/puperqukuai.png"))
            self.ui.toolButton_34.setText(' Completed')
            self.ui.toolButton_34.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_34.setIcon(QIcon(":/pic/puperqukuai.png"))
            self.ui.toolButton_37.setText(' Completed')
            self.ui.toolButton_37.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_37.setIcon(QIcon(":/pic/puperqukuai.png"))
            self.ui.toolButton_39.setText(' Completed')
            self.ui.toolButton_39.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_39.setIcon(QIcon(":/pic/puperqukuai.png"))
        if self.miningtatus == 0:
            self.ui.lineEdit_11.setText('0')
            self.ui.toolButton_26.setText(' Mining')
            self.ui.toolButton_26.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_26.setIcon(QIcon(":/pic/graymining.png"))
            self.ui.toolButton_22.setText(' Mining')
            self.ui.toolButton_22.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_22.setIcon(QIcon(":/pic/graymining.png"))
            self.ui.toolButton_29.setText(' Mining')
            self.ui.toolButton_29.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_29.setIcon(QIcon(":/pic/graymining.png"))
            self.ui.toolButton_32.setText(' Mining')
            self.ui.toolButton_32.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_32.setIcon(QIcon(":/pic/graymining.png"))
            self.ui.toolButton_35.setText(' Mining')
            self.ui.toolButton_35.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_35.setIcon(QIcon(":/pic/graymining.png"))
            self.ui.toolButton_38.setText(' Mining')
            self.ui.toolButton_38.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_38.setIcon(QIcon(":/pic/graymining.png"))
            self.ui.toolButton_41.setText(' Mining')
            self.ui.toolButton_41.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_41.setIcon(QIcon(":/pic/graymining.png"))
        else:
            self.ui.lineEdit_11.setText(str(self.w3.eth.hashrate))
            self.ui.toolButton_26.setText(' Mining')
            self.ui.toolButton_26.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_26.setIcon(QIcon(":/pic/mining1.png"))
            self.ui.toolButton_29.setText(' Mining')
            self.ui.toolButton_29.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_29.setIcon(QIcon(":/pic/mining1.png"))
            self.ui.toolButton_22.setText(' Mining')
            self.ui.toolButton_22.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_22.setIcon(QIcon(":/pic/mining1.png"))
            self.ui.toolButton_32.setText(' Mining')
            self.ui.toolButton_32.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_32.setIcon(QIcon(":/pic/mining1.png"))
            self.ui.toolButton_35.setText(' Mining')
            self.ui.toolButton_35.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_35.setIcon(QIcon(":/pic/mining1.png"))
            self.ui.toolButton_38.setText(' Mining')
            self.ui.toolButton_38.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_38.setIcon(QIcon(":/pic/mining1.png"))
            self.ui.toolButton_41.setText(' Mining')
            self.ui.toolButton_41.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_41.setIcon(QIcon(":/pic/mining1.png"))
        if self.peers == 0:
            self.ui.toolButton_24.setText(' Peers Connected:0')
            self.ui.toolButton_24.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_24.setIcon(QIcon(":/pic/tubiaoer.png"))
            self.ui.toolButton_23.setText(' Peers Connected:0')
            self.ui.toolButton_23.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_23.setIcon(QIcon(":/pic/tubiaoer.png"))
            self.ui.toolButton_27.setText(' Peers Connected:0')
            self.ui.toolButton_27.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_27.setIcon(QIcon(":/pic/tubiaoer.png"))
            self.ui.toolButton_30.setText(' Peers Connected:0')
            self.ui.toolButton_30.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_30.setIcon(QIcon(":/pic/tubiaoer.png"))
            self.ui.toolButton_36.setText(' Peers Connected:0')
            self.ui.toolButton_36.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_36.setIcon(QIcon(":/pic/tubiaoer.png"))
            self.ui.toolButton_33.setText(' Peers Connected:0')
            self.ui.toolButton_33.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_33.setIcon(QIcon(":/pic/tubiaoer.png"))
            self.ui.toolButton_40.setText(' Peers Connected:0')
            self.ui.toolButton_40.setStyleSheet(
                'color: rgb(100, 100, 100);border:0px;')
            self.ui.toolButton_40.setIcon(QIcon(":/pic/tubiaoer.png"))
        else:
            self.ui.toolButton_24.setText(
                ' Peers Connected:' + str(self.peers))
            self.ui.toolButton_24.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_24.setIcon(QIcon(":/pic/tubiao1.png"))
            self.ui.toolButton_23.setText(
                ' Peers Connected:' + str(self.peers))
            self.ui.toolButton_23.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_23.setIcon(QIcon(":/pic/tubiao1.png"))
            self.ui.toolButton_27.setText(
                ' Peers Connected:' + str(self.peers))
            self.ui.toolButton_27.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_27.setIcon(QIcon(":/pic/tubiao1.png"))
            self.ui.toolButton_33.setText(
                ' Peers Connected:' + str(self.peers))
            self.ui.toolButton_33.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_33.setIcon(QIcon(":/pic/tubiao1.png"))
            self.ui.toolButton_36.setText(
                ' Peers Connected:' + str(self.peers))
            self.ui.toolButton_36.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_36.setIcon(QIcon(":/pic/tubiao1.png"))
            self.ui.toolButton_30.setText(
                ' Peers Connected:' + str(self.peers))
            self.ui.toolButton_30.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_30.setIcon(QIcon(":/pic/tubiao1.png"))
            self.ui.toolButton_40.setText(
                ' Peers Connected:' + str(self.peers))
            self.ui.toolButton_40.setStyleSheet(
                'color: #8700ff;border:0px;')
            self.ui.toolButton_40.setIcon(QIcon(":/pic/tubiao1.png"))

    def initchart(self):
        if self.IsnitchartThreadstarted == False:
            self.IsnitchartThreadstarted = True
            from updata import initchartThread
            dr = Figure_Canvas()
            self.initchartThread = initchartThread(dr,self.m_wallet.address)
            #self.initchartThread.finishSignal.connect(self.UpdateBalanceGUI)
            self.initchartThread.start()
        self.getMWTransactionListData()

    def initmining(self):
        try:
            if len(self.ui.lineEdit_7.text().strip())== 42 and self.ui.lineEdit_7.text().strip()[0:2]=='0x':
                ret5 = Core_func.getMiningRecord(self.ui.lineEdit_7.text().strip())
                self.ui.miningHistory.setRowCount(0)
                for i in range(len(ret5[1])):
                    Rcount = self.ui.miningHistory.rowCount()
                    self.ui.miningHistory.setRowCount(Rcount + 1)
                    time_s = datetime.datetime.strptime(
                        ret5[1][i]['utc_timestamp'], "%Y-%m-%d %H:%M:%S")
                    localtime = Core_func.utc2local(time_s)
                    newItemtime = QTableWidgetItem(
                        localtime.strftime('%Y-%m-%d %H:%M:%S'))
                    #newItemtime = QTableWidgetItem(ret5[1][i]['timestamp'])
                    newItemblock = QTableWidgetItem(str(ret5[1][i]['blockNumer']))
                    newItemreward = QTableWidgetItem(
                        str(ret5[1][i]['totol_reward'])+' WTCT')

                    self.ui.miningHistory.setItem(Rcount, 0, newItemtime)
                    self.ui.miningHistory.setItem(Rcount, 1, newItemblock)
                    self.ui.miningHistory.setItem(Rcount, 2, newItemreward)
            elif len(self.ui.lineEdit_7.text().strip())!= 0:
                self.publishform.show_w2('invalid address',self)
        except Exception as err:
            self.refreshTop()
        self.ui.lineEdit_32.setText(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time())))

    def initcontact(self):
        try:
            if os.path.isfile(pathConfig.lastSettingPath +'test.xml'):
                if len(self.addrroot.getElementsByTagName('AddressEntity')) != 0:
                    for AddressEntity in self.addrroot.getElementsByTagName('AddressEntity'):
                        Rcount = self.ui.ContactsT.rowCount()
                        self.ui.ContactsT.setRowCount(Rcount + 1)
                        itemlist1 = AddressEntity.getElementsByTagName(
                            'AccountName')
                        item1 = itemlist1[0]
                        itemlist2 = AddressEntity.getElementsByTagName('Address')
                        item2 = itemlist2[0]

                        newItemname = QTableWidgetItem(item1.firstChild.data)
                        newItemaddr = QTableWidgetItem(item2.firstChild.data)

                        newItemdel = QTableWidgetItem('   delete   ')
                        newItemdel.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemdel.setFlags(QtCore.Qt.ItemIsEnabled)
                        newItemsend = QTableWidgetItem('    send    ')
                        newItemsend.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemsend.setFlags(QtCore.Qt.ItemIsEnabled)
                        newItemedit = QTableWidgetItem('    edit    ')
                        newItemedit.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemedit.setFlags(QtCore.Qt.ItemIsEnabled)

                        self.ui.ContactsT.setItem(Rcount, 0, newItemname)
                        self.ui.ContactsT.setItem(Rcount, 1, newItemaddr)
                        self.ui.ContactsT.setItem(Rcount, 2, newItemsend)
                        self.ui.ContactsT.setItem(Rcount, 3, newItemedit)
                        self.ui.ContactsT.setItem(Rcount, 4, newItemdel)
            else:
                print('')
        except Exception as err:
            self.publishform.show_w2('refresh failed',self)

    def initwallets(self):
        try:
            print('go to find   ./wa.xml')
            if os.path.isfile(pathConfig.lastSettingPath + 'Wallets.xml'):  # address
                url = pathConfig.lastSettingPath + 'Wallets.xml'
                print('find   ./wa.xml')
                if len(self.walletroot.getElementsByTagName('WalletBaseEntity')) - self.ui.multWallet.rowCount() > 0:
                    self.ui.multWallet.setRowCount(0)
                    for WalletEntity in self.walletroot.getElementsByTagName('WalletBaseEntity'):
                        Rcount = self.ui.multWallet.rowCount()
                        self.ui.multWallet.setRowCount(Rcount + 1)
                        print(Rcount)
                        itemlist1 = WalletEntity.getElementsByTagName(
                            'AccountName')
                        item1 = itemlist1[0]
                        itemlist2 = WalletEntity.getElementsByTagName('Address')
                        item2 = itemlist2[0]

                        newItemname = QTableWidgetItem(item1.firstChild.data)
                        newItemaddr = QTableWidgetItem(item2.firstChild.data)

                        self.ui.multWallet.setItem(Rcount, 0, newItemname)
                        self.ui.multWallet.setItem(Rcount, 1, newItemaddr)

                        newItemdel = QTableWidgetItem('   Delete   ')
                        newItemdel.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemdel.setFlags(QtCore.Qt.ItemIsEnabled)
                        newItemopen = QTableWidgetItem('    Open    ')
                        newItemopen.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemopen.setFlags(QtCore.Qt.ItemIsEnabled)

                        newItemedit = QTableWidgetItem('    Edit    ')
                        newItemedit.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemedit.setFlags(QtCore.Qt.ItemIsEnabled)

                        newItemsave = QTableWidgetItem('  Save key  ')
                        newItemsave.setForeground(QBrush(QColor(135, 0, 255)))
                        newItemsave.setFlags(QtCore.Qt.ItemIsEnabled)

                        self.ui.multWallet.setItem(Rcount, 2, newItemopen)
                        self.ui.multWallet.setItem(Rcount, 3, newItemedit)
                        self.ui.multWallet.setItem(Rcount, 4, newItemdel)
                        self.ui.multWallet.setItem(Rcount, 5, newItemsave)
            else:
                print('  wallet  failed')
        except Exception as err:
            print(str(err))
            # self.publishform.show_w2('refresh failed',self)

    def initmap(self):
        pen = QPen()
        pen.setColor(QColor(255, 0, 0))
        pen.setBrush(QColor(255, 0, 0))
        try:
            source = Core_func.getCurrentNodesDistribution()
            sou = json.dumps(source[1]).strip('}')
            rce = sou.split(',')
        except Exception as err:
            return 1    
        graphicsceneCR = QtWidgets.QGraphicsScene()
        nodemax = 0
        self.nationlist = ('AU', 3330, 1505,
                           'BR', 1370, 1365,
                           'CN', 3030, 865,
                           'CA', 690, 520,
                           'DE', 2005, 640,
                           'FR', 1920, 705,
                           'GB', 1880, 620,
                           'HK', 3115, 1000,
                           'IN', 2730, 1000,
                           'JP', 3375, 830,
                           'KR', 3255, 835,
                           'MY', 2985, 1195,
                           'RU', 2980, 480,
                           'SG', 3000, 1220,
                           'TH', 2275, 1070,
                           'US', 820, 795,

                           'AE', 2485, 1000,
                           'AR', 1225, 1635,
                           'BE', 1960, 667,
                           'BG', 2180, 778,
                           'GR', 2150, 820,
                           'RO', 2175, 730,
                           'TR', 2260, 820,
                           'BY', 2200, 625,
                           'PL', 2125, 645,
                           'DK', 2025, 590,
                           'EE', 2185, 550,
                           'CZ', 2070, 680,
                           'FI', 2200, 465,
                           'SE', 2080, 485,
                           'NO', 1995, 515,
                           'CH', 1998, 720,
                           'IT', 2045, 760,
                           'NL', 1970, 645,
                           'IE', 1830, 630,
                           'AT', 2065, 710,
                           'SI', 2080, 733,
                           'YU', 2135, 760,
                           'ES', 1870, 805,
                           'PT', 1825, 815,
                           'CY ', 2265, 868,
                           'MD', 2215, 715,
                           'CL', 1140, 1670,
                           'CO', 1120, 1215,
                           'NZ', 3785, 1695,
                           'TW', 3190, 990,
                           'IL', 2310, 915,
                           'DO', 1175, 1050,
                           'LU', 1990, 680,
                           'GE', 2375, 780,
                           'CR', 1020, 1152,
                           'HU', 2110, 720,
                           'CU', 1080, 1025,
                           'LV', 2180, 575,
                           'LT', 2165, 602,
                           'MA', 1830, 915,
                           'PE', 1095, 1350,
                           'PR', 1205, 1060,
                           'SK', 2120, 695,
                           'AM', 2390, 805,
                           'TJ', 2655, 825,
                           'TM', 2520, 815,
                           'ZA', 2165, 1595,

                           'LY', 2090, 960,
                           'NG', 1990, 1160,
                           'ID', 3120, 1270,
                           'MX', 815, 1000,
                           'PK', 2650, 930,
                           'VN', 3065, 1125,
                           'VE', 1210, 1180,
                           'SA', 2380, 1000,
                           'KH', 3025, 1125,
                           'AZ', 2420, 803,
                           'MM', 2930, 1025,
                           'EC', 1075, 1270,
                           'HN', 990, 1095,
                           'IS', 1710, 450,
                           'JM', 1088, 1061,
                           'JO', 2300, 920,
                           'SN', 1755, 1105,
                           'SC', 2505, 1304,
                           'UA', 2245, 690,
                           'UY', 1315, 1615)
        for i in rce:
            nodei = int(i.split(':')[1])
            if nodei > nodemax:
                nodemax = nodei
        for i in rce:
            webnation = i.split(':')[0][2:-1]
            for j in range(len(self.nationlist)):
                if self.nationlist[j] == webnation:
                    graphicsceneCR.addEllipse(float(self.nationlist[j + 1]) / 4000 * 661 + 90,
                                              float(
                                                  self.nationlist[j + 2]) / 1991 * 241 + 20,
                                              3 + int(i.split(':')
                                                      [1]) / nodemax * 15,
                                              3 + int(i.split(':')[1]) / nodemax * 10, pen)

                    graphicsceneCR.addEllipse(float(self.nationlist[j + 1]) / 4000 * 661,
                                              float(self.nationlist[j + 2]) / 1991 * 241, 0.00001, 0.00001, pen)
        self.ui.graphicsView_7.setScene(graphicsceneCR)
        self.ui.graphicsView_7.show()

    def closeEvent(self, event):
        address = ' '
        if self.m_wallet.address != '':
            address = self.m_wallet.address
        mineAddress = ' '
        if len(self.ui.lineEdit_7.text().strip())== 42 and self.ui.lineEdit_7.text().strip()[0:2]=='0x':
            mineAddress = self.ui.lineEdit_7.text().strip()

        self.settingroot.getElementsByTagName('wallet')[0].firstChild.data = address
        self.settingroot.getElementsByTagName('minewallet')[0].firstChild.data = mineAddress

        f = open(pathConfig.lastSettingPath + 'setting.xml', 'w')
        self.settingdom.writexml(f, indent = '\n',addindent='    ', newl='',encoding='utf-8')

        f.close()

        self.kill_by_name('walton')
        #delete private.png
        if (os.path.exists(pathConfig.keystoresPath + "private.png")):
            os.remove(pathConfig.keystoresPath + "private.png")
        event.accept()

    def kill_by_name(self, name):

        cmd = 'killall walton'
        os.system(cmd)

    def refreshmininfo(self):
        try:
            if len(self.ui.lineEdit_7.text().strip()) == 42 and self.ui.lineEdit_7.text().strip()[0:2] == '0x':
                self.ui.lineEdit_10.setText(
                    str(Core_func.getDifficulty()[1][0][1]))
                r = Core_func.getTransactionRecord_day(self.ui.lineEdit_7.text(), '2')[
                    1][0]['history_balance']
                if (int(r)) / (10 ** 9) < 5000:
                    self.ui.lineEdit_12.setText('2')
                else:
                    self.ui.lineEdit_12.setText('3')
                if self.miningtatus == 0:
                    self.ui.lineEdit_11.setText('0')
                else:
                    self.ui.lineEdit_11.setText(str(self.w3.eth.hashrate))
                self.initMingres()
                self.initmining()


            # else:
            #     self.publishform.show_w2("invalid address", self)
                        # self.ui.lineEdit_10.setText(
                        #     str(Core_func.getDifficulty()[1][0][1]))
                        # r = Core_func.getTransactionRecord_day(self.ui.lineEdit_7.text(), '2')[
                        #     1][0]['history_balance']
                        # if (int(r)) / (10 ** 9) < 5000:
                        #     self.ui.lineEdit_12.setText('2')
                        # else:
                        #     self.ui.lineEdit_12.setText('3')
                        # if self.miningtatus == 0:
                        #     self.ui.lineEdit_11.setText('0')
                        # else:
                        #     self.ui.lineEdit_11.setText(str(self.w3.eth.hashrate))
                        # self.initMingres()
                        # self.initmining()

        except Exception as err:
            # self.publishform.show_w2('mining information refresh failed',self)
            #os.chdir('WTCWallet.app/')
            subprocess.Popen('walton.exe', shell=True)
            #os.chdir('..')
            print('j2 once walton')

    def startWalton(self):
        #先判断要打开的walton程序是否存在，存在则打开， 不存在则报错返回且程序退出
        if not os.path.isfile ('./walton.exe'):
            # 弹框报错返回False
            self.publishform.show_w2('Can not find walton ! please check your Installation package ', self)
            return False
        result1 = subprocess.Popen('walton.exe', shell=True)
        #如果当前walton程序下不存在Data文件夹，则需要再启动一次
        if not os.path.isdir('./Data'):
            time.sleep(3)
            result2 = subprocess.Popen('walton.exe', shell=True)
        return  True

    def btntraHisrefreshClick(self):
        #开启钱包页面刷新按钮的定时器
        self.traHisrefreshTimer.start(10000)  #
        # 将我的钱包页面刷新按钮设置为不可用
        self.ui.pushButton_46.setIcon(QIcon(":/pic/grayqukuai.png"))
        self.ui.pushButton_46.setEnabled(False)

        self.getMWHistoryBalance()
        self.getMWTransactionListData()

    def resetTraHisrefreshBtn(self):
        self.ui.pushButton_46.setEnabled(True)
        self.ui.pushButton_46.setIcon(QIcon(":/pic/puperqukuai.png"))

    def createMWConnection(self):
        # btntraHisrefresh 按钮按下如果长时间没请求到数据，隔一段时间自动恢复按钮可用，请求到数据则直接设置可用
        self.traHisrefreshTimer = QTimer(self)  #
        self.traHisrefreshTimer.timeout.connect(self.resetTraHisrefreshBtn)
        #这是一个一次性的定时器，每开启一次指挥执行一次
        self.traHisrefreshTimer.setSingleShot(True)
        # My Wallet 页面刷新的按钮
        btntraHisrefresh = self.ui.pushButton_46
        btntraHisrefresh.clicked.connect(self.btntraHisrefreshClick)

        self.TransactionTimer = QTimer(self)  #
        self.TransactionTimer.timeout.connect(self.getMWTransactionListData)  #
        self.TransactionTimer.start(60000)  #

        self.BalanceTimer = QTimer(self)  #
        self.BalanceTimer.timeout.connect(self.getMWHistoryBalance)  #
        self.BalanceTimer.start(60000)  #

    def createMessageConnection(self):
        self.ui.LogMessage.itemClicked.connect(self.showMessageDetails)


    
    
    def createConnection(self):

        self.LastBlockTimer = QTimer(self)  #
        self.LastBlockTimer.timeout.connect(self.getLastBlock)  #
        self.LastBlockTimer.start(30000)  #


        self.timertop = QTimer(self)  #
        self.timertop.timeout.connect(self.refreshTop)  #
        self.timertop.start(30000)  #

        '''
        self.timerchart = QTimer(self)  #
        self.timerchart.timeout.connect(self.initchart)  #
        self.timerchart.start(1000)  #

        self.timertran = QTimer(self)  #
        self.timertran.timeout.connect(self.refresh)  #
        self.timertran.start(153000)  #

        self.timertop = QTimer(self)  #
        self.timertop.timeout.connect(self.refreshTop)  #
        self.timertop.start(30000)  #



        self.timermining = QTimer(self)  #
        self.timermining.timeout.connect(self.initmining)  #
        self.timermining.start(267000)  #

        self.timermap = QTimer(self)  #
        self.timermap.timeout.connect(self.initmap)  #
        self.timermap.start(1730000)  #


        self.timermap = QTimer(self)  #
        self.timermap.timeout.connect(self.initMarket)  #
        self.timermap.start(3600000)  # 12h

        self.timermap = QTimer(self)  #
        self.timermap.timeout.connect(self.initMingres)  #
        self.timermap.start(900000)  # 15min
        '''
        btnminHisrefresh = self.ui.pushButton_45
        btnminHisrefresh.clicked.connect(self.initmining)

        # Page of Create Wallet
        btncnw = self.ui.creat_new_wallet
        btncnw.clicked.connect(self.pressCreatNewWallet)
        btnimportKeys = self.ui.import_Keystore
        btnimportKeys.clicked.connect(self.pressimportbykeystore)
        btnimportPri = self.ui.import_Pri
        btnimportPri.clicked.connect(self.presspressimportbyPri)
        btnimportMnem = self.ui.import_MP
        btnimportMnem.clicked.connect(self.presspressimportbyMnem)
        btnmywallet = self.ui.mw_2
        btnmywallet.clicked.connect(self.pressbtn6)
        btnback1 = self.ui.back_to_import
        btnback1.clicked.connect(self.pressback2import)
        btnback2 = self.ui.back_to_import_2
        btnback2.clicked.connect(self.pressback2import)
        btnback3 = self.ui.back_to_import_6
        btnback3.clicked.connect(self.pressback2import)
        btnback4 = self.ui.back_to_import_7
        btnback4.clicked.connect(self.pressback2import)
        btngenerate = self.ui.Gene_Key
        btngenerate.clicked.connect(lambda: self.generateKey())
        btnloginpri = self.ui.login_pri
        btnloginpri.clicked.connect(lambda: self.importsecret())
        btnloginmnem = self.ui.login_mnem
        btnloginmnem.clicked.connect(lambda: self.importmnemonic())
        btnimportfile = self.ui.import_Keystore_2
        btnimportfile.clicked.connect(self.importfile)
        # enter password
        btntosee1 = self.ui.turn2visible1
        btntosee1.clicked.connect(self.seepass1)

        btntosee2 = self.ui.turn2visible2
        btntosee2.clicked.connect(self.seepass2)

        # enter secret
        btntosee3 = self.ui.turn2visible1_9
        btntosee3.clicked.connect(self.seepri1)

        btntosee4 = self.ui.turn2visible1_8
        btntosee4.clicked.connect(self.seephrs1)

        btntosee5 = self.ui.turn2visible2_5
        btntosee5.clicked.connect(self.seephrs2)

        # enter mnem
        btntosee6 = self.ui.turn2visible1_7
        btntosee6.clicked.connect(self.seemnem1)

        btntosee7 = self.ui.turn2visible1_6
        btntosee7.clicked.connect(self.seephrm1)

        btntosee8 = self.ui.turn2visible2_4
        btntosee8.clicked.connect(self.seephrm2)

        # enter keystore
        btntosee9 = self.ui.turn2visible1_2
        btntosee9.clicked.connect(self.seepassK)

        btnloginkeys = self.ui.login_keys
        btnloginkeys.clicked.connect(lambda: self.importKetstore())

        # all pages shift
        btn1 = self.ui.mywallet
        btn1.clicked.connect(self.pressbtn1)
        btn2 = self.ui.statistic
        btn2.clicked.connect(self.pressbtn2)
        btn3 = self.ui.message
        btn3.clicked.connect(self.pressbtn3)
        btn4 = self.ui.contact
        btn4.clicked.connect(self.pressbtn4)
        btn5 = self.ui.mining
        btn5.clicked.connect(self.pressbtn5)
        btn6 = self.ui.mw
        btn6.clicked.connect(self.pressbtn6)
        btn0 = self.ui.cw
        btn0.clicked.connect(self.pressbtn0)

        # new wallet page
        btneye1 = self.ui.pushButton_41

        btneye1.clicked.connect(self.seepassword)
        btnsavekey = self.ui.SaveKey
        btnsavekey.clicked.connect(lambda: self.savekey(0, 1))
        btnsavename = self.ui.SaveName
        btnsavename.clicked.connect(self.savename)

        btneye2 = self.ui.pushButton_40

        btneye2.clicked.connect(self.seeprikey)

        btncopy1 = self.ui.pushButton_39
        btncopy1.clicked.connect(self.copyPublicKey)
        btncopy2 = self.ui.pushButton_42
        btncopy2.clicked.connect(self.copymnemword)
        # *4

        # my wallet page
        btneyepri = self.ui.pushButton_35

        btneyepri.clicked.connect(self.seeprivatekey)
        btneyepriqrcode = self.ui.pushButton_43
        btneyepriqrcode.clicked.connect(self.seeprivateqrcode)
        btncopypub = self.ui.pushButton_34
        btncopypub.clicked.connect(self.copyPublicKey)
        btnreb = self.ui.pushButton_6
        btnreb.clicked.connect(self.toreddit)
        btntwi = self.ui.pushButton_7
        btntwi.clicked.connect(self.totwitter)
        btntme = self.ui.pushButton_5
        btntme.clicked.connect(self.totme)
        btnsta = self.ui.pushButton_8
        btnsta.clicked.connect(self.tostack)
        self.ui.pushButton_9.clicked.connect(lambda: self.sendform.show_w2(self))
        self.ui.pushButton_21.clicked.connect(self.seeprikey)

        # Multiple Wallet page
        btn2create = self.ui.pushButton_32
        btn2create.clicked.connect(self.pressbtn0)
        btn2create1 = self.ui.pushButton_33
        btn2create1.clicked.connect(self.pressbtn0)
        btn2set1 = self.ui.pushButton_31
        btn2set1.clicked.connect(lambda: self.setpswform.show_w2(self))

        # Message page
        #btnMark = self.ui.pushButton_37
        #btnMark.clicked.connect(self.purple2black)

        # mining page
        self.mingwaform = mingwaform(self)
        btnrebm = self.ui.pushButton_12
        btnrebm.clicked.connect(self.toreddit)
        btntwim = self.ui.pushButton_13
        btntwim.clicked.connect(self.totwitter)
        btntmem = self.ui.pushButton_14
        btntmem.clicked.connect(self.totme)
        btnstam = self.ui.pushButton_11
        btnstam.clicked.connect(self.tostack)
        btnacc = self.ui.pushButton_29
        btnacc.clicked.connect(lambda: self.mingwaform.show_w2(self))
        self.ui.lineEdit_7.textChanged.connect(self.refreshmininfo)

        self.ui.radioButton_4.clicked.connect(self.changereg)
        self.ui.radioButton_4.setChecked(0)
        # self.ui.radioButton_3.toggle()
        self.ui.radioButton_3.clicked.connect(self.changefast)
        self.ui.radioButton_3.setChecked(True)
        # self.ui.radioButton_6.toggle()
        self.ui.radioButton_6.clicked.connect(self.changesfast)
        self.ui.radioButton_6.setChecked(0)
        # self.ui.radioButton_5.toggle()
        self.ui.radioButton_5.clicked.connect(self.changeefast)
        self.ui.radioButton_5.setChecked(0)
        self.ui.radioButton_2.setVisible(0)

        self.ui.horizontalSlider.setValue(2)
        self.ui.horizontalSlider.valueChanged.connect(self.changespeed)
        btnmining = self.ui.pushButton_30

        btnmining.clicked.connect(self.startmining)

        # statistics page
        btnrebs = self.ui.pushButton_17
        btnrebs.clicked.connect(self.toreddit)
        btntwis = self.ui.pushButton_16
        btntwis.clicked.connect(self.totwitter)
        btntmes = self.ui.pushButton_18
        btntmes.clicked.connect(self.totme)
        btnstas = self.ui.pushButton_15
        btnstas.clicked.connect(self.tostack)

    def setToolBoxVisible(self,bVisible):
        self.ui.mywallet.setVisible(bVisible)
        self.ui.statistic.setVisible(bVisible)
        self.ui.message.setVisible(bVisible)
        self.ui.contact.setVisible(bVisible)

    #初始化的时候全部设置成灰色的，触发选中某个按钮的时候先全部恢复成灰色的
    def setToolBoxNoHeighlight(self):
        self.ui.mywallet.setIcon(QIcon(":/pic/mywallet0.png"))
        self.ui.statistic.setIcon(QIcon(":/pic/statistics0.png"))
        self.ui.message.setIcon(QIcon(':/pic/message0.png'))
        self.ui.contact.setIcon(QIcon(":/pic/contact0.png"))
        self.ui.mining.setIcon(QIcon(":/pic/mining0.png"))
        self.ui.mw.setIcon(QIcon(":/pic/mw0.png"))
        self.ui.cw.setIcon(QIcon(":/pic/cw0.png"))

    def initUI(self):
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setFixedSize(1030, 548)

        # 主界面的tablewidget的，第一次打开默认设置在登录的界面，后面打开默认在上一次打开的钱包的界面
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.importstack.setCurrentIndex(0)
        self.ui.cw.setIcon(QIcon(":/pic/cw1.png"))
        self.setToolBoxVisible(False)

        self.ui.LogMessage.setStyleSheet("color:#8700ff;border:0px;background-color: rgb(255, 255, 255);")
        self.ui.LogMessage.setSelectionBehavior(Core_func.QTableWidget.SelectRows)
        self.ui.LogMessage.horizontalHeader().setVisible(0)
        self.ui.LogMessage.verticalHeader().setVisible(0)
        self.ui.LogMessage.setShowGrid(0)
        self.ui.LogMessage.horizontalHeader().setStretchLastSection(1)
        self.ui.LogMessage.verticalHeader().setDefaultSectionSize(57)
        self.ui.LogMessage.setColumnWidth(0, 130)  #
        self.ui.LogMessage.setColumnWidth(1, 160)  #
        self.ui.LogMessage.setColumnWidth(2, 300)  #
        self.ui.LogMessage.setColumnWidth(3, 10)  #
        self.ui.LogMessage.setFrameShape(QFrame.NoFrame)  #
        self.ui.LogMessage.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.LogMessage.setSelectionMode(
            QAbstractItemView.NoSelection)
        self.ui.LogMessage.setFocusPolicy(Qt.NoFocus)  #
        self.ui.LogMessage.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        self.ui.ContactsT.horizontalHeader().setVisible(0)
        self.ui.ContactsT.verticalHeader().setVisible(0)
        self.ui.ContactsT.setShowGrid(0)
        self.ui.ContactsT.horizontalHeader().setStretchLastSection(1)
        self.ui.ContactsT.verticalHeader().setDefaultSectionSize(45)
        self.ui.ContactsT.setColumnWidth(0, 140)  #
        self.ui.ContactsT.setColumnWidth(1, 370)  #
        self.ui.ContactsT.setColumnWidth(2, 100)  #
        self.ui.ContactsT.setColumnWidth(3, 100)  #
        self.ui.ContactsT.setColumnWidth(4, 100)
        self.ui.ContactsT.setFrameShape(QFrame.NoFrame)  #
        self.ui.ContactsT.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.ContactsT.setSelectionBehavior(Core_func.QTableWidget.SelectItems)
        self.ui.ContactsT.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.ContactsT.setFocusPolicy(Qt.NoFocus)
        self.ui.ContactsT.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        self.ui.TransactionHistory.horizontalHeader().setVisible(0)
        self.ui.TransactionHistory.verticalHeader().setVisible(0)
        self.ui.TransactionHistory.setShowGrid(0)
        self.ui.TransactionHistory.horizontalHeader().setStretchLastSection(1)
        self.ui.TransactionHistory.verticalHeader().setDefaultSectionSize(40)
        self.ui.TransactionHistory.setColumnWidth(0, 15)
        self.ui.TransactionHistory.setColumnWidth(1, 130)  #
        self.ui.TransactionHistory.setColumnWidth(2, 280)  #
        self.ui.TransactionHistory.setColumnWidth(3, 71)  #
        self.ui.TransactionHistory.setColumnWidth(4, 90)  #
        self.ui.TransactionHistory.setFrameShape(QFrame.NoFrame)  #
        self.ui.TransactionHistory.setEditTriggers(
            QAbstractItemView.NoEditTriggers)
        self.ui.TransactionHistory.setSelectionMode(
            QAbstractItemView.NoSelection)
        self.ui.TransactionHistory.setFocusPolicy(Qt.NoFocus)
        self.ui.TransactionHistory.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")

        self.ui.miningHistory.horizontalHeader().setVisible(0)
        self.ui.miningHistory.verticalHeader().setVisible(0)
        self.ui.miningHistory.setShowGrid(0)
        self.ui.miningHistory.horizontalHeader().setStretchLastSection(1)
        self.ui.miningHistory.horizontalHeader().setDefaultSectionSize(200)
        self.ui.miningHistory.verticalHeader().setDefaultSectionSize(40)
        self.ui.miningHistory.setFrameShape(QFrame.NoFrame)
        self.ui.miningHistory.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.miningHistory.setSelectionMode(QAbstractItemView.NoSelection)
        self.ui.miningHistory.setFocusPolicy(Qt.NoFocus)
        self.ui.miningHistory.setSelectionMode(
            QAbstractItemView.NoSelection)
        self.ui.miningHistory.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")



        self.ui.multWallet.horizontalHeader().setVisible(0)
        self.ui.multWallet.verticalHeader().setVisible(0)
        self.ui.multWallet.setShowGrid(0)
        self.ui.multWallet.horizontalHeader().setStretchLastSection(1)

        # self.ui.multWallet.horizontalHeader().setDefaultSectionSize(0,180)
        self.ui.multWallet.setColumnWidth(0, 110)  #
        self.ui.multWallet.setColumnWidth(1, 355)  #
        self.ui.multWallet.setColumnWidth(2, 78)  #
        self.ui.multWallet.setColumnWidth(3, 77)  #
        self.ui.multWallet.setColumnWidth(4, 80)  #
        self.ui.multWallet.setColumnWidth(5, 80)  #

        self.ui.multWallet.verticalHeader().setDefaultSectionSize(45)
        self.ui.multWallet.setFrameShape(QFrame.Box)  #
        self.ui.multWallet.setEditTriggers(QAbstractItemView.NoEditTriggers)  #
        self.ui.multWallet.setSelectionMode(QAbstractItemView.NoSelection)  #
        self.ui.multWallet.setFocusPolicy(Qt.NoFocus)
        self.ui.multWallet.setSelectionMode(
            QAbstractItemView.NoSelection)
        self.ui.multWallet.verticalScrollBar().setStyleSheet(
            "QScrollBar{background:transparent; width: 10px;}"
            "QScrollBar::handle{background:lightgray; border:2px solid transparent; border-radius:5px; }"
            "QScrollBar::handle:hover{background:#9e9e9e; }"
            "QScrollBar::handle:pressed{background:#9e9e9e;}"
            "QScrollBar::sub-line{background:transparent;}"
            "QScrollBar::add-line{background:transparent;}")




    def init(self):
        # 由主窗口弹出的对话框先new一个实体
        self.setpswform = setpswform(self)
        self.publishform = publishform(self)
        self.changepswform = changepswform(self)
        self.sendform = sendform(self)
        self.pswform = pswform(self)

        # 主程序对象初始化
        self.m_wallet = Wallet
        self.Trans = Transaction
        # 标志刷新balance的线程是否开启了
        self.IsnitchartThreadstarted = False
        self.transactionListGetting  = False
        self.historyBalanceGetting = False
        self.lastBlockGetting = False
        self.waite_miningtatus = 0
        self.lastblacknum = 0
        self.cpures = 2
        self.miningtatus = 0
        self.syncstatus = 0
        self.peers = 0
        self.pass1eye = 1
        self.pass2eye = 1
        self.pri1eye = 1
        self.phrs1eye = 1
        self.phrs2eye = 1
        self.mnemeye = 1
        self.phrm1eye = 1
        self.phrm2eye = 1
        self.passKeye = 1
        self.passwordeye = 1
        self.prieye = 1
        self.privatekeyeye = 1
        self.startstop = 1
        self.cpumode = 1

        self.getLastBlock()

        # 开启walton服务器
        if self.startWalton() == False:
            return
        # 连接walton服务器的端口
        self.w3 = Web3(HTTPProvider('http://127.0.0.1:8545', request_kwargs={'timeout': 3}))

        # 加载上一次的配置信息，还需要整合以及添加一些配置文件（待做）
        self.loadConfigFile();

        # 将本地记录的钱包账户加载到multiple wallet
        self.initwallets()
        #默认打开第一个钱包，我认为不对，先注销掉，应该打开上一次打开的钱包
        #if self.m_wallet.address != '':
         #   self.openwallet(0, 1)

        #初始化联系人，这个不需要联网，初始化一次就可以了
        self.initcontact()
        #初始化挖矿结果，应该显示上一次挖矿账号30天内的挖矿结果
        self.initMingres()
        #显示当前挖矿账户的挖矿记录
        self.initmining()
        #显示30天内的市场信息
        self.initMarket()
        #初始化世界地图那张
        self.initmap()


        self.show()
        self.createConnection()
        self.createMWConnection()
        self.createMessageConnection()



    def loadConfigFile(self):
        #
        if not os.path.isfile(pathConfig.lastSettingPath + 'test.xml'):
            ret = Core_func.generateaddressXml()
        self.praseTestFile()
        if not os.path.isfile(pathConfig.lastSettingPath + 'Wallets.xml'):
            ret = Core_func.generatewalletXml()
        self.praseWalletsFile()

        if os.path.isfile(pathConfig.lastSettingPath +'test.xml'):
            self.transdom = xml.dom.minidom.parse(pathConfig.lastSettingPath +"test.xml")
            xmlStr = self.transdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.transdom = xml.dom.minidom.parseString(xmlStr)
            xmlStr = self.transdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.transdom = xml.dom.minidom.parseString(xmlStr)
            self.transroot = self.transdom.documentElement
        else:
            ret = Core_func.generatetransXml()
            self.transdom = xml.dom.minidom.parse(pathConfig.lastSettingPath +"test.xml")  #
            self.transroot = self.transdom.documentElement  #
            for i in range(self.ui.multWallet.rowCount()):
                ind = Core_func.QTableWidget.indexFromItem(self.ui.multWallet, self.ui.multWallet.item(i, 1))
                print(i, self.ui.multWallet.rowCount())
                Core_func.addtransaddrxml(self.transdom, self.transroot, ind.data(), time.strftime('%Y-%m-%d', time.localtime(time.time())))
            xmlStr = self.transdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.transdom = xml.dom.minidom.parseString(xmlStr)
            xmlStr = self.transdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.transdom = xml.dom.minidom.parseString(xmlStr)

        if not os.path.isfile(pathConfig.lastSettingPath + 'setting.xml'):
            Core_func.generateSettingXml()
        self.praseSettingFile()

        '''
            self.settingdom = xml.dom.minidom.parse(pathConfig.lastSettingPath +  "setting.xml")  #
            xmlStr = self.settingdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.settingdom = xml.dom.minidom.parseString(xmlStr)
            xmlStr = self.settingdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.settingdom = xml.dom.minidom.parseString(xmlStr)
            self.settingroot = self.settingdom.documentElement  #
            if len(self.settingroot.getElementsByTagName('minewallet')[0].firstChild.data) == 42:
                self.ui.lineEdit_7.setText(self.settingroot.getElementsByTagName('minewallet')[0].firstChild.data)
                self.refreshmininfo()
            if len(self.settingroot.getElementsByTagName('wallet')[0].firstChild.data) == 42:
                self.m_wallet.address = self.settingroot.getElementsByTagName('wallet')[0].firstChild.data

            if self.settingroot.getElementsByTagName('MinerP')[0].firstChild.data == ' ':
                stackedW.setCurrentIndex(1)
                self.setpswform.ui.pushButton_35.setIcon(QIcon(":/pic/close2.png"))
                self.setpswform.setable = 0
                self.pswform = pswform(self)
                #self.show()
            else:
                stackedW.setCurrentIndex(0)
                self.setpswform.ui.pushButton_35.setIcon(QIcon(":/pic/open2.png"))
                self.setpswform.setable = 1
                self.pswform = pswform(self)
                #self.show()
                self.pswform.show_w2(self)
            if len(self.settingroot.getElementsByTagName('wallet')[0].firstChild.data) < 40:
                stackedW.setCurrentIndex(0)
                self.ui.mywallet.setVisible(0)
                self.ui.statistic.setVisible(0)
                self.ui.message.setVisible(0)
                self.ui.contact.setVisible(0)
            else:
                stackedW.setCurrentIndex(1)
                self.m_wallet.address = self.settingroot.getElementsByTagName('wallet')[0].firstChild.data
                self.ui.mywallet.setVisible(1)
                self.ui.statistic.setVisible(1)
                self.ui.message.setVisible(1)
                self.ui.contact.setVisible(1)
        else:
        '''

            #self.show()

    def praseTestFile(self):
        # 打开文档 将xml文件数据转化成一个树储存
        self.addrdom = xml.dom.minidom.parse(pathConfig.lastSettingPath + "test.xml")
        xmlStr = self.addrdom.toprettyxml(indent='', newl='', encoding='utf-8')
        xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')

        self.addrdom = xml.dom.minidom.parseString(xmlStr)
        xmlStr = self.addrdom.toprettyxml(indent='', newl='', encoding='utf-8')
        xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
        self.addrdom = xml.dom.minidom.parseString(xmlStr)
        # 根节点
        self.addrroot = self.addrdom.documentElement

    def praseWalletsFile(self):
        self.walletdom = xml.dom.minidom.parse(pathConfig.lastSettingPath + 'Wallets.xml')
        xmlStr = self.walletdom.toprettyxml(indent='', newl='', encoding='utf-8')
        xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
        self.walletdom = xml.dom.minidom.parseString(xmlStr)
        xmlStr = self.walletdom.toprettyxml(indent='', newl='', encoding='utf-8')
        xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
        self.walletdom = xml.dom.minidom.parseString(xmlStr)
        self.walletroot = self.walletdom.documentElement

    def praseSettingFile(self):
        self.settingdom = xml.dom.minidom.parse(pathConfig.lastSettingPath + "setting.xml")  #
        xmlStr = self.settingdom.toprettyxml(indent='', newl='', encoding='utf-8')
        xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
        self.settingdom = xml.dom.minidom.parseString(xmlStr)
        xmlStr = self.settingdom.toprettyxml(indent='', newl='', encoding='utf-8')
        xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
        self.settingdom = xml.dom.minidom.parseString(xmlStr)
        self.settingroot = self.settingdom.documentElement  #
        if len(self.settingroot.getElementsByTagName('minewallet')[0].firstChild.data) == 42:
            self.ui.lineEdit_7.setText(self.settingroot.getElementsByTagName('minewallet')[0].firstChild.data)
            #self.refreshmininfo()
        if len(self.settingroot.getElementsByTagName('wallet')[0].firstChild.data) == 42:
            self.m_wallet.address = self.settingroot.getElementsByTagName('wallet')[0].firstChild.data
        #判断MinerP这个标签是否有值，如果没有值的话则正常打开程序，有账户则跳转到上一次打开的账户
        if self.settingroot.getElementsByTagName('MinerP')[0].firstChild.data == ' ':
            #self.ui.stackedWidget.setCurrentIndex(1)
            self.pressbtn0()
            self.setpswform.ui.pushButton_35.setIcon(QIcon(":/pic/close2.png"))
            self.setpswform.setable = 0
            self.pswform = pswform(self)
            self.show()
        #有值的话则打开，则先打开输入密码的创窗口，输入密码之后才可以可以使用钱包，如果上次有打开的钱包则打开那个钱包
        else:
            self.ui.stackedWidget.setCurrentIndex(0)
            self.setpswform.ui.pushButton_35.setIcon(QIcon(":/pic/open2.png"))
            self.setpswform.setable = 1
            self.pswform = pswform(self)
            self.show()
            self.pswform.show_w2(self)

        #不管需不需要输入密码，这个过程过了之后就打开之前记录地址的钱包，并且定位到mywallet页面，如果没有钱包则还在创建钱包的页面
        if self.m_wallet.address != '':
            self.openWalletByAddress(self.m_wallet.address)











class Wallet:
    password = ''
    privateKey = ''
    mnem = ''
    address = ''
    accountname = ''
    filename = ''
    nonce = 0


class Transaction:
    txhash = ''
    status = 'Submitted'
    value = ''
    fromaddr = ''
    toaddr = ''
    Type = ''
    Gas = ''
    Gasprice = ''
    Blocknumber = ''
    timestamp = ''


class nationpos:
    nationlist = ('AU', 3330, 1505,
                  'BR', 1370, 1365,
                  'CN', 3030, 865,
                  'CA', 690, 520,
                  'DE', 2005, 640,
                  'FR', 1920, 705,
                  'GB', 1880, 620,
                  'HK', 3115, 1000,
                  'IN', 2730, 1000,
                  'JP', 3375, 830,
                  'KR', 3255, 835,
                  'MY', 2985, 1195,
                  'RU', 2980, 480,
                  'SG', 3000, 1220,
                  'TH', 2275, 1070,
                  'US', 820, 795,

                  'AE', 2485, 1000,
                  'AR', 1225, 1635,
                  'BE', 1960, 667,
                  'BG', 2180, 778,
                  'GR', 2150, 820,
                  'RO', 2175, 730,
                  'TR', 2260, 820,
                  'BY', 2200, 625,
                  'PL', 2125, 645,
                  'DK', 2025, 590,
                  'EE', 2185, 550,
                  'CZ', 2070, 680,
                  'FI', 2200, 465,
                  'SE', 2080, 485,
                  'NO', 1995, 515,
                  'CH', 1998, 720,
                  'IT', 2045, 760,
                  'NL', 1970, 645,
                  'IE', 1830, 630,
                  'AT', 2065, 710,
                  'SI', 2080, 733,
                  'YU', 2135, 760,
                  'ES', 1870, 805,
                  'PT', 1825, 815,
                  'CY ', 2265, 868,
                  'MD', 2215, 715,
                  'CL', 1140, 1670,
                  'CO', 1120, 1215,
                  'NZ', 3785, 1695,
                  'TW', 3190, 990,
                  'IL', 2310, 915,
                  'DO', 1175, 1050,
                  'LU', 1990, 680,
                  'GE', 2375, 780,
                  'CR', 1020, 1152,
                  'HU', 2110, 720,
                  'CU', 1080, 1025,
                  'LV', 2180, 575,
                  'LT', 2165, 602,
                  'MA', 1830, 915,
                  'PE', 1095, 1350,
                  'PR', 1205, 1060,
                  'SK', 2120, 695,
                  'AM', 2390, 805,
                  'TJ', 2655, 825,
                  'TM', 2520, 815,
                  'ZA', 2165, 1595,

                  'LY', 2090, 960,
                  'NG', 1990, 1160,
                  'ID', 3120, 1270,
                  'MX', 815, 1000,
                  'PK', 2650, 930,
                  'VN', 3065, 1125,
                  'VE', 1210, 1180,
                  'SA', 2380, 1000,
                  'KH', 3025, 1125,
                  'AZ', 2420, 803,
                  'MM', 2930, 1025,
                  'EC', 1075, 1270,
                  'HN', 990, 1095,
                  'IS', 1710, 450,
                  'JM', 1088, 1061,
                  'JO', 2300, 920,
                  'SN', 1755, 1105,
                  'SC', 2505, 1304,
                  'UA', 2245, 690,
                  'UY', 1315, 1615)

    AU = [3330, 1505]
    BR = [1370, 1365]
    CN = [3030, 865]
    CA = [690, 520]
    DE = [2005, 640]
    FR = [1920, 705]
    GB = [1880, 620]
    HK = [3115, 1000]
    IN = [2730, 1000]
    JP = [3375, 830]
    KR = [3255, 835]
    MY = [2985, 1195]
    RU = [2980, 480]
    SG = [3000, 1220]
    TH = [2275, 1070]
    US = [820, 795]

    AE = [2485, 1000]
    AR = [1225, 1635]
    BE = [1960, 667]
    BG = [2180, 778]
    GR = [2150, 820]
    RO = [2175, 730]
    TR = [2260, 820]
    BY = [2200, 625]
    PL = [2125, 645]
    DK = [2025, 590]
    EE = [2185, 550]
    CZ = [2070, 680]
    FI = [2200, 465]
    SE = [2080, 485]
    NO = [1995, 515]
    CH = [1998, 720]
    IT = [2045, 760]
    NL = [1970, 645]
    IE = [1830, 630]
    AT = [2065, 710]
    SI = [2080, 733]
    YU = [2135, 760]
    ES = [1870, 805]
    PT = [1825, 815]
    CY = [2265, 868]
    MD = [2215, 715]
    CL = [1140, 1670]
    CO = [1120, 1215]
    NZ = [3785, 1695]
    TW = [3190, 990]
    IL = [2310, 915]
    DO = [1175, 1050]
    LU = [1990, 680]
    GE = [2375, 780]
    CR = [1020, 1152]
    HU = [2110, 720]
    CU = [1080, 1025]
    LV = [2180, 575]
    LT = [2165, 602]
    MA = [1830, 915]
    PE = [1095, 1350]
    PR = [1205, 1060]
    SK = [2120, 695]
    AM = [2390, 805]
    TJ = [2655, 825]
    TM = [2520, 815]
    ZA = [2165, 1595]

    LY = [2090, 960]
    NG = [1990, 1160]
    ID = [3120, 1270]
    MX = [815, 1000]
    PK = [2650, 930]
    VN = [3065, 1125]
    VE = [1210, 1180]
    SA = [2380, 1000]
    KH = [3025, 1125]
    AZ = [2420, 803]
    MM = [2930, 1025]
    EC = [1075, 1270]
    HN = [990, 1095]
    IS = [1710, 450]
    JM = [1088, 1061]
    JO = [2300, 920]
    SN = [1755, 1105]
    SC = [2505, 1304]
    UA = [2245, 690]
    UY = [1315, 1615]












if __name__ == '__main__':
    app = QApplication(sys.argv)
    if not (os.path.exists(pathConfig.keystoresPath)):
        os.makedirs(pathConfig.keystoresPath)
    if not (os.path.exists(pathConfig.lastSettingPath)):
        os.makedirs(pathConfig.lastSettingPath)
    #windows下底部工具栏不显示图标的问题
    print("system : " + platform.system())
    if platform.system() == 'Windows':
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
    ex = Example()
    recieveform = recieveform(ex)
    mulwalform = mulwalform(ex)
    pubaddrForm = pubaddrForm(ex)
    newcontactform = newcontactform(ex)

    ex.ui.pushButton_10.clicked.connect(lambda: recieveform.show_w2(ex))
    ex.ui.pushButton_36.clicked.connect(lambda: pubaddrForm.show_w2(ex))
    ex.ui.pushButton_38.clicked.connect(lambda: newcontactform.show_w2(ex))
    #messform = messform(ex)
    #ex.ui.LogMessage.itemClicked.connect(messform.show_w2)
    ex.ui.ContactsT.itemClicked.connect(ex.choosebtn)
    ex.ui.multWallet.itemClicked.connect(ex.walletbtn)
    sys.exit(app.exec_())
