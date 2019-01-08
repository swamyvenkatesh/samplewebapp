import pandas as objPnd
from pymongo import MongoClient
from bson import json_util
import globalstore
from pyChatBotConstants import *
from pyMasterDataFrameFunctions import *
from pyChatBotConstants import *
#ServerName = '10.211.205.248'
ServerName = '10.155.141.51'
PortNumber = 27017
database_connection = None
import traceback

def GetMetaColColl():
	globalstore.globalLogger.info('Start')
	objCollection = None
	try:
		objClient = MongoClient(SERVERNAME, PORTNUMBER)
		if not (objClient is None):
			objDB = objClient.bARM
			if not (objDB is None):
				objCollection = objDB.MetaCol
			else:
				objCollection = None
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
		objCollection = None
	globalstore.globalLogger.info('End')
	return objCollection


def GetMetaResultSet():
	globalstore.globalLogger.info('Start')
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
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
		objCollection = None
	globalstore.globalLogger.info('End')
	return objCollection


def GetconfigdataColl():
	globalstore.globalLogger.info('Start')
	objCollection = None
	try:
		objClient = MongoClient(SERVERNAME, PORTNUMBER)
		if not (objClient is None):
			objDB = objClient.bARM
			if not (objDB is None):
				objCollection = objDB.configdata
			else:
				objCollection = None
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
		objCollection = None
	globalstore.globalLogger.info('End')
	return objCollection


def GetresourceColl():
	globalstore.globalLogger.info('Start')
	objCollection = None
	try:
		objClient = MongoClient(SERVERNAME, PORTNUMBER)
		if not (objClient is None):
			objDB = objClient.bARM
			if not (objDB is None):
				objCollection = objDB.resource
		else:
			objCollection = None
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
		objCollection = None
	globalstore.globalLogger.info('End')
	return objCollection

def GenConflbl(SessionId,TicketNo,Label,Type):
	globalstore.globalLogger.info(SESSIONID+': ' + str(SessionId))
	globalstore.globalLogger.info(TICKETNO+': ' +str(TicketNo))
	globalstore.globalLogger.info(LABEL+': ' + str(Label))
	globalstore.globalLogger.info(TYPE+': ' + str(Type))
	return {SESSIONID:SessionId,TICKETNO:TicketNo,LABEL:Label,TYPE:Type}

def GenConf(Label,Type,confVal):
	globalstore.globalLogger.info(LABEL+': ' + Label)
	globalstore.globalLogger.info(TYPE+': ' + Type)
	globalstore.globalLogger.info(CONFVAL+': ' + Type)
	DfSkeleton=GetDataFrameSkeleton(LABELCONFIG)
	return objPnd.DataFrame([[Label,Type,confVal]],columns=DfSkeleton.columns)


def LoadConfig(confMeta):
	globalstore.globalLogger.info('Start')
	objCollection = None
	objMongoDf = None
	objConfig = None
	try:
		globalstore.globalLogger.info(LABEL+': ' + confMeta[LABEL])
		globalstore.globalLogger.info(TYPE+': ' + confMeta[TYPE])
		#print(confMeta)
		#print(globalstore.globalLogger.info(LABEL+': ' + confMeta[LABEL]))
		#print(globalstore.globalLogger.info(TYPE+': ' + confMeta[TYPE]))
		objCollection=GetconfigdataColl()		
		if not (objCollection is None):
			objMongoDf=objPnd.DataFrame(list(objCollection.find({LABEL:confMeta[LABEL],TYPE:confMeta[TYPE]}, {ID: 0})))
			#print(objMongoDf)
			if not (objMongoDf is None):
				objConfig= objMongoDf.iloc[0].Value
		else:
			objConfig = None
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
		objConfig = None
	globalstore.globalLogger.info('End')
	return objConfig

def LoadResource(resourceMeta):
	globalstore.globalLogger.info('Start')
	objCollection = None
	objMongoDf = None
	objConfig = None
	try:
		objCollection=GetresourceColl()
		if not (objCollection is None):
			objMongoDf = objPnd.DataFrame(list(objCollection.find({LABEL:resourceMeta[LABEL]}, {ID: 0})))
			if not (objMongoDf is None):
				objConfig= objMongoDf.iloc[0].Value
		else:
			objConfig = None
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
		objConfig = None
	globalstore.globalLogger.info('End')
	return objConfig

def SaveConfig(itrMeta,confValue):
	globalstore.globalLogger.info('Start')
	objCollection = None
	objMongoDf = None
	objData = None
	try:
		objCollection=GetconfigdataColl()
		if not (objCollection is None):
			objMongoDf=GenConf(itrMeta[LABEL],itrMeta[TYPE],confValue)
			if not (objMongoDf is None):
				objData = json_util.loads(objMongoDf.to_json(orient=RECORDS))
				objCollection.insert(objData)
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
	globalstore.globalLogger.info('End')

def substRootVars(execstr):
	globalstore.globalLogger.info('Start')
	globalstore.globalLogger.info('Input str: '+ execstr)
	for sVar in globalstore.globalList:
		execstr=execstr.replace(sVar,'globalstore.globalList["'+sVar+'"]')
	globalstore.globalLogger.info('Modified str:'+ execstr)
	globalstore.globalLogger.info('End')
	return execstr


