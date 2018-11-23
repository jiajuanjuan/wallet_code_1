from PyQt5 import QtCore
import requests
import json
from Mainform import Figure_Canvas

from  ApplicationHelper import  ApplicationHelper
import Core_func
from TransactionListHelper import  TransactionList, AccountTransactionsListEntity,AccountTransactionsEntity,AddressTransactionsEntity
from AddressLastBalanceEntity import HistoryBalanceHelper ,AddressBalanceEntity,BalanceEntity,BalanceEntityList
from datetime import datetime, timedelta
import time

class initchartThread(QtCore.QThread):
    finishSignal = QtCore.pyqtSignal(tuple,Figure_Canvas)
    def __init__(self,dr,addr,parent=None):
        super(initchartThread, self).__init__(parent)
        self.dr=dr
        self.addr = addr
        self.interval = "20"

    def run(self):
        print("start Thread")
        self.ret = self.test()
        try:
            self.finishSignal.emit(self.ret,self.dr)
        except Exception as err:
            print("Error : " + str(err))

    def test(self):
        if self.addr != '':
            ret3 = self.getTransactionRecord_day()
            if ret3[0] == 0:
                return ('0','0')
            self.dr.y = []
            self.dr.x = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2,1]
            try:
                for i in range(len(ret3[1])):
                    self.dr.y.append(float(ret3[1][i]['history_balance']))
                self.dr.axes.plot(self.dr.x, self.dr.y, 'r-', 1)
                self.dr.axes.set_axis_off()
                print('jjbalance=' + str(ret3[1][0]['history_balance']))
                self.dr.balance = ret3[1][0]['history_balance']
                return ('1',ret3[1][0]['history_balance'])
            except Exception as err:
                print("Error : " + str(err))
                return ('0', '0')
        else:
            self.dr.y = [0]
            self.dr.x = [0]
            self.dr.axes.plot(self.dr.x, self.dr.y, 'r-', 1)
            self.dr.axes.set_axis_off()
            return ('1','0')

    def getTransactionRecord_day(self):
        try:
            response = requests.get("https://waltonchain.net:18950/api/getHistoryBalance/" + self.addr + '/' + self.interval ,timeout=(5,10))
            if response.status_code == 200:
                return (1, response.json()['HistoryBalance'])
        except Exception:
            return (0,0)



class getHistoryBalanceThread(QtCore.QThread):
    getBalancefinishSignal = QtCore.pyqtSignal(bool)
    def __init__(self,addr, parent=None):
        super(getHistoryBalanceThread, self).__init__(parent)
        self.address = addr

    def run(self):
        print("getHistoryBalanceThread run")
        try:
            retBalance = Core_func.getHistoryBalance(self.address)
            if retBalance[0] == False:
                self.getBalancefinishSignal.emit(False)
                return
        except Exception as err:
            print("getHistoryBalanceThread Run Error :" + str(err))
            self.getBalancefinishSignal.emit(False)
            return

        self.refreshLocalFileData(retBalance[1])
        self.getBalancefinishSignal.emit(True)

    def refreshLocalFileData(self, strBalance):
        try:
            # 将字典转成对象
            balist =  BalanceEntityList()
            # 将请求到的数据转成字典
            print("$$"+strBalance + "$$")
            balanceDict = json.loads(s=strBalance)
            balist.__dict__ = balanceDict

            addressBaEntity = AddressBalanceEntity()

            # 记录当前对象的地址，再add的时候防止重复
            addressBaEntity.address = self.address
            # 变量列表的字典一个个转成对象
            for i in range(len(balist.HistoryBalance)):
                bEntity = BalanceEntity()
                bEntity.__dict__ = balist.HistoryBalance[i]
                # 时间进行转换
                time_s = datetime.strptime(bEntity.utc_timestamp, "%Y-%m-%d %H:%M:%S")
                bEntity.utc_timestamp = Core_func.utc2local(time_s).strftime('%Y-%m-%d %H:%M:%S')
                addressBaEntity.HistoryBalanceList.append(bEntity)
            hbHelper = HistoryBalanceHelper()
            hbHelper.add(addressBaEntity)
            hbHelper.save()
        except Exception as err:
            print("getHistoryBalanceThread refreshLocalFileData Run Error :" + str(err))
            self.getBalancefinishSignal.emit(False)
            return







