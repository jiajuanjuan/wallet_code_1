from PyQt5 import QtCore
import requests
import json
from Mainform import Figure_Canvas

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
            while 1:
                try:
                    response = requests.get(
                        "https://waltonchain.net:18950/api/getHistoryBalance/" + self.addr + '/' + self.interval,
                        timeout=(5, 10))
                    if response.status_code == 200:
                        return (1, response.json()['HistoryBalance'])
                except Exception as err:
                    print("Network Error : " + str(err))