def GetRoot(sessionLabel,sRootVar):
	globalstore.globalLogger.info('Start')
	globalstore.globalLogger.info('Input str: '+ sRootVar)
	if not (sRootVar is None):
		sRootVar=sRootVar+'.'
		sRootBaseVar=sRootVar[:sRootVar.find('.')]
	globalstore.globalLogger.info('Modified str:'+ sRootBaseVar)
	globalstore.globalLogger.info('End')
	return sRootBaseVar

def GetRootGlobal(sRootVar):
	globalstore.globalLogger.info('Start')
	globalstore.globalLogger.info('Input str: '+ sRootVar)
	if not (sRootVar is None):
		sRootBaseVar=sRootVar[sRootVar.find('[')+2:sRootVar.find(']')-1]
	globalstore.globalLogger.info('Modified str:'+ sRootBaseVar)
	globalstore.globalLogger.info('End')
	return sRootBaseVar

def LoadRoot(sessionLabel,sRootVar):
	globalstore.globalLogger.info('Start')
	sRootBaseVar=sRootVar
	objCollection = None
	objMongoDf = None
	objRoot = None
	try:
		#globalstore.globalLogger.info('SessionLabel: '+sessionLabel)
		globalstore.globalLogger.info('SRootVar: '+sRootVar)
		objCollection = GetMetaColColl()
		if not (objCollection is None):
			objMongoDf = objPnd.DataFrame(list(objCollection.find({SESSIONID:sessionLabel[SESSIONID],TICKETNO:sessionLabel[TICKETNO],LABEL: sRootBaseVar, TYPE: UDF}, {ID: 0})))
			#objMongoDf = objPnd.DataFrame(list(objCollection.find({LABEL: sRootBaseVar}, {ID: 0})))
			if not (objMongoDf is None):
				objRoot=objMongoDf.iloc[0].Value
				globalstore.globalList[sRootVar]=objRoot
			globalstore.globalRefData[sRootVar]=sessionLabel
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
	globalstore.globalLogger.info('End')
	return objRoot

def SaveMeta(dfMetaVar):
	globalstore.globalLogger.info('Start')
	objCollection = None
	objMetaDefn = None
	objData = None
	statusFlag = False
	try:
		objCollection = GetMetaColColl()
       
		if not (dfMetaVar is None):
			objMetaDefn=dfMetaVar.iloc[0].to_dict()
			if not (objCollection is None):              
				objCollection.delete_many({SESSIONID:objMetaDefn[SESSIONID],TICKETNO:objMetaDefn[TICKETNO],LABEL: objMetaDefn[LABEL]})
				objData = json_util.loads(dfMetaVar.to_json(orient=RECORDS))
				globalstore.globalResponseSavedData[objMetaDefn[LABEL]]=objData
				if(objMetaDefn[TYPE]==UDF):
					globalstore.globalCollectionData[objMetaDefn[LABEL]]=objData
					#dataObjectJson = {"Information":[{'Label':key,"Json":value} for key,value in globalstore.globalResponseSavedData.items()]}
					#data = {'Response':[{'ReturnCode': 0,TICKETNO:objMetaDefn[TICKETNO], 'ChatInformation': None, "DataObjects": dataObjectJson}]}
					#jsonData=json_util.dumps(data, indent=5)
					#globalstore.globalResponseJson=jsonData
				objCollection.insert(objData)
				statusFlag = True
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
		tb = traceback.format_exc()
		errorInfo=str(globalstore.globalCollectionData)+str(tb)
		data = {'Response':[{'ReturnCode': -1, 'ChatInformation': None, 'DataObjects': errorInfo}]}
		jsonData=json_util.dumps(data, indent=5)
		globalstore.globalResponseJson=jsonData
		statusFlag = False
	globalstore.globalLogger.info('End')
	return statusFlag

def SaveMetaWebService(MetaVar):
	globalstore.globalLogger.info('Start')
	objCollection = None
	objMetaDefn = None
	objData = None
	statusFlag = False
	try:
		objCollection = GetMetaColColl()
		
		if not (MetaVar is None):
			#objMetaDefn=dfMetaVar.iloc[0].to_dict()
			if not (objCollection is None):              
				#objCollection.delete_many({SESSIONID:objMetaDefn[SESSIONID],TICKETNO:objMetaDefn[TICKETNO],LABEL: objMetaDefn[LABEL]})
				#objData = json_util.loads(MetaVar)
				#print(MetaVar)
				objCollection.insert(MetaVar)
				statusFlag = True
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
		tb = traceback.format_exc()
		errorInfo=str(globalstore.globalCollectionData)+str(tb)
		data = {'Response':[{'ReturnCode': -1, 'ChatInformation': None, 'DataObjects': errorInfo}]}
		jsonData=json_util.dumps(data, indent=5)
		globalstore.globalResponseJson=jsonData
		statusFlag = False
	globalstore.globalLogger.info('End')
	return statusFlag
    
