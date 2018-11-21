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
docCount = 0

for root, dirs, files in os.walk(".", topdown=False):
    #Prints files
    for name in files:
        fullName =os.path.join(root, name)
        f=open(fullName, "rb")
        content = f.read()
        hasher.update(content)
        print(hasher.hexdigest())
        if re.search('.txt', name):
            txtCount += 1
print("Number of text files: ", txtCount)
    #Prints directories
   # for name in dirs:
   #     print(os.path.join(root, name))
