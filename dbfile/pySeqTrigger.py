# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 14:39:10 2018

@author: 427516
"""

from pyDataMgmt import *

SessionId = str(sys.argv[1])
ActionName = str(sys.argv[2])
DynamicParam = str(sys.argv[2])


result = LoadDefaultConfig(ActionName,SessionId,DynamicParam)
_newArr = result.replace(',',' ')

#import os 
#os.system('python pySeq.py ' + _newArr)

import subprocess
subprocess.call("python pySeq.py " + _newArr, shell=True)
