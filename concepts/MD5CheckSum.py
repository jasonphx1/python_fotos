# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:48:04 2018
YOUTUBE VIDEO = "How to generate the MD5 checksum of a file using python." by PyBear.
@author: jason
"""
__author__ = "Jason Lutz"

import hashlib

filename = '/home/jason/git_hub_repos/python_fotos/concepts/deleteme.txt'

hasher = hashlib.md5()

#Open and read file to hash

with open(filename, 'rb') as open_file:
    content = open_file.read()
    hasher.update(content)
print(hasher.hexdigest())




