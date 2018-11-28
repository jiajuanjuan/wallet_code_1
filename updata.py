from PyQt5 import QtCore
import requests
import json
from Mainform import Figure_Canvas

from  ApplicationHelper import  ApplicationHelper
import Core_func
from TransactionListHelper import  TransactionList, AccountTransactionsListEntity,AccountTransactionsEntity,AddressTransactionsEntity
from AddressLastBalanceEntity import HistoryBalanceHelper ,AddressBalanceEntity,BalanceEntity,BalanceEntityList
from TransactionSendListHelper import  TransactionSendListHelper,AddressTransactionSendEntity,TransactionSendEntity
from datetime import datetime, timedelta
import time

#更新20天余额的线程
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

#更新交易记录的线程
class getTransactionDataThread(QtCore.QThread):
    getTransfinishSignal = QtCore.pyqtSignal(bool)
    def __init__(self,addr, parent=None):
        super(getTransactionDataThread, self).__init__(parent)
        self.address = addr
    def run(self):
        #获取余额
        #balance = 0
        #nonce = 0
        try:
            #发现请求的balance 和nonce没有什么作用，先不请求
            """
            retBalance =Core_func.getAccountBalance(self.address)
            if retBalance[0] == False:
                self.getTransfinishSignal.emit(False,nonce)
                return
            balance = retBalance[1]

            retNonce = Core_func.getAccountNonce(self.address)
            if retNonce[0] == False:
                self.getTransfinishSignal.emit(False,nonce)
                return
            nonce = retNonce[1]
            print("getTransactionDataThread nonce : " + str(nonce))
            """
            # 获取交易记录
            retTrans = Core_func.getTransactionRecord(self.address)
            if retTrans[0] == False:
                self.getTransfinishSignal.emit(False)
                return
            self.time =time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
            self.refreshLocalFileData(retTrans[1]);
            self.getTransfinishSignal.emit(True)
            return
        except Exception as err:
            print("1Error : " +  str(err))
            self.getTransfinishSignal.emit(False)
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
            # --------------------------------------------------------------------------------------
            #用请求到的数据刷新TransactionList.xml的信息
            for i in range(len(lstEntity.tx_pagination_details)):
                # 创建一个账户交易
                accountEntity = AccountTransactionsEntity()
                # 将网络请求的交易数据额dict赋值给账户交易对象的dict（用dict初始化对象）
                accountEntity.__dict__ = lstEntity.tx_pagination_details[i]
                print("---------------accountEntity value : " + str(accountEntity.value))
                # 跟新blockType的属性
                if lastBlock - accountEntity.blockNumber >= 11:
                    accountEntity.blockType = ApplicationHelper.transSuccess
                else:
                    accountEntity.blockType = str(lastBlock - accountEntity.blockNumber + 1) + '/12'
                # 跟新每笔交易的类型是send 还是receive
                if accountEntity.addressFrom.lower() == self.address.lower():
                    accountEntity.transType = ApplicationHelper.transSend
                else:
                    accountEntity.transType = ApplicationHelper.transReceive
                # 时间进行转换
                time_s = datetime.strptime(accountEntity.utc_timestamp, "%Y-%m-%d %H:%M:%S")
                accountEntity.utc_timestamp = Core_func.utc2local(time_s).strftime('%Y-%m-%d %H:%M:%S')
                # 将账户交易的对象添加到钱包的账户交易列表中
                addressEntity.AccountTransactionsEntityList.append(accountEntity)
            tHelper = TransactionList()
            tHelper.add(addressEntity)
            # --------------------------------------------------------------------------------------
            # 更新transSendlist里面的信息
            tsHelper = TransactionSendListHelper()
            addressTransSendList = tsHelper.find(self.address)
            for i in range(len(addressTransSendList.TransactionSendList)):
                accountSendEntity = addressTransSendList.TransactionSendList[i]
                bhas = False
                if accountSendEntity.blockType != ApplicationHelper.transSuccess:
                    for i in range(len(addressEntity.AccountTransactionsEntityList)):
                        accountEntity = addressEntity.AccountTransactionsEntityList[i]
                        # 判断send的交易信息是否已经在请求到的list中存在(用hash值判断)，如果已经存在则transSend里面的交易类型就改为Success，否则暂不处理
                        if accountSendEntity.tx_hash.lower() == accountEntity.tx_hash.lower():
                            bhas = True
                            break
                    if bhas == True:
                        accountSendEntity.blockType = ApplicationHelper.transSuccess
                    else:
                        # C#是会根据lastnonce判断是否失败的，这边暂时没有判断
                        pass
                    tsHelper.save()
            # --------------------------------------------------------------------------------------
            return
        except Exception as err:
            print("2Error : " + str(err))
            #self.getTransfinishSignal.emit(False)
            return

#更新市场信息的线程
class getMarketDataThread(QtCore.QThread):
    #返回4个信息 ：x轴的信息，y轴的信息，起止日期，usd的值，通过信号传递给界面，界面绘制出来
    getMarketSignalShowChart = QtCore.pyqtSignal(bool,tuple,tuple,tuple,float)
    #tuple里面嵌套四个信息：Highest，lowest，closing，Opening值，通过信号传递出去显示在界面
    getMarketSignalShowText  = QtCore.pyqtSignal(bool,tuple)
    #线程出现异常或者正常结束的信号，通过传递出去的值重置线程标志位
    getMarketfinishSignal = QtCore.pyqtSignal(bool)


    def __init__(self,parent=None):
        super(getMarketDataThread, self).__init__(parent)

    def run(self):
        try:
            Core_func.getTokenMarket()
        except Exception as err:
            self.getMarketfinishSignal.emit(False)
        try:
            Core_func.get_new_USD()
        except Exception as err:
            self.getMarketfinishSignal.emit(False)

#获取最新block的信息
class getLastBlockThread(QtCore.QThread):
    getLastBlockfinishSignal = QtCore.pyqtSignal(tuple)
    def __init__(self, parent=None):
        super(getLastBlockThread, self).__init__(parent)

    def run(self):
        lastBlockRet = Core_func.getLatestBlock()
        self.getLastBlockfinishSignal.emit(lastBlockRet)





























