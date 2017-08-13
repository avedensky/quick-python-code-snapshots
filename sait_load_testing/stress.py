#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import time
import threading
import datetime

'''

This program generated many request (GET) to host, uses threads. 
You can config limit of threads.

You can run this program from console as:
python3 ./stress.py 

Basic alternative yandex.tank :)

'''

#Your config

#1 pause from request
WOKER_PAUSE_BETWEEN_REQUEST = 0.01 

# How many request will be send at one woker (thread)
WOKER_HOW_MANY_REQUESTS_SEND = 100 

#How many wokers (threads)
WOKERS_LIMIT = 20 

#You host for testing
HOST = 'http://you_host_here.com'

#-----------


class myThread (threading.Thread):

	def __init__(self, id):
		threading.Thread.__init__(self)
		self.id= id
		self.result_list = []
      
	def run(self):      
		for i in range (WOKER_HOW_MANY_REQUESTS_SEND):      	
			print ("Woker ID: "+str(self.id)+" send request, count: "+str(i))

			start_time = datetime.datetime.utcnow()
			r = requests.get(HOST)      	
			finish_time = datetime.datetime.utcnow()

			delta_time = finish_time - start_time			
			self.result_list.append ([delta_time, self.id, r.status_code])

			time.sleep(WOKER_PAUSE_BETWEEN_REQUEST)     	

	def showMeLog (self):
		for row in self.result_list:
			print ("Delta time: %-10s Woker ID: %5d Response Code: %-5s" % (str(row[0].total_seconds()), row[1], str(row[2])))


def main ():
	print ("--- Start Main Thread ---")
	woker_list = []

	for i in range (0, WOKERS_LIMIT):		
		woker_list.append (myThread (i))	

	#Run thread
	for woker in woker_list:
		woker.start()

	#Wait finished child process
	for woker in woker_list:		
		woker.join()

	#Show log
	print ("----- Log -----")
	print ("Delta time - delta from send and response time")
	print ("Woker ID - id of thread")
	print ("Response code - result of send GET Request")
	print ("")
	for woker in woker_list:		
	 	woker.showMeLog ();

	print ("--- Exiting Main Thread ---")


if __name__=='__main__' :
	main ()