#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import threading

#Some basic sample of Thread

class myThread (threading.Thread):

   def __init__(self, id):
      threading.Thread.__init__(self)
      self.id= id     
      

   def run(self):
      print ("Starting Woker ID: "+str(self.id))
      for i in range (5):
      	print ("Woker ID: "+str(self.id)+" My count: "+str(i))
      	time.sleep(0.5)
      print ("Exiting Woker ID: "+str(self.id))


def main ():
	print ("Start Main Thread")

	#Thread list
	woker_list = []

	#Create and add new thread to list
	for i in range (0,5):		
		woker_list.append (myThread (i))	

	#Run thread
	for woker in woker_list:
		woker.start()

	#Wait finished child process
	for woker in woker_list:		
		woker.join()

	print ("Exiting Main Thread")

if __name__=='__main__' :
	main ()
