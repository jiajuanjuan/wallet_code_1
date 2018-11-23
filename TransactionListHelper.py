from ApplicationHelper import  pathConfig
try:
    import cPickle as pickle
except ImportError:
    import pickle


#读取配置文件转成对象
#各个钱包的交易记录
class TransactionList:
    def __init__(self):
        self.addressTransactionsEntityList = []
        try:
            f = open(pathConfig.lastSettingPath + "TransactionList.xml", "rb")
            temp = pickle.load(f)
            self.addressTransactionsEntityList = temp.addressTransactionsEntityList
            f.close()
        except Exception as err:
            #如果加载TransactionList.xml失败，则正常new一个对象出来，作为新的对象，进行数据的添加
            pass

    def add(self,addressEntity):
        has = False
        #判断该钱包是否存在
        for i in range(len(self.addressTransactionsEntityList)):
            #存在
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
            if addressEntity.Address == address:
                return  addressEntity
        return  AddressTransactionsEntity()




#一个钱包的交易记录
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

#每笔交易的对象
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






