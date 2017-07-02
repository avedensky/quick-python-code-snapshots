#!/bin/python3
#-*- coding: utf-8 -*-

"""

The program create new Data Base (postgresSQL)

"""

#You Config
BD_NAME = "test_bd"
USER = "postgres"
PASSWORD = "postgres"
HOST = "192.168.100.125" #You remote ip or localhost
PORT = "5432"

import psycopg2

connection = psycopg2.connect(user=USER, password=PASSWORD, host=HOST, port=PORT)
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()
cursor.execute("CREATE DATABASE {0};".format(BD_NAME))
cursor.close ()
connection.close()   
   



