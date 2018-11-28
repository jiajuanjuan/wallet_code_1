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

#����20�������߳�
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
            # ���ֵ�ת�ɶ���
            balist =  BalanceEntityList()
            # �����󵽵�����ת���ֵ�
            print("$$"+strBalance + "$$")
            balanceDict = json.loads(s=strBalance)
            balist.__dict__ = balanceDict

            addressBaEntity = AddressBalanceEntity()

            # ��¼��ǰ����ĵ�ַ����add��ʱ���ֹ�ظ�
            addressBaEntity.address = self.address
            # �����б���ֵ�һ����ת�ɶ���
            for i in range(len(balist.HistoryBalance)):
                bEntity = BalanceEntity()
                bEntity.__dict__ = balist.HistoryBalance[i]
                # ʱ�����ת��
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

#���½��׼�¼���߳�
class getTransactionDataThread(QtCore.QThread):
    getTransfinishSignal = QtCore.pyqtSignal(bool)
    def __init__(self,addr, parent=None):
        super(getTransactionDataThread, self).__init__(parent)
        self.address = addr
    def run(self):
        #��ȡ���
        #balance = 0
        #nonce = 0
        try:
            #���������balance ��nonceû��ʲô���ã��Ȳ�����
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
            # ��ȡ���׼�¼
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
        #���ñ�����¼��������֤һ�ν��׼�¼��ȡ�Ĺ�����lastBlock��ֵ��һ����
        lastBlock = ApplicationHelper.lastBlock

        try:

            lstEntity = AccountTransactionsListEntity()
            AccountTransListDict = json.loads(s=strTrans)
            lstEntity.__dict__ = AccountTransListDict
            # ��ʼ��һ��Ǯ��
            addressEntity = AddressTransactionsEntity()
            addressEntity.Address = self.address
            addressEntity.UpdateTime = self.time
            # --------------------------------------------------------------------------------------
            #�����󵽵�����ˢ��TransactionList.xml����Ϣ
            for i in range(len(lstEntity.tx_pagination_details)):
                # ����һ���˻�����
                accountEntity = AccountTransactionsEntity()
                # ����������Ľ������ݶ�dict��ֵ���˻����׶����dict����dict��ʼ������
                accountEntity.__dict__ = lstEntity.tx_pagination_details[i]
                print("---------------accountEntity value : " + str(accountEntity.value))
                # ����blockType������
                if lastBlock - accountEntity.blockNumber >= 11:
                    accountEntity.blockType = ApplicationHelper.transSuccess
                else:
                    accountEntity.blockType = str(lastBlock - accountEntity.blockNumber + 1) + '/12'
                # ����ÿ�ʽ��׵�������send ����receive
                if accountEntity.addressFrom.lower() == self.address.lower():
                    accountEntity.transType = ApplicationHelper.transSend
                else:
                    accountEntity.transType = ApplicationHelper.transReceive
                # ʱ�����ת��
                time_s = datetime.strptime(accountEntity.utc_timestamp, "%Y-%m-%d %H:%M:%S")
                accountEntity.utc_timestamp = Core_func.utc2local(time_s).strftime('%Y-%m-%d %H:%M:%S')
                # ���˻����׵Ķ�����ӵ�Ǯ�����˻������б���
                addressEntity.AccountTransactionsEntityList.append(accountEntity)
            tHelper = TransactionList()
            tHelper.add(addressEntity)
            # --------------------------------------------------------------------------------------
            # ����transSendlist�������Ϣ
            tsHelper = TransactionSendListHelper()
            addressTransSendList = tsHelper.find(self.address)
            for i in range(len(addressTransSendList.TransactionSendList)):
                accountSendEntity = addressTransSendList.TransactionSendList[i]
                bhas = False
                if accountSendEntity.blockType != ApplicationHelper.transSuccess:
                    for i in range(len(addressEntity.AccountTransactionsEntityList)):
                        accountEntity = addressEntity.AccountTransactionsEntityList[i]
                        # �ж�send�Ľ�����Ϣ�Ƿ��Ѿ������󵽵�list�д���(��hashֵ�ж�)������Ѿ�������transSend����Ľ������;͸�ΪSuccess�������ݲ�����
                        if accountSendEntity.tx_hash.lower() == accountEntity.tx_hash.lower():
                            bhas = True
                            break
                    if bhas == True:
                        accountSendEntity.blockType = ApplicationHelper.transSuccess
                    else:
                        # C#�ǻ����lastnonce�ж��Ƿ�ʧ�ܵģ������ʱû���ж�
                        pass
                    tsHelper.save()
            # --------------------------------------------------------------------------------------
            return
        except Exception as err:
            print("2Error : " + str(err))
            #self.getTransfinishSignal.emit(False)
            return

#�����г���Ϣ���߳�
class getMarketDataThread(QtCore.QThread):
    #����4����Ϣ ��x�����Ϣ��y�����Ϣ����ֹ���ڣ�usd��ֵ��ͨ���źŴ��ݸ����棬������Ƴ���
    getMarketSignalShowChart = QtCore.pyqtSignal(bool,tuple,tuple,tuple,float)
    #tuple����Ƕ���ĸ���Ϣ��Highest��lowest��closing��Openingֵ��ͨ���źŴ��ݳ�ȥ��ʾ�ڽ���
    getMarketSignalShowText  = QtCore.pyqtSignal(bool,tuple)
    #�̳߳����쳣���������������źţ�ͨ�����ݳ�ȥ��ֵ�����̱߳�־λ
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

#��ȡ����block����Ϣ
class getLastBlockThread(QtCore.QThread):
    getLastBlockfinishSignal = QtCore.pyqtSignal(tuple)
    def __init__(self, parent=None):
        super(getLastBlockThread, self).__init__(parent)

    def run(self):
        lastBlockRet = Core_func.getLatestBlock()
        self.getLastBlockfinishSignal.emit(lastBlockRet)





























