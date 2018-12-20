#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 21:33:17 2018

@author: jason
"""

#Define the relative path of the DB
sqlite_file = './music.sqlite3'

#Create connection to slqDB and setup cursor
import sqlite3
conn = sqlite3.connect(sqlite_file)
sqlCursor = conn.cursor()

#Show all tables
sqlCursor.execute("SELECT name FROM sqlite_master WHERE type='table';" )
print("The following tables exist:")
print(sqlCursor.fetchall())

#Show items in the table (Later do iterations)
sqlCursor.execute("SELECT * FROM  Tracks")
rows = sqlCursor.fetchall()

print("These are the tracks available:")
for row in rows:
    print("Track:")
    print(row)
#close out cursor and connection
sqlCursor.close()
conn.close()
