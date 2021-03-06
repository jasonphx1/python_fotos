#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 18:30:24 2018

@author: jason
"""
import sys
import sqlite3
from sqlite3 import Error
import countModule
'''Maturity Considerations: bring in modules called in the called modules.'''
'''Consider using PANDA and pyTest.'''

database = sys.argv[1]
currentDIR = "."

def create_connection(db_file):
    #create connection to database
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None

def iterateItems_fotoDB(conn):
    cur = conn.cursor()
    cur.execute("Select * FROM fotoMeta")
    
    rows = cur.fetchall()
    
    for row in rows:
        print(row)

def main():
    #conn = create_connection(database)
    #with conn:
    #    print("Current items in the foto database:")
    #    iterateItems_fotoDB
    countModule.countFiles(currentDIR)
    print("Done") 

if __name__ == '__main__':
    main()

    
    
