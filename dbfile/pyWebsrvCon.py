import requests
import pandas as objPnd
import re
import globalstore
from pyDataMgmt import *
from pyLDMeta import *
from pyQuerygen import *
import numpy as np
import socket
from pyMasterDataFrameFunctions import *
from pyChatBotConstants import *
import json
import ast
import sys


	
def webServiceConsumersub(sLabel, substVar):
    globalstore.globalLogger.info('Start')
    try:
        confLabel = GenConflbl(globalstore.globalSessionData['SessionId'],globalstore.globalSessionData['TicketNo'], sLabel, 'WebsrvDefn')
        srootvar = GetRoot(confLabel, substVar)
        webConfs=LoadConfig(confLabel)
        webConfs=dynreplacehirarchystatments(webConfs,substVar,'Parameters')		
        webConf= webConfs[0]
        webConf['Parameters']=subsDynValue(webConf['Parameters'])
        print(webConf['Parameters'])
        if(webConf[SERVICEMETHOD] == GET):
            getResponse = getApiResponse(webConf)		
        dfResponse=objPnd.read_json(getResponse)
        print(dfResponse)
        #print(srootvar)	        
        sAttachPoint=webConf[ATTACHPOINT]
        if srootvar == 'globalstore':
            if (sAttachPoint != ''):
                exec(substVar + '.update({\'' + sAttachPoint + '\':dfResponse.to_dict(orient=\'records\')})')
                SaveGlobal(GetRootGlobal(substVar))
            else:
                exec(substVar + '.update(dfResponse.iloc[0])')
                SaveGlobal(GetRootGlobal(substVar))
        else:
            mbotLoadMetaJson(confLabel,dfResponse,substVar)			

		
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
    globalstore.globalLogger.info('End')

def webServiceConsumersubpost(sLabel, substVar):
    globalstore.globalLogger.info('Start')
    try:
        confLabel = GenConflbl(np.NaN,np.NaN, sLabel, 'WebsrvDefn')
        webConfs=LoadConfig(confLabel)
        webConfs=dynreplacehirarchystatments(webConfs,substVar,'Parameters')		
        webConf= webConfs[0]
        webConf['Parameters']=subsDynValue(webConf['Parameters'])
        #print(webConf)
        dfResponse=objPnd.read_json(postApiResponse(webConf))
        #print(dfResponse)
        sAttachPoint=webConf[ATTACHPOINT]
        if (sAttachPoint != ''):
            exec(substVar + '.update({\'' + sAttachPoint + '\':dfResponse.to_dict(orient=\'records\')})')	
        else:
            exec(substVar + '.update(dfResponse.iloc[0])')
        SaveGlobal(GetRootGlobal(substVar))
		
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
    globalstore.globalLogger.info('End')
	
	
def getApiResponse(apiParams):
    globalstore.globalLogger.info('Start')
    try:
        serviceName = apiParams[SERVICENAME]
        Params = apiParams[PARAMETERS]
        sResource = apiParams['Resource']
        SerResCol = LoadResource({LABEL:sResource}) 
        SerResCol = SerResCol[0]
        #print(SerResCol)		
        serURL = SerResCol['url']+serviceName+'?'+Params
        #print(serURL)
        Result = requests.get(serURL)
        #print(Result.status_code)
        if Result.status_code == 200:
            response = Result.text
        return response
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
    globalstore.globalLogger.info('End')

def postApiResponse(apiParams):
    globalstore.globalLogger.info('Start')
    try:
        serviceName = apiParams[SERVICENAME]
        Params = apiParams[PARAMETERS]
        sResource = apiParams['Resource']
        SerResCol = LoadResource({LABEL:sResource}) 
        SerResCol = SerResCol[0]
        #print(SerResCol)
        serURL = SerResCol[URL]+serviceName
        #print(serURL)
        header = {CONTENTTYPE: SerResCol[CONTENT]}
        Result = requests.post(serURL,data=json.dumps([Params]),headers = header)
        if Result.status_code == 200:
            response = Result.text
        return response
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
    globalstore.globalLogger.info('End')

if __name__ == '__main__':
    globalstore.init()
    ticketNum='T01'
    globalstore.globalSessionData={'SessionId':str(sys.argv[1]),'TicketNo':ticketNum}
    substVar=str(sys.argv[2])
    sLabel = str(sys.argv[3])
    webConfLabel=GenConflbl(str(sys.argv[1]),ticketNum,str(sys.argv[3]),'SerConsumer')
    webServiceConsumer(webConfLabel, substVar)
