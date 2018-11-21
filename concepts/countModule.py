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


fotoPath = "/vm_hosts/Sample_Data"

def countFiles(fotoPath):
    totalCount = 0
    txtCount = 0
    jpgCount = 0
    jpegCount = 0
    docCount = 0
    imgCount = 0
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
    percentTXTFile = txtCount / totalCount
    percentJPGFile = jpgCount / totalCount
    percentJPEGFile = jpegCount / totalCount
    percentDOCFile = docCount / totalCount
    percentIMGFile = imgCount / totalCount
    print("Total No. of Files: ", totalCount)
    print("Number of text files: ", txtCount, "Percentage: ", percentTXTFile)
    print("Number of jpg files: ", jpgCount, "Percentage: ", percentJPGFile)
    print("Number of jpeg files: ", jpegCount, "Percentage: ", percentJPEGFile)
    print("Number of doc files: ", docCount, "Percentage: ", percentDOCFile)
    print("Number of img files: ", imgCount, "Percentage: ", percentIMGFile)

countFiles(fotoPath)

