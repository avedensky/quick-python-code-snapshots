#!/usr/bin/env python3
#coding: utf-8

"""

Show hostname

"""

from socket import gethostname

print (gethostname())

#Set DEBUG (True/False) depend from hostname, as example
DEBUG = gethostname()=="developer_computer"

