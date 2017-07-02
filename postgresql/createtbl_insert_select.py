#!/bin/python3
#-*- coding: utf-8 -*-

"""

The program create tables, insert some data, and show to console
For connect to postgresSQL used psycopg2
(sudo pip3 install psycopg2)

"""

#You Config
BD_NAME = "test_bd"
USER = "postgres"
PASSWORD = "postgres"
HOST = "192.168.100.125" #You remote ip or localhost
PORT = "5432"

import psycopg2

connection = psycopg2.connect(dbname = BD_NAME, user = USER, password=PASSWORD, host=HOST, port=PORT)
connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
cursor = connection.cursor()

#Create Table
cursor.execute("CREATE TABLE star (id int, star_name varchar(10));")

#Insert Data
cursor.execute("INSERT INTO star (id, star_name ) VALUES (1, 'Sun');")
cursor.execute("INSERT INTO star (id, star_name ) VALUES (2, 'Capella');")

#Show Data
cursor.execute("SELECT * FROM star;")
for row in cursor:
        print ("%-3s %s" % (row[0], row[1]))
        print ("-----------------------------------------------------------------------------")

cursor.close()
connection.close()   