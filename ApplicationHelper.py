
class pathConfig:
    keystoresPath = "./keystores/"
    picPath = ":/pic/"
    lastSettingPath = "./Temp/"

class  ApplicationHelper:
    WaltonUrl = "https://waltonchain.net:18950/"
    lastBlock = 0
    transSend = "Send"
    transReceive = "Receive"
    transSuccess = "Success"
    Wei = 10**18

#对list中对象的时间属性进行排序
import  time
class sortByTimeOfObj:
    def date_compare(item1, item2):
        t1 = time.mktime(time.strptime(item1.utc_timestamp, '%Y-%m-%d %H:%M:%S'))
        t2 = time.mktime(time.strptime(item2.utc_timestamp, '%Y-%m-%d %H:%M:%S'))
        if t1 < t2:
            return -1
        elif t1 > t2:
            return 1
        else:
            return 0






