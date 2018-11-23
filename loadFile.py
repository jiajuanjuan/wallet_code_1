from Mainform import Example


class loadConfigFile:
    def __init__(self):
       pass

    def loadorCreateConfigFile(self):
        if not os.path.isfile(pathConfig.lastSettingPath + 'test.xml'):
            ret = Core_func.generateaddressXml()
        Example.addrdom = xml.dom.minidom.parse(pathConfig.lastSettingPath + "test.xml")
        xmlStr = self.addrdom.toprettyxml(indent='', newl='', encoding='utf-8')
        xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
        self.addrdom = xml.dom.minidom.parseString(xmlStr)
        xmlStr = self.addrdom.toprettyxml(indent='', newl='', encoding='utf-8')
        xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
        self.addrdom = xml.dom.minidom.parseString(xmlStr)
        self.addrroot = self.addrdom.documentElement

        if os.path.isfile(pathConfig.lastSettingPath + 'Wallets.xml'):
            self.walletdom = xml.dom.minidom.parse(pathConfig.lastSettingPath + 'Wallets.xml')
            xmlStr = self.walletdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.walletdom = xml.dom.minidom.parseString(xmlStr)
            xmlStr = self.walletdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.walletdom = xml.dom.minidom.parseString(xmlStr)
            self.walletroot = self.walletdom.documentElement
        else:
            ret = Core_func.generatewalletXml()
            self.walletdom = xml.dom.minidom.parse(pathConfig.lastSettingPath + 'Wallets.xml')
            xmlStr = self.walletdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.walletdom = xml.dom.minidom.parseString(xmlStr)
            xmlStr = self.walletdom.toprettyxml(indent='', newl='', encoding='utf-8')
            xmlStr = xmlStr.decode().replace('\t', '').replace('\n', '')
            self.walletdom = xml.dom.minidom.parseString(xmlStr)
            self.walletroot = self.walletdom.documentElement

    def praseConfigFile(self):