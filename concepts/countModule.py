#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:01:40 2018

@author: jason
"""

import os
import hashlib
import re

hasher = hashlib.md5()


fotoPath = "/home/jason/USB/BackSpace_Labs"

def countFiles(fotoPath):
    totalCount = 0
    txtCount = 0
    jpgCount = 0
    jpegCount = 0
    docCount = 0
    imgCount = 0
    mp4Count = 0
    countDict = {}
    
    for root, dirs, files in os.walk(fotoPath, topdown=False):
        for name in files:
            totalCount += 1
            if re.search('.txt', name):
                txtCount += 1
            if re.search('.jpg', name):
                jpgCount += 1
            if re.search('.jpeg', name):
                jpegCount += 1
            if re.search('.doc', name):
                docCount += 1
            if re.search('.img', name):
                imgCount += 1
            if re.search('.mp4', name):
                mp4Count += 1
    percentTXTFile = txtCount / totalCount
    percentJPGFile = jpgCount / totalCount
    percentJPEGFile = jpegCount / totalCount
    percentDOCFile = docCount / totalCount
    percentIMGFile = imgCount / totalCount
    percentmp4File = mp4Count / totalCount
    print("Total No. of Files: ", totalCount)
    print("Number of text files: ", txtCount, "Percentage: ", percentTXTFile)
    print("Number of jpg files: ", jpgCount, "Percentage: ", percentJPGFile)
    print("Number of jpeg files: ", jpegCount, "Percentage: ", percentJPEGFile)
    print("Number of doc files: ", docCount, "Percentage: ", percentDOCFile)
    print("Number of img files: ", imgCount, "Percentage: ", percentIMGFile)
    print("Number of mp4 files: ", imgCount, "Percentage: ", percentmp4File)
    countDict["totalCount"] = totalCount
    countDict["txtCount"] = txtCount
    countDict["jpgCount"] = jpgCount
    countDict["jpegCount"] = jpegCount
    countDict["docCount"] = docCount
    countDict["imgCount"] = imgCount
    countDict["mp4Count"] = mp4Count
    #print(countDict)
#    for i in countDict:
#        print(countDict[i])
    return countDict
    
def hashFiles(fotoPath):
    for root, dirs, files in os.walk(fotoPath, topdown=False):
        for name in files:
            fullName =os.path.join(root, name)
            f=open(fullName, "rb")
            content = f.read()
            hasher.update(content)
            print(name)
            print(hasher.hexdigest())

def makeDictionary(fotoPath):
    hashDictionary = dict()
    dictCount = 0
    directoryCount = 0
    for root, dirs, files in os.walk(fotoPath, topdown=False):
        for directoy in dirs:
            directoryCount += 1
        for name in files:
            fullName =os.path.join(root, name)
            f=open(fullName, "rb")
            content = f.read()
            hasher.update(content)
            hashValue = hasher.hexdigest()
            hashDictionary[name] = hashValue
    for items in hashDictionary:
        dictCount += 1
    #print("Number of Items in the Dictionary", dictCount)
    #print("Nubmer of Directories", directoryCount)
    return hashDictionary
    
hashDictionary = makeDictionary(fotoPath)
countDict = countFiles(fotoPath)
print(countDict)
print(hashDictionary)
#hashFiles(fotoPath)

