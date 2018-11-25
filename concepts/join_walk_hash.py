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
txtCount = 0
jpgCount = 0
jpegCount = 0
docCount = 0
imgCount = 0
otherCount = o

for root, dirs, files in os.walk("/vm_hosts/Sample_Data", topdown=False):
    #Prints files
    for name in files:
#        fullName =os.path.join(root, name)
 #       f=open(fullName, "rb")
#        content = f.read()
#        hasher.update(content)
#        print(hasher.hexdigest())
        if re.search('.txt', name):
            txtCount += 1
        elif re.search('.jpg', name):
            jpgCount += 1
        elif re.search('.jpeg', name):
            jpegCount += 1
        elif re.search('.doc', name):
            docCount += 1
        elif re.search('.img', name):
            imgCount += 1
        else
print("Number of text files: ", txtCount)
print("Number of jpg files: ", jpgCount)
print("Number of jpeg files: ", jpegCount)
print("Number of doc files: ", docCount)
print("Number of img files: ", imgCount)
    #Prints directories
   # for name in dirs:
   #     print(os.path.join(root, name))
