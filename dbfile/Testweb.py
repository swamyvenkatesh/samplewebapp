import requests
import pandas as objPnd
import re
import globalstore
from pyDataMgmt import *
from pyQuerygen import *
import numpy as np
import socket
from pyMasterDataFrameFunctions import *
from pyChatBotConstants import *
import json
import ast
import sys

def webServiceConsumerRoot(sLabel, substVar):
    globalstore.globalLogger.info('Start')
    try:
        confLabel = GenConflbl(np.NaN,np.NaN, sLabel, WEBSRVDEFN)
        webConfs=LoadConfig(confLabel)
        webConfs=dynreplacehirarchystatments(webConfs,substVar,PARAMETERS)		
        webConf= webConfs[0]
        webConf[PARAMETERS]=subsDynValue(webConf[PARAMETERS])
        #print(webConf)
        if(webConf[SERVICEMETHOD] == GET):
            response=getApiResponse(webConf)
        elif(webConf[SERVICEMETHOD] == POST):
            response=postApiResponse(webConf)
        dfResponse=objPnd.read_json(response)
        print(dfResponse)
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
        sResource = apiParams[RESOURCE]
        SerResCol = LoadResource({LABEL:sResource}) 
        SerResCol = SerResCol[0]
        #print(SerResCol)		
        serURL = SerResCol[URL]+serviceName+'?'+Params
        #print(serURL)
        Result = requests.get(serURL)
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
        sResource = apiParams[RESOURCE]
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

