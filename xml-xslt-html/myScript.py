#!/usr/bin/python3
"""
Easy XSLT Transformation

XML + XSLT  = HTML
"""
# -*- coding: utf-8 -*-

print ('*** Easy XSLT Transformation ***')

from lxml import etree,html

# XML Data From File
# XSLT Data From File
print ("======== Example 1 ==========")
my_xml = etree.parse('myXML.xml')
my_xslt = etree.parse('myXSLT.xsl')
transform = my_xml.xslt (my_xslt)
print (transform)


# XML Data From string
# XSLT Data From File
print ("======== Example 2 ==========")
my_xml2 = etree.XML("<source><title>XSL</title><author>John Smith</author></source>")
my_xslt2 = etree.parse('myXSLT.xsl')
transform2 = my_xml.xslt (my_xslt)

my_html = html.fromstring (etree.tostring(transform2, encoding='utf-8',xml_declaration=True,pretty_print=False,method='html',with_tail=True))

print (transform2)
print (str (transform2))
res=etree.tostring(transform2, encoding='utf-8',xml_declaration=True,pretty_print=False,method='html',with_tail=True)
print(res)
#print (etree.tostring (my_xml2, pretty_print=True))

file = open("test.html", "w")
file.write(str(res))
file.close()
