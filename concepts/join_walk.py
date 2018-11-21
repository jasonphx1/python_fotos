#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 19:01:40 2018

@author: jason
"""

import os
import hashlib

hasher = hashlib.md5()

for root, dirs, files in os.walk("..", topdown=False):
    #Prints files
    for name in files:
        print(os.path.join(root, name))
        f=open(name, "rb")
        content = f.read()
        hasher.update(content)
        print(hasher.hexdigest())
    #Prints directories
   # for name in dirs:
   #     print(os.path.join(root, name))