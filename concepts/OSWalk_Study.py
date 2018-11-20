# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 12:03:53 2018
YouTube Title = Python 13 - Directories and OS Walk by VoidRealms
@author: jason
"""

__author__ = "Jason Lutz"

import os

spath = r"/home/jason/git_hub_repos/Spyder3_Workspace"

print(os.listdir(spath))

#Examplel of "get everything split"

#   for dir in dirs:
#        print("Directory = %s:" % dir)
#   for file in files:
#      print("File = %s:" % file)

#Only the roots
roots = next(os.walk(spath))[0]
print("Roots = %s" % roots)

#Only the dirs
dirs = next(os.walk(spath))[1]
print("Directories = %s" % dirs)

#Only the files
files = next(os.walk(spath))[2]
print("Files = %s" % files)



        