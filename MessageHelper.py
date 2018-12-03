# -*- coding: utf-8 -*-
from ApplicationHelper import  pathConfig
try:
    import cPickle as pickle
except ImportError:
    import pickle

class MessageListHelper:
    def __init__(self):
        self.AddressMessageList = []
        try:
            f = open(pathConfig.lastSettingPath + "Message.xml", "rb")
            temp = pickle.load(f)
            self.AddressMessageList = temp.AddressMessageList
            f.close()
        except Exception as err:
            #如果加载文件失败，则正常new一个对象出来，作为新的对象，进行数据的添加
            pass

    def save(self):
        f = open(pathConfig.lastSettingPath + "Message.xml", "wb")
        pickle.dump(self, f, 0)
        f.close()

    def find(self,address):
        for i in range(len(self.AddressMessageList)):
            addressMEntity = self.AddressMessageList[i]
            if addressMEntity.Address.lower() == address.lower():
                return  addressMEntity
        #找不到则new一个新的添加到list中去，并返回new出来的对象
        newAddressMEntity = AddressMessageEntity()
        newAddressMEntity.Address = address
        self.AddressMessageList.append(newAddressMEntity)
        return  newAddressMEntity

    def addHashToAddressEntity(self,AddressEntity,tx_hash):
        has = False
        if tx_hash in AddressEntity.Tx_hashList:
            has = True
        if has == False:
            AddressEntity.Tx_hashList.append(tx_hash);

class AddressMessageEntity:
    def __init__(self):
        self.Address = ""
        self.Tx_hashList = []