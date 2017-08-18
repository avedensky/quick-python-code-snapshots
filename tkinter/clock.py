#!/usr/bin/env python3
#coding: utf-8

"""
	Clock, GUI python example. 
	
	This code depend from tkinter. 

	For installation tkinter:
	sudo apt-get install python3-tk

"""

import tkinter
import time

curtime = ''
clock = tkinter.Label()
clock.pack()

def tick():
    global curtime
    newtime = time.strftime('%H:%M:%S')
    if newtime != curtime:
        curtime = newtime
        clock.config(text=curtime)
    clock.after(200, tick)

tick()
clock.mainloop()