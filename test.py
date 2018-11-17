import  subprocess
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip, QDesktopWidget, QMessageBox, QTextEdit, QLabel,
                             QPushButton, QApplication, QMainWindow, QAction, qApp, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QDialog, QFileDialog, QTableWidgetItem,
                             QLineEdit, QFrame, QAbstractItemView)
from test2 import loadConfigFile


def openWalton():
    try:
        #subprocess.Popen("walton.exe",shell=True)
        #subprocess.Popen("F:/WeChat/WeChat.exe")
        print("success" )
    except Exception as Error:
        print("jjjj"+ Error)

class tttt:
    def __init__(self):
        self.a =0
    def show(self):
        loadConfigFile.setValue(6,8)
        print("first: a = " +self.a + " b = "+ self.b)
        loadConfigFile.setValue(10, 20)
        print("first: a = " + self.a+ " b = " + self.b)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    openWalton()
    t = tttt()
    t.show()
    sys.exit(app.exec_())