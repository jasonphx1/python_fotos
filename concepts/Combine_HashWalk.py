# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:48:04 2018
YOUTUBE VIDEO = "How to generate the MD5 checksum of a file using python." by PyBear.
@author: jason
"""
__author__ = "Jason Lutz"

import os
import hashlib

fotoPath = '/home/jason/git_repos/python_fotos/concepts'
hasher = hashlib.md5()

for roots, dirs, files in os.walk(fotoPath):
    for file in files:
        f=open(file, "rb")
        content = f.read()
        hasher.update(content)
        print(file + '    ' + hasher.hexdigest())
        #print(hasher.hexdigest())    
    
    
    
    
    
    
#    for filename in files:
 #    content = open_file(file, 'rb')
 #    hasher.update(content)
 #    print(hasher.hexdigest())









#
#for files in os.walk(fotoPath):
#    for file in files:
#        with open(file, 'rb') as open_file:
 #           content = open_file.read()
 #           hasher.update(content)
#        print(hasher.hexdigest())



#   for file in files:
#      print("File = %s:" % file)