def isDocumentavailable(dictSearch):
	globalstore.globalLogger.info('Start')
	bFoundVal=True
	objCollection = None
	objMongoDf = None
	try:
		#globalstore.globalLogger.info('Search Parameter: '+dictSearch)
		objCollection = GetMetaColColl()
		if not (objCollection is None):
			objMongoDf = objPnd.DataFrame(list(objCollection.find(dictSearch)))
			if(objMongoDf.empty):
				bFoundVal=False
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
	globalstore.globalLogger.info('End')
	return bFoundVal


def SaveGlobal(sGlobalVar):
	globalstore.globalLogger.info('Start')
	dMetaDef=globalstore.globalRefData[sGlobalVar]
	dfMetaVal=globalstore.globalList[sGlobalVar]
	dfSkeleton=GetDataFrameSkeleton(ITERATORRUN)
	dfMetaData=objPnd.DataFrame([[dMetaDef[SESSIONID],dMetaDef[TICKETNO],sGlobalVar,UDF,dfMetaVal]],columns=dfSkeleton.columns)
	SaveMeta(dfMetaData)
	globalstore.globalLogger.info('End')

def SaveGlobalWebService(sGlobalVar, dfResData):
	globalstore.globalLogger.info('Start')
	dMetaDef=globalstore.globalRefData[sGlobalVar]
	dfMetaVal=globalstore.globalList[sGlobalVar]
	dfSkeleton=GetDataFrameSkeleton(ITERATORRUN)
	dfMetaData=objPnd.DataFrame([[dMetaDef[SESSIONID],dMetaDef[TICKETNO],sGlobalVar,UDF,dfResData]],columns=dfSkeleton.columns)
	#print(dfMetaData)
	SaveMeta(dfMetaData)
	globalstore.globalLogger.info('End')

def SaveResultCollection(MetaLoadConfLabel,ChatInfo):
	globalstore.globalLogger.info('Start')
	objCollection = None
	objMetaDefn = None
	objData = None
	statusFlag = False
	try:
		objCollection = GetMetaResultSet()
		if not (objCollection is None):
			objCollection.delete_many({TICKETNO:MetaLoadConfLabel[TICKETNO], 'ChatInformation':ChatInfo})
			if bool(globalstore.globalResponseSavedData):
				dataObjectJson = {"Information":[{'Label':key,"Json":value} for key,value in globalstore.globalResponseSavedData.items()]}
				data = {'SessionID': MetaLoadConfLabel[SESSIONID], TICKETNO:MetaLoadConfLabel[TICKETNO],'ChatInformation': ChatInfo,'Response':[{'ReturnCode': 0,TICKETNO:MetaLoadConfLabel[TICKETNO], 'ChatInformation': ChatInfo, "DataObjects": dataObjectJson}]}
				jsonData=json_util.dumps(data, indent=5)
				objData = json_util.loads(jsonData)
				objCollection.insert(objData)
				globalstore.globalResponseJson=jsonData
				statusFlag = True
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
		tb = traceback.format_exc()
		dataObjectJson = {"Information":[{'Label':key,"Json":value} for key,value in globalstore.globalResponseSavedData.items()]}
		errorInfo=str(dataObjectJson)+str(tb)
		data = {'SessionID': MetaLoadConfLabel[SESSIONID], TICKETNO:MetaLoadConfLabel[TICKETNO],'ChatInformation': ChatInfo,'Response':[{'ReturnCode': -1,TICKETNO:MetaLoadConfLabel[TICKETNO], 'ChatInformation': ChatInfo, "DataObjects": errorInfo}]}
		jsonData=json_util.dumps(data, indent=5)
		#objCollection.insert(objData)
		globalstore.globalResponseJson=jsonData
		statusFlag = False
	globalstore.globalLogger.info('End')
	return statusFlag

def LoadResultCollection(sessionLabel,sRootVar):
	globalstore.globalLogger.info('Start')
	sRootBaseVar=sRootVar
	objCollection = None
	objMongoDf = None
	objRoot = None
	try:
		#globalstore.globalLogger.info('SessionLabel: '+sessionLabel)
		objCollection = GetMetaResultSet()
		if not (objCollection is None):
			objMongoDf = objPnd.DataFrame(list(objCollection.find({TICKETNO:sessionLabel[TICKETNO],'ChatInformation': sRootBaseVar})))
			if not (objMongoDf.empty):
				objRoot=objMongoDf.iloc[0].Response
	except:
		globalstore.globalLogger.error('Exception Information:',exc_info=1)
	globalstore.globalLogger.info('End')
	return objRoot

def NewLoadResultCollection(variableName):
    globalstore.globalLogger.info('Start')
    sRootBaseVar=variableName
    objCollection = None
    objMongoDf = None
    objRoot = None
    try:
        objCollection = GetMetaResultSet()
        if not (objCollection is None):
            objMongoDf = objPnd.DataFrame(list(objCollection.find({Response_Get: sRootBaseVar})))
            if not (objMongoDf.empty):			
                objRoot=objMongoDf.iloc[0].Response[0]['DataObjects']['Information'][1]
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
    globalstore.globalLogger.info('End')
    return objRoot
