# -*- coding: utf-8 -*-
#重写minidom的writexml函数，使得再次写入的时候不会有多余的空行
import xml
from xml.dom import minidom
import codecs
def fixed_writexml(self, writer, indent="", addindent="", newl=""):
    # addindent = indentation to add to higher levels
    # indent = current indentation
    # newl = newline string
    writer.write(indent + "<" + self.tagName)

    attrs = self._get_attributes()
    a_names = attrs.keys()
    #a_names.sort()

    for a_name in a_names:
        writer.write(" %s=\"" % a_name)
        minidom._write_data(writer, attrs[a_name].value)
        writer.write("\"")
    if self.childNodes:
        if len(self.childNodes) == 1 \
                and self.childNodes[0].nodeType == minidom.Node.TEXT_NODE:
            writer.write(">")
            self.childNodes[0].writexml(writer, "", "", "")
            writer.write("</%s>%s" % (self.tagName, newl))
            return
        writer.write(">%s" % (newl))
        for node in self.childNodes:
            if node.nodeType is not minidom.Node.TEXT_NODE:
                node.writexml(writer, indent + addindent, addindent, newl)
        writer.write("%s</%s>%s" % (indent, self.tagName, newl))
    else:
        writer.write("/>%s" % (newl))
minidom.Element.writexml = fixed_writexml

#xml转dict
from collections import defaultdict
def etree_to_dict(t):
    d = {t.tag: {} if t.attrib else None}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        d = {t.tag: {k: v[0] if len(v) == 1 else v
                     for k, v in dd.items()}}
    if t.attrib:
        d[t.tag].update(('@' + k, v)
                        for k, v in t.attrib.items())
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
              d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

import  xmltodict
def trans_dict_to_xml(jsdict):
    xmlText = ''
    try:
        xmlText = xmltodict.unparse(jsdict, encoding='utf-8')
    except:
        xmlText = xmltodict.unparse({'request': jsdict}, encoding='utf-8')
    return xmlText

import re
class formatxml:
    def __init__(self):
        pass
    def getSpace(self,level):
        space = '\n'
        for i in range(level):
            space = space + '    '
        return space
    def printXml(self,xml_str):
        # xml_list=xml_str.split('([>])')
        new_xml_list = ""
        head = xml_str[0:0]
        xml_str = xml_str[0:]
        xml_list = re.split(r'([>])', xml_str)
        xml_list = ["".join(i) for i in zip(xml_list[0::2], xml_list[1::2])]
        level = 0
        for node in xml_list:
            if (re.match(r'<\?xml .*version.*\?>', node)):
                new_xml_list = new_xml_list + new_xml_list + node
                continue
            elif (re.match(r'<[^\?^/].*[^/]>', node)):
                new_xml_list = new_xml_list + self.getSpace(level) + node
                level = level + 1
                continue
            elif (re.match(r'</.*[^/]>', node)):
                level = level - 1
                new_xml_list = new_xml_list + self.getSpace(level) + node
                continue
            elif (re.match(r'<[^/].*/>', node)):
                new_xml_list = new_xml_list + self.getSpace(level) + node
            elif (re.match(r'.+</.*[^/]>', node)):
                new_xml_list = new_xml_list + node
                level = level - 1
        return new_xml_list