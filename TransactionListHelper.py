from ApplicationHelper import  pathConfig,ApplicationHelper
try:
    import cPickle as pickle
except ImportError:
    import pickle
#��ȷ����,���־���
from decimal import *



#��ȡ�����ļ�ת�ɶ���
#����Ǯ���Ľ��׼�¼
class TransactionList:
    def __init__(self):
        self.addressTransactionsEntityList = []
        try:
            f = open(pathConfig.lastSettingPath + "TransactionList.xml", "rb")
            temp = pickle.load(f)
            self.addressTransactionsEntityList = temp.addressTransactionsEntityList
            f.close()
        except Exception as err:
            #�������TransactionList.xmlʧ�ܣ�������newһ�������������Ϊ�µĶ��󣬽������ݵ����
            pass

    def add(self,addressEntity):
        has = False
        #�жϸ�Ǯ���Ƿ����
        for i in range(len(self.addressTransactionsEntityList)):
            #����
            if self.addressTransactionsEntityList[i].Address == addressEntity.Address:
                self.addressTransactionsEntityList[i] = addressEntity
                has = True
                break
        if has == False:
            self.addressTransactionsEntityList.append(addressEntity)
        self.save()



    def save(self):
        f = open(pathConfig.lastSettingPath + "TransactionList.xml", "wb")
        pickle.dump(self, f, 0)
        f.close()

    def find(self,address):
        for i in range(len(self.addressTransactionsEntityList)):
            addressEntity = self.addressTransactionsEntityList[i]
            if addressEntity.Address.lower() == address.lower():
                return  addressEntity
        return  AddressTransactionsEntity()




#һ��Ǯ���Ľ��׼�¼
class AddressTransactionsEntity:
    def __init__(self):
        self.Address=""
        self.UpdateTime=""
        self.AccountTransactionsEntityList = []


class AccountTransactionsListEntity:
    def __init__(self):
        self.total_records=""
        self.return_counts=""
        self.total_page=""
        self.current_page=""
        self.counts_per_page=""
        self.tx_pagination_details =[]

#ÿ�ʽ��׵Ķ���
class AccountTransactionsEntity:
    def __init__(self):
        self.addressFrom = ""
        self.blockNumber = ""
        self.gasPrice = ""
        self.gasUsed = ""
        self.blockHash = ""
        self.transacIndex = ""
        self.tx_hash = ""
        self.gas = ""
        self.addressTo = ""
        self.value = ""
        self.utc_timestamp = ""
        self.transType = ""
        self.blockType = ""

    def setValue(self,sendEntity):
        self.addressFrom = sendEntity.addressFrom
        self.gasPrice = sendEntity.gasPrice
        self.blockHash = sendEntity.tx_hash
        self.transacIndex = ""
        self.tx_hash = sendEntity.tx_hash
        self.gas = sendEntity.gas
        self.addressTo = sendEntity.addressTo
        self.value = sendEntity.value
        self.utc_timestamp = sendEntity.timestamp
        self.transType = ApplicationHelper.transSend
        self.blockType = sendEntity.blockType