class getTransactionDataThread(QtCore.QThread):
    getTransfinishSignal = QtCore.pyqtSignal(bool,int)
    def __init__(self,addr, parent=None):
        super(getTransactionDataThread, self).__init__(parent)
        self.address = addr
    def run(self):
        #获取余额
        balance = 0
        nonce = 0
        try:
            retBalance =Core_func.getAccountBalance(self.address)
            if retBalance[0] == False:
                self.getTransfinishSignal.emit(False,nonce)
                return
            balance = retBalance[1]

            # 获取Nonce
            retNonce = Core_func.getAccountNonce(self.address)
            if retNonce[0] == False:
                self.getTransfinishSignal.emit(False,nonce)
                return
            nonce = retNonce[1]
            print("getTransactionDataThread nonce : " + str(nonce))

            # 获取交易记录
            retTrans = Core_func.getTransactionRecord(self.address)
            if retTrans[0] == False:
                self.getTransfinishSignal.emit(False,nonce)
                return
            self.time =time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
            self.refreshLocalFileData(retTrans[1]);
            self.getTransfinishSignal.emit(True,nonce)
            return
        except Exception as err:
            print("1Error : " +  str(err))
            self.getTransfinishSignal.emit(False,nonce)
            return
    def refreshLocalFileData(self,strTrans):
        #先用变量记录下来，保证一次交易记录获取的过程中lastBlock的值是一样的
        lastBlock = ApplicationHelper.lastBlock
        try:
            lstEntity = AccountTransactionsListEntity()
            AccountTransListDict = json.loads(s=strTrans)
            lstEntity.__dict__ = AccountTransListDict
            # 初始化一个钱包
            addressEntity = AddressTransactionsEntity()
            addressEntity.Address = self.address
            addressEntity.UpdateTime = self.time
            currentAddress = self.address.lower()
            for i in range(len(lstEntity.tx_pagination_details)):
                # 创建一个账户交易
                accountEntity = AccountTransactionsEntity()
                # 将网络请求的交易数据额dict赋值给账户交易对象的dict（用dict初始化对象）
                accountEntity.__dict__ = lstEntity.tx_pagination_details[i]
                # 跟新blockType的属性
                if  lastBlock - accountEntity.blockNumber >= 11:
                    accountEntity.blockType = ApplicationHelper.transSuccess
                else:
                    accountEntity.blockType = str(lastBlock - accountEntity.blockNumber + 1) + '/12'
                # 跟新每笔交易的类型是send 还是receive
                if accountEntity.addressFrom == currentAddress:
                    accountEntity.transType = ApplicationHelper.transSend
                else:
                    accountEntity.transType = ApplicationHelper.transReceive
                #时间进行转换
                time_s = datetime.strptime(accountEntity.utc_timestamp, "%Y-%m-%d %H:%M:%S")
                accountEntity.utc_timestamp = Core_func.utc2local(time_s).strftime('%Y-%m-%d %H:%M:%S')
                # 将账户交易的对象添加到钱包的账户交易列表中
                addressEntity.AccountTransactionsEntityList.append(accountEntity)
            tHelper = TransactionList()
            tHelper.add(addressEntity)
            return
        except Exception as err:
            print("2Error : " + str(err))
            #self.getTransfinishSignal.emit(False)
            return




class getLastBlockThread(QtCore.QThread):
    getLastBlockfinishSignal = QtCore.pyqtSignal(tuple)
    def __init__(self, parent=None):
        super(getLastBlockThread, self).__init__(parent)

    def run(self):
        lastBlockRet = Core_func.getLatestBlock()
        self.getLastBlockfinishSignal.emit(lastBlockRet)


























