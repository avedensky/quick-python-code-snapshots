#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Working with string

Formated output
"""


print ('*** split string in cvs format***');

str = "green,red,blues,orange,black,white,grey"

mylist = [tmp for tmp in str.split (",")]

print ("String:",str)
print ("List of part this string:")
for value in mylist:
	print (value)

print ("")	
print ("*** String alignment ***")
a = "just a test line"
print ("Left",a.center (30),"Right")
print ("Left",a.rjust (30),"Right")
print ("Left",a.ljust (30),"Right")

print ("")
print ("*** String formated ***")
b = 1
c = 'one'
d = 38.5672
print ("Format: %d, %s, %0.2f" % (b, c, d))
