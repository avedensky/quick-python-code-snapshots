#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Working with logging module
"""


import logging

#logging.basicConfig(level = logging.DEBUG)
#CRITICAL:root:Critical message

#logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)
#log2Console.py[LINE:11]# DEBUG    [2017-06-27 13:38:06,309]  Debug message

#logging.basicConfig(format = u"%(asctime)s - %(name)s - %(levelname)s - %(message)s", level = logging.DEBUG)
#2017-06-27 13:38:45,539 - root - CRITICAL - Critical message

#pretty print
#logging.basicConfig(format = u"%(asctime)s - %(levelname)-8s - %(message)s", level = logging.DEBUG)
#2017-06-27 13:43:42,889 - CRITICAL - Critical message


logging.basicConfig(format = u"%(asctime)s - %(levelname)-8s - %(filename)s[LINE:%(lineno)-4d]# %(message)s", level = logging.DEBUG)
#2017-06-27 13:48:23,529 - CRITICAL - log2Console.py[LINE:29  ]# Critical message

#Write to log file
#logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'mylog.log')

logging.debug ("Debug message")
logging.info ("Info message")
logging.warning ("Warning message")
logging.error ("Error message")
logging.critical ("Critical message")


