# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 19:13:38 2019

@author: salba
"""

import os
import shutil
from send2trash import send2trash

os.chdir(os.pardir)
for item in os.scandir(os.curdir):
    if item.is_file() and item.name != 'cleaner.py':
        try:
            name, exten = os.path.splitext(item.name)
            #does a fancy trick to tokenize the file name and take the last two items. 
            #if there are not two to take, exception thrown; if there are, take the second one, which is the file extension
            
            if not os.path.isdir(exten):
                os.mkdir(exten)
            shutil.copy(item.name, exten)
            send2trash(item.name)
            
        except IndexError:
            send2trash(item.name)


            
            
    
    