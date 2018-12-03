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

