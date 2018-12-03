# -*- coding: utf-8 -*-
import getpass
import json
import os
import sys
import time
import requests
from eth_account import Account
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from web3.auto import w3
from datetime import datetime
# import commands
import subprocess
import eth_utils
import eth_hash
#精确计算,保持精度
from decimal import *

"""
failure reason for Generate_Two_Key function
10000: password length less than 6
10001: two passwords do not match
"""


from ApplicationHelper import pathConfig

from xml.dom import minidom
import MyXml

def generateaddressXml():
    doc = minidom.Document()

    rootElement = doc.createElement('ArrayOfAddressEntity')
    rootElement.setAttribute('xmlns:xsd','"https://www.w3.org/2001/XMLSchema"')

    doc.appendChild(rootElement)

    f = open(pathConfig.lastSettingPath + 'test.xml', 'w')
    doc.writexml(f, addindent='    ', newl='\n', encoding="utf-8")
    f.close()

    return (doc,rootElement)

def addaddressxml(doc,rootElement,accountname,address):
    AddressEntity = doc.createElement('AddressEntity')
    rootElement.appendChild(AddressEntity)
    # childElement.setAttribute('id', str(pythonId))
    UAddress = doc.createElement('UAddress')
    AddressEntity.appendChild(UAddress)

    GuidNo = doc.createElement('GuidNo')
    AddressEntity.appendChild(GuidNo)

    AccountName = doc.createElement('AccountName')
    AddressEntity.appendChild(AccountName)
    name = doc.createTextNode(accountname)
    AccountName.appendChild(name)

    Address = doc.createElement('Address')
    AddressEntity.appendChild(Address)
    addr = doc.createTextNode(address)
    Address.appendChild(addr)

    doc.appendChild(rootElement)
    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)


    f = open(pathConfig.lastSettingPath + 'test.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def editaddressxml(doc,rootElement,accountname,row):
    addrentity = rootElement.getElementsByTagName('AddressEntity')[row]
    nametag = addrentity.getElementsByTagName('AccountName')[0].childNodes[0]
    nametag.nodeValue=accountname

    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)

    f = open(pathConfig.lastSettingPath + 'test.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def generatewalletXml():
    doc = minidom.Document()
    rootElement = doc.createElement('ArrayOfWalletBaseEntity')
    rootElement.setAttribute('xmlns:xsd', '"https://www.w3.org/2001/XMLSchema"')
    doc.appendChild(rootElement)
    f = open(pathConfig.lastSettingPath + 'Wallets.xml', 'w')
    #os.path.realpath(__file__)
    doc.writexml(f, addindent='    ', newl='\n',encoding="utf-8")
    f.close()
    return (doc, rootElement)

def addwalletxml(doc,rootElement,accountname,address,filename,GMN='false'):
    WalletBaseEntity = doc.createElement('WalletBaseEntity')
    rootElement.appendChild(WalletBaseEntity)
    Address = doc.createElement('Address')
    WalletBaseEntity.appendChild(Address)
    addr = doc.createTextNode(address)
    Address.appendChild(addr)
    # childElement.setAttribute('id', str(pythonId))
    UUID = doc.createElement('UUID')
    WalletBaseEntity.appendChild(UUID)

    AccountName = doc.createElement('AccountName')
    WalletBaseEntity.appendChild(AccountName)
    name = doc.createTextNode(accountname)
    AccountName.appendChild(name)

    FileName = doc.createElement('FileName')
    WalletBaseEntity.appendChild(FileName)
    fname = doc.createTextNode(filename)
    FileName.appendChild(fname)

    GMNtag = doc.createElement('GMN')
    WalletBaseEntity.appendChild(GMNtag)
    gmn = doc.createTextNode(GMN)
    GMNtag.appendChild(gmn)

    doc.appendChild(rootElement)
    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)

    f = open(pathConfig.lastSettingPath +'Wallets.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def editwalletxml(doc,rootElement,accountname,row):
    walletentity = rootElement.getElementsByTagName('WalletBaseEntity')[row]
    nametag = walletentity.getElementsByTagName('AccountName')[0].childNodes[0]
    nametag.nodeValue=accountname

    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)

    f = open(pathConfig.lastSettingPath +'Wallets.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def Generate_Three_Key(password1, password2):
    print("jjj1 Generate_Three_Key")
    if password1 == password2:
        pass1 = password1
        pass2 = password2
        print("jjj2 password1 == password2")
        if len(pass1) < 6:
            print('less than 6')
            return (0, 10000)
        else:
            print("jjj3 create password")
            acct = Account.create(password1)
            print("jjj4 create password")
            public_key = acct.address
            print("jjj5 create password")
            private_key = acct.privateKey
            print("jjj6 create password")
            encrypted = Account.encrypt(private_key, password1)
            print("jjj6 create password")
            # cmd = 'ma -genkey ' + '-pass ' + password2
            # a = subprocess.getstatusoutput(cmd)
            # if a[0] == 0:
            #     ret = (a[1].split('{')[1].split('}')[0], a[1].split('{')[2].split('}')[0])
            #     # return ret      
            #     acct = Account.privateKeyToAccount(ret[1])
            #     public_key = acct.address
            #     encrypted = Account.encrypt(ret[1], password2)
            #     return (1, [public_key, ret[1], json.dumps(encrypted),ret[0]])
            return (1, [public_key, w3.toHex(private_key), json.dumps(encrypted)])
    else:
        print("jjj4 password")
        print('wrong')
        return (0, 10001)


"""
failure reason for Generate_Key function
"""


def Import_From_Private(secret, password1):
    print("this is imported private key", secret)
    acct = Account.privateKeyToAccount(secret)
    public_key = acct.address
    encrypted = Account.encrypt(secret, password1)
    return (1, public_key, json.dumps(encrypted))


def Import_Keystore(passphrase, filecontent):
    try:
        # content = json.loads(filecontent)
        private_key = w3.toHex(Account.decrypt(filecontent, passphrase))
        public_key = Account.privateKeyToAccount(private_key).address
        encrypted = Account.encrypt(private_key, passphrase)
        return (1, [public_key, private_key], json.dumps(encrypted))
    except Exception as err:
        print("Import_Keystore Error :" + str(err))
        return (0, 10000)


def Import_mnemonic(passphrase1, passphrase2, mnemonicwords):
    if passphrase1 == passphrase2:
        cmd = 'ma -m \"' + mnemonicwords + '\" -pass \"' + passphrase2 +'\"'
        a = subprocess.getstatusoutput(cmd)
        if a[0] == 0:
            ret = (a[1].split('{')[1].split('}')[0],a[1].split('{')[2].split('}')[0])
            acct = Account.privateKeyToAccount(ret[1])
            public_key = acct.address
            encrypted = Account.encrypt(ret[1], passphrase2)
            return (1, [public_key, ret[1],json.dumps(encrypted)])
        else:
            return (0, 0)
    else:
        return (0, 0)


def Transaction_out(private_key, toaddr, value, gas, gasprice, nonce):
    toaddr = w3.toChecksumAddress(toaddr)
    acct = Account.privateKeyToAccount(private_key)
    #public_key = acct.address
    transaction = {
        'to': toaddr,
        'value': int(Decimal(value) * (10 ** 18)),
        'gas': int(gas),
        'gasPrice': int(Decimal(gasprice) * (10 ** 18)),
        'nonce': nonce,
        'chainId': 15
    }
    print(transaction)
    #key = '0x4c0883a69102937d6231471b5dbb6204fe5129617082792ae468d01a3f362318'
    try:
        signed = w3.eth.account.signTransaction(transaction, private_key)
        print("sendData :" + w3.toHex(signed.rawTransaction))
    except Exception as err:
        print("signTransaction Error : " + str(err))
        return (False, nonce, "")

    try:
        print("jjjjjjjjjjjjjjnonce : " + str(nonce))
        tx_hash = requests.get("https://waltonchain.net:18950/api/sendRawTransaction/" + w3.toHex(signed.rawTransaction)).json()
    except Exception as err:
        print("sendRawTransaction Error : " + str(err))
        return (False,nonce,str(err))

    #判断如果是nonce too low的错误，则将nonce的值自动+1 再请求
    if "error" in tx_hash.keys():
        try:
            while tx_hash["error"] == "nonce too low":
                nonce += 1
                transaction = {
                    'to': toaddr,
                    'value': int(Decimal(value) * (10 ** 18)),
                    'gas': int(gas),
                    'gasPrice': int(Decimal(gasprice) * (10 ** 18)),
                    'nonce': nonce,
                    'chainId': 15
                }
                signed = w3.eth.account.signTransaction(transaction, private_key)
                newtx_hash = requests.get(
                    "https://waltonchain.net:18950/api/sendRawTransaction/" + w3.toHex(signed.rawTransaction)).json()
                if "error" not in newtx_hash.keys():
                    return (True, nonce, newtx_hash["tx_hash"])
        except Exception as err:
            print("re Transaction error : " + str(err))
            return (False, nonce, str(err))
        return (False, nonce, tx_hash["error"])
    return  (True,nonce,tx_hash["tx_hash"])
    #返回值的格式 1、返回请求成功还是失败，2、返回nonce的值（可能经过了自加加的操作），返回请求得到的结果



def startCPUMining():
    pass


def stopCPUMining():
    pass





def getMiningRecord(public_key):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getMinedBlocksPagination/"+public_key+"/1/30").json()
        return (1, r1['tx_pagination_details'])
    except Exception as err:
        print(err)
        return (0, err)




def getTransactionInfo(hash):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getTransactionInfo/"+hash).json()
        return (1, r1['tx_details'])
    except Exception as err:
        print(err)
        return (0, err)
#api/getAccountTransactionsAllPagination/" + address + "/1/100"


def getTokenMarket():
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getMarket/WTC/30").json()
        return (True, r1['token_market'])
    except Exception as err:
        print("getTokenMarket Error : "+ str(err))
        return (False, str(err))





    


def getCurrentNodesDistribution():
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getCurrentNodesDistribution").json()
        return (1, r1)
    except Exception as err:
        print(err)
        return (0, err)


def getLatestBlock():
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getLatestBlock").json()
        return (True, r1['latest_block'])
    except Exception as err:
        print("getLatestBlock Error:"+ str(err))
        return (False, err)

def getDifficulty():
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getWTCBlockDifficulty/1").json()
        return (1, r1)
    except Exception as err:
        print(err)
        return (0, err)


def getGasPrice():
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getGasPrice").json()
        return (1, r1)
    except Exception as err:
        print(err)
        return (0, err)


def getHashRate():
    try:
        r1 = requests.post('https://httpsbin.org/post', data={
            "jsonrpc": "2.0", "method": "eth_hashrate", "params": [], "id": 2}).json()
        return (1, r1)
    except Exception as err:
        print(err)
        return (0, err)

def utc2local(utc_st):
    now_stamp = time.time()
    local_time = datetime.fromtimestamp(now_stamp)
    utc_time = datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st
#
# print(utc2local(timenow))
#
# ret = getMiningRecord('0xfbf36b7c56258dc3e29769c1a686250b8b002de3')
# print(ret)

def generatetransXml():
    doc = minidom.Document()
    rootElement = doc.createElement('ArrayOfAddressTransactionsEntity')
    rootElement.setAttribute('xmlns:xsd', '"https://www.w3.org/2001/XMLSchema"')
    doc.appendChild(rootElement)
    f = open(pathConfig.lastSettingPath + 'trans.xml', 'w')
    doc.writexml(f, addindent='  ', newl='\n')
    f.close()

    return (doc, rootElement)

def addtransaddrxml(doc,rootElement,address,updatetime):
    AddressTransactionsEntity = doc.createElement('AddressTransactionsEntity')
    rootElement.appendChild(AddressTransactionsEntity)

    Address = doc.createElement('Address')
    AddressTransactionsEntity.appendChild(Address)
    addr = doc.createTextNode(address)
    Address.appendChild(addr)

    UpdateTime = doc.createElement('UpdateTime')
    AddressTransactionsEntity.appendChild(UpdateTime)
    updatet = doc.createTextNode(updatetime)
    UpdateTime.appendChild(updatet)

    TransactionList = doc.createElement('TransactionList')
    AddressTransactionsEntity.appendChild(TransactionList)

    # doc.appendChild(rootElement)
    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)


    f = open(pathConfig.lastSettingPath + 'trans.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def addtranslistxml\
    (doc,rootElement,address,updatetime,fromaddr,blocknum,
     toaddr,gasprice,blockhash,transacindex,txhash,Gas,Value,utctimestamp,transtype,blocktype):

    foundaddr = 0
    for AddressTransactionsEntity in rootElement.getElementsByTagName('AddressTransactionsEntity'):
        if address == AddressTransactionsEntity.getElementsByTagName('Address')[0].firstChild.data:
            # walletentity = AddressTransactionsEntity.getElementsByTagName('UpdateTime')
            updatet = AddressTransactionsEntity.getElementsByTagName('UpdateTime')[0].firstChild
            updatet.nodeValue=updatetime

            AccountTransactionsEntity = doc.createElement('AccountTransactionsEntity')
            newtrans = AddressTransactionsEntity.getElementsByTagName('TransactionList')[0]
            newtrans.appendChild(AccountTransactionsEntity)

            addressFrom = doc.createElement('addressFrom')
            AccountTransactionsEntity.appendChild(addressFrom)
            faddr = doc.createTextNode(fromaddr)
            addressFrom.appendChild(faddr)

            blockNumber = doc.createElement('blockNumber')
            AccountTransactionsEntity.appendChild(blockNumber)
            blockNo = doc.createTextNode(blocknum)
            blockNumber.appendChild(blockNo)

            gasPrice = doc.createElement('gasPrice')
            AccountTransactionsEntity.appendChild(gasPrice)
            gp = doc.createTextNode(gasprice)
            gasPrice.appendChild(gp)

            blockHash = doc.createElement('blockHash')
            AccountTransactionsEntity.appendChild(blockHash)

            transacIndex = doc.createElement('transacIndex')
            AccountTransactionsEntity.appendChild(transacIndex)
            tranid = doc.createTextNode(transacindex)
            transacIndex.appendChild(tranid)

            tx_hash = doc.createElement('tx_hash')
            AccountTransactionsEntity.appendChild(tx_hash)
            hash = doc.createTextNode(txhash)
            tx_hash.appendChild(hash)

            gas = doc.createElement('gas')
            AccountTransactionsEntity.appendChild(gas)
            GAS = doc.createTextNode(Gas)
            gas.appendChild(GAS)

            addressTo = doc.createElement('addressTo')
            AccountTransactionsEntity.appendChild(addressTo)
            taddr = doc.createTextNode(toaddr)
            addressTo.appendChild(taddr)

            value = doc.createElement('value')
            AccountTransactionsEntity.appendChild(value)
            val = doc.createTextNode(Value)
            value.appendChild(val)

            utc_timestamp = doc.createElement('utc_timestamp')
            AccountTransactionsEntity.appendChild(utc_timestamp)
            utct = doc.createTextNode(utctimestamp)
            utc_timestamp.appendChild(utct)

            transType = doc.createElement('transType')
            AccountTransactionsEntity.appendChild(transType)
            ttype = doc.createTextNode(transtype)
            transType.appendChild(ttype)

            blockType = doc.createElement('blockType')
            AccountTransactionsEntity.appendChild(blockType)
            btype = doc.createTextNode(blocktype)
            blockType.appendChild(btype)

            foundaddr = 1
            break
    if foundaddr == 0:
        addtransaddrxml(doc, rootElement, address, updatetime)
        addtranslistxml \
            (doc, rootElement, address, updatetime, fromaddr, blocknum,
             toaddr, gasprice, blockhash, transacindex, txhash, Gas, Value, utctimestamp, transtype, blocktype)


    # doc.appendChild(rootElement)
    xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
    xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
    doc = minidom.parseString(xmlStr)


    f = open(pathConfig.lastSettingPath + 'trans.xml', 'w')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

def edittransxml(doc,rootElement,address,blocktype,row):
    for AddressTransactionsEntity in rootElement.getElementsByTagName('AddressTransactionsEntity'):
        if address == AddressTransactionsEntity[0].childNodes[0]:
            TransactionList = AddressTransactionsEntity[0].childNodes[2]
            trans = TransactionList.getElementsByTagName('AccountTransactionsEntity')[row]
            typetag = trans.getElementsByTagName('blockType')[0].childNodes[0]
            typetag.nodeValue=blocktype

            xmlStr = doc.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            doc = minidom.parseString(xmlStr)

            f = open(pathConfig.lastSettingPath +'trans.xml', 'w')
            doc.writexml(f, addindent=' ', newl='\n')
            f.close()

            break

def generateSettingXml():
    doc = minidom.Document()
    rootElement = doc.createElement('MiningEntity')
    rootElement.setAttribute('xmlns:xsd', '"https://www.w3.org/2001/XMLSchema"')
    doc.appendChild(rootElement)
    password = doc.createElement('MinerP')
    rootElement.appendChild(password)
    addr = doc.createTextNode(' ')
    password.appendChild(addr)
    wallet = doc.createElement('wallet')
    rootElement.appendChild(wallet)
    wa = doc.createTextNode(' ')
    wallet.appendChild(wa)
    minewallet = doc.createElement('minewallet')
    rootElement.appendChild(minewallet)
    minewa = doc.createTextNode(' ')
    minewallet.appendChild(minewa)
    minediff = doc.createElement('Difficulty')
    rootElement.appendChild(minediff)
    #diff = doc.createTextNode('478705014976')
    diff = doc.createTextNode('Getting')

    minediff.appendChild(diff)
    minereward = doc.createElement('Mining_reward')
    rootElement.appendChild(minereward)
    #reward = doc.createTextNode('3')
    reward = doc.createTextNode('Getting')
    minereward.appendChild(reward)
    f = open(pathConfig.lastSettingPath + 'setting.xml', 'w')
    doc.writexml(f, addindent='    ', newl='\n', encoding="utf-8")
    f.close()

    return (doc, rootElement)



