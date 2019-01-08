# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 12:33:36 2018

@author: 427516
"""
from pymongo import MongoClient
import pandas as objPnd
SERVERNAME = '10.155.141.51'
PORTNUMBER = 27017

objCollection = None
try:
	objClient = MongoClient(SERVERNAME, PORTNUMBER)
	if not (objClient is None):
		objDB = objClient.bARM
		if not (objDB is None):
			objCollection = objDB.ResponseResult
		else:
			objCollection = None
except:	
	objCollection = None

objMongoDf = objPnd.DataFrame(list(objCollection.find({'Response.DataObjects.Information.Label':'varqmove'})))
objRoot=objMongoDf.iloc[0].Response[0]['DataObjects']['Information'][1]['Json']
from bson.json_util import dumps
jsonData=dumps(objRoot,indent=5)
print(jsonData)

#import pandas as objPnd
#objMongoDf = None
#objRoot = None
#if not (objCollection is None):
#	objMongoDf = objPnd.DataFrame(list(objCollection.find({'TicketNo':'T01','ChatInformation': 'Sequence'})))
#	if not (objMongoDf.empty):
#		objRoot=objMongoDf.iloc[0].Response
#
#objMongoDf = objPnd.DataFrame(list(objCollection.find({'Response.DataObjects.Information.Label':'varqmove'})))
#objRoot=objMongoDf.iloc[0].Response[0]['DataObjects']['Information'][1]['Json']
#
#objr = objRoot[0]['Value'][0]
#
#
#for k in objr.keys():
#    print('First: ' + str(type(objr[k])))
#    if type(objr[k]) == list:
#        for i in objr[k]:
#            if type(i) == dict:
#                for nk in i.keys():
#                    if(nk == 'XMLFile'):
#                        i.pop(nk, None)
#                        break
#
#types1 = [type(k) for k in objr.keys()]
#
#from bson.json_util import dumps
#jsonData=dumps(objRoot,indent=5)
#
#import json
#FileName = 'var' + 'output.json'
#with open(FileName, 'w') as outfile:
#    dumps(objRoot,indent=5)
