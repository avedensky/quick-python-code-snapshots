#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

Example of socket
----------------

The program open socket, listen and print message from localhost 9005 port


For check, you can start netcat utility in another console, for example:

netcat localhost 9005 

and you can write and send message through socket


"""

import socket

HOST = 'localhost'
PORT = 9005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))

print 'Ver 4.0'
server.listen(1)
sock, address = server.accept()

print address

try:
   while 1:      
      data = sock.recv(1024)
      print data      
      if str(data).find('q')>=0:
         print 'quit'
         break
      
      sock.send('server answer:hello\n')      
finally:
   server.close()