def get_new_USD():
    try:
        r1 = requests.get("https://waltonchain.net:18950/api/getAllCoinMarketPrice").json()
        for i in range(len(r1)):
            if r1[i]['id'] == 'waltonchain':
                new_USD = r1[i]['price_usd']
                return (True,new_USD)
        return (False,0)
    except Exception as err:
        print("get_new_USD Error : "+ str(err))
        return (False, 0)


#获取余额暂时没用到
"""
def getAccountBalance(address):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getBalance/" + address).json()
        return (True, r1['Balance'])
    except Exception as err:
        print("Error: " + str(err))
        return (False, err)    
"""
#获取Nonce
def getAccountNonce(address):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getSendTransactionNonce/" + address).json()["send_nonce"]
        return (True, r1)
    except Exception as err:
        print("Error: " + str(err))
        return (False, err)

#获取该地址的100条交易记录
def getTransactionRecord(address):
    try:
        r1 = requests.get(
            "https://waltonchain.net:18950/api/getAccountTransactionsAllPagination/" + address + "/1/100").content.decode()
        #return (True, r1['tx_pagination_details'])
        return  (True,r1)
    except Exception as err:
        print("Error: " + str(err))
        return (False, err)

#获取该地址的20天的余额，20代表20天的数据
def getHistoryBalance(address):
    print("address : " + address)
    try:
        r1 = requests.get("https://waltonchain.net:18950/api/getHistoryBalance/"+address+'/'+"20").content.decode()
        print("request result: ")
        print(r1)
        #return (True, r1['HistoryBalance'])
        return (True ,r1)
    except Exception as err:
        print("getHistoryBalance Error: ")
        print(err)
        print("getHistoryBalance Error end : ")
        return (False, err)

#是要删掉的
def getTransactionRecord_day(public_key, interval):
    try:
        r1 = requests.get("https://waltonchain.net:18950/api/getHistoryBalance/"+public_key+'/'+interval).json()
        return (True, r1['HistoryBalance'])
    except Exception as err:
        #print("Error ：" + str(err))
        return (False, err)









