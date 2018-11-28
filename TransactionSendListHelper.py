from ApplicationHelper import  pathConfig
from datetime import datetime
try:
    import cPickle as pickle
except ImportError:
    import pickle

class TransactionSendListHelper:
    def __init__(self):
        self.AddressTransactionSendList = []
        try:
            f = open(pathConfig.lastSettingPath + "TransactionSendList.xml", "rb")
            temp = pickle.load(f)
            self.AddressTransactionSendList = temp.AddressTransactionSendList
            f.close()
        except Exception as err:
            #�������TransactionList.xmlʧ�ܣ�������newһ�������������Ϊ�µĶ��󣬽������ݵ����
            pass

    def add(self, currentWalletAddress, TransactionSendEntity):
        has = False
        # �жϸ�Ǯ���Ƿ����
        for i in range(len(self.AddressTransactionSendList)):
            # ����
            if self.AddressTransactionSendList[i].Address == currentWalletAddress:
                self.AddressTransactionSendList[i].TransactionSendList.append(TransactionSendEntity)
                has = True
                break
        if has == False:
            addrTransSendEntity = AddressTransactionSendEntity()
            addrTransSendEntity.Address = currentWalletAddress
            addrTransSendEntity.TransactionSendList.append(TransactionSendEntity)
            self.AddressTransactionSendList.append(addrTransSendEntity)
        self.save()




    def save(self):
        f = open(pathConfig.lastSettingPath + "TransactionSendList.xml", "wb")
        pickle.dump(self, f, 0)
        f.close()

    def find(self,address):
        for i in range(len(self.AddressTransactionSendList)):
            addressSendEntity = self.AddressTransactionSendList[i]
            if addressSendEntity.Address.lower() == address.lower():
                return  addressSendEntity
        return  AddressTransactionSendEntity()


class AddressTransactionSendEntity:
    def __init__(self):
        self.Address=""
        self.TransactionSendList=[]


class TransactionSendEntity:
    def __init__(self,addressFrom,gasPrice,gas,value,addressTo,nonce):
        self.addressFrom=addressFrom
        self.gasPrice=gasPrice
        self.nonce=nonce
        self.gas=gas
        self.addressTo=addressTo
        self.value=value
        self.tx_hash=""
        #self.sign = "" ��Ҫ��������ݼ�ֵ�Ծ���ת��������ݣ�ֻ�������ʱ���õ�����ʱ�Ȳ���¼�������������ʧ����Ҫ�ظ�����Ļ����¼�������Լ����ظ�ת��
        self.timestamp= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.blockType="Submitted"




