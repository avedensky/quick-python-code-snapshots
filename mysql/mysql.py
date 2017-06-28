#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb

if note !="":    
    db = MySQLdb.connect(host="localhost", user="USERNAME", passwd="PASSWORD",db="DATABASENAME")
 
    cur2 = db.cursor()
    if name:
        cur2.execute("INSERT INTO note (note, name) VALUES (%s, %s)", (note, name))
    else:
        cur2.execute("INSERT INTO note (note) VALUES (%s)", (note))
