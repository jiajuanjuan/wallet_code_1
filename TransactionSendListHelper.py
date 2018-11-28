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
            #如果加载TransactionList.xml失败，则正常new一个对象出来，作为新的对象，进行数据的添加
            pass

    def add(self, currentWalletAddress, TransactionSendEntity):
        has = False
        # 判断该钱包是否存在
        for i in range(len(self.AddressTransactionSendList)):
            # 存在
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
        #self.sign = "" 需要请求的数据键值对经过转化后的数据，只在请求的时候用到，暂时先不记录，如果后期请求失败需要重复请求的话则记录下来可以减少重复转换
        self.timestamp= datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.blockType="Submitted"




