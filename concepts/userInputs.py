# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 11:49:02 2018

@author: jason
"""

defaultDB = "database.db"

def initialInput(defaultDB):
    print("For all inputs used ABSOLUTE PATHS")
    srcDir=input("The directory of the new fotos:")
    print("Checking source directory:", srcDir)
    #Call checkDir(srcDir):
    dstDB=input("The database: [ENTER for default]:")
    print("Checking database connection/exists, for database:", defaultDB)
    #Call checkDB(dstDB)

def checkDir(dir):  #Used to check if any directories exist
    print(dir)

def checkDB(db):
    print(db)
    

initialInput(defaultDB)
