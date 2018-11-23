from ApplicationHelper import  pathConfig
try:
    import cPickle as pickle
except ImportError:
    import pickle
from  pprint import  pprint
class HistoryBalanceHelper:
    def __init__(self):
        self.addressBalanceEntityList = []
        try:
            f = open(pathConfig.lastSettingPath + "HistoryBalance.xml", "rb")
            temp = pickle.load(f)
            print('####------------------------------')
            pprint(temp)
            print(len(temp.addressBalanceEntityList))
            print('####------------------------------end')
            self.addressBalanceEntityList = temp.addressBalanceEntityList
            f.close()
        except Exception as err:
            print("HistoryBalanceHelper Error : "+ str(err))
            #如果加载HistoryBalance.xml失败，则正常new一个对象出来，作为新的对象，进行数据的添加
            pass

    def add(self,addressEntity):
        has = False
        # 判断该钱包是否存在
        for i in range(len(self.addressBalanceEntityList)):
            # 存在
            if self.addressBalanceEntityList[i].address == addressEntity.address:
                self.addressBalanceEntityList[i] = addressEntity
                has = True
                break
        if has == False:
            self.addressBalanceEntityList.append(addressEntity)
        self.save()

    def save(self):
        f = open(pathConfig.lastSettingPath + "HistoryBalance.xml", "wb")
        pickle.dump(self, f, 0)
        f.close()

    def find(self,address):
        try:
            for i in range(len(self.addressBalanceEntityList)):
                addressEntity = self.addressBalanceEntityList[i]
                if addressEntity.address == address:
                    return addressEntity
            return AddressBalanceEntity()
        except Exception as err:
            print("find Error : "+ str(err))
            return AddressBalanceEntity()



class AddressBalanceEntity:
    def __init__(self):
        self.address=""
        self.HistoryBalanceList=[]


class BalanceEntityList:
    def __init__(self):
        self.HistoryBalance = []

class BalanceEntity:
    def __init__(self):
        self.address=""
        self.history_balance=""
        self.block=""
        self.utc_timestamp=""