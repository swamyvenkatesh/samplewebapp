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

def healthchecks(hlthConf,substVars,bExtendedCheck):
    globalstore.globalLogger.info('Start')
    bStatusFlag=False
    try:
        if not (hlthConf is None):
            hlthLabel=hlthConf[CHECKOBJECT]
            bStatusAggregate = True
            iSuccessAggregate = 0
            hlthConfLabel = GenConflbl(np.NaN, np.NaN, hlthLabel, HEALTHCHK)
            hlthConf = LoadConfig(hlthConfLabel)
            sColorCode_Tag=GREEN_CODE
            dfSkeletonDF=GetDataFrameSkeleton(HEALTHCHECKRESULT)
            dfResponses = objPnd.DataFrame(columns=dfSkeletonDF.columns)
            for i in range(hlthConf.__len__()):
                sCheckType = hlthConf[i][CHECKTYPE]
                sLevel = hlthConf[i][LEVEL]
                globalstore.globalLogger.info(CHECKTYPE+': ' + sCheckType)
                globalstore.globalLogger.info(LEVEL+': ' + sLevel)
                if(bExtendedCheck == False and sLevel==EXTENDED):
                    continue
                if sCheckType == CHECKURL:
                    dfResponse = checkurlhttp(hlthConf[i],substVars)                    
                    globalstore.globalLogger.info('URL Response: ' + json.dumps(dfResponse))
                elif sCheckType == CHECKSQL:
                    dfResponse = checkdB(hlthConf[i], substVars)
                    globalstore.globalLogger.info('SQL Response: ' + json.dumps(dfResponse))
                elif sCheckType == CHECKPORT:
                    dfResponse = checkPort(hlthConf[i], substVars)
                    globalstore.globalLogger.info('Port Response: ' + json.dumps(dfResponse))
                elif sCheckType == CHECKWEBREQ:                   
                    dfResponse = checkurlPost(hlthConf[i], substVars)
                    globalstore.globalLogger.info('Web Request: ' + json.dumps(dfResponse))
                bStatusAggregate = bStatusAggregate and dfResponse[BSTATUS]
                if(dfResponse[BSTATUS]):
                    iSuccessAggregate=iSuccessAggregate+1
                else:
                    sColorCode_Tag = LIGHT_ORANGE
                dfResponses = dfResponses.append(dfResponse, ignore_index=True)
            exec(substVars + '.update({\'Results\':dfResponses.to_dict(orient=\'records\')})')
            dfAggregate = {COLORCODE_TAG:sColorCode_Tag,'Total':hlthConf.__len__(),'Success':iSuccessAggregate}
            exec(substVars + '.update(dfAggregate)')
            SaveGlobal(GetRootGlobal(substVars))
            bStatusFlag= True
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        bStatusFlag=False
    globalstore.globalLogger.info('End')
    return bStatusFlag

def checkurlPost(dUrlPostConf,substVars):
    globalstore.globalLogger.info('Start')    
    sDescription=dUrlPostConf[CHECKDESCRIPTION]
    sUrl=dUrlPostConf[URL]
    dPostVars = ''
    if(len(dUrlPostConf[POST_VARS])>1):
        dPostVars = eval(dUrlPostConf[POST_VARS])    
        
    sText=dUrlPostConf[VALIDATETEXT]
    globalstore.globalLogger.info(POST_VARS+': ' + dPostVars)
    globalstore.globalLogger.info(CHECKDESCRIPTION+': ' + sDescription)
    globalstore.globalLogger.info(URL+': ' + sUrl)
    globalstore.globalLogger.info(VALIDATETEXT+': ' + sText)
    dStatus={INTERFACE:sDescription,DETAIL:sUrl,RESULT:FAILED,COLORCODE_TAG:LIGHT_ORANGE,BSTATUS:False}
    try:
        siteresult = requests.post(sUrl,dPostVars)
        if siteresult.status_code == 200:
            if(re.search(sText,siteresult.text)):
                dStatus[RESULT] = SUCCESS
                dStatus[COLORCODE_TAG] = GREEN_CODE
                dStatus[BSTATUS] = True
    except :
        dStatus[RESULT] = FAILED
    globalstore.globalLogger.info('End')
    return dStatus

def checkurlhttp(dUrlConf,substVars):
    globalstore.globalLogger.info('Start')    
    sDescription=dUrlConf[CHECKDESCRIPTION]
    sUrl=dUrlConf[URL]
    sText=dUrlConf[VALIDATETEXT]
    globalstore.globalLogger.info(CHECKDESCRIPTION+': ' + sDescription)
    globalstore.globalLogger.info(URL+': ' + sUrl)
    globalstore.globalLogger.info(VALIDATETEXT+': ' + sText)
    dStatus={INTERFACE:sDescription,DETAIL:sUrl,RESULT:FAILED,COLORCODE_TAG:LIGHT_ORANGE,BSTATUS:False}
    try:
        siteresult = requests.get(sUrl)
        if siteresult.status_code == 200:
            if(re.search(sText,siteresult.text)):
                dStatus[RESULT] = SUCCESS
                dStatus[COLORCODE_TAG] = GREEN_CODE
                dStatus[BSTATUS] = True
    except :
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        dStatus[RESULT] = FAILED
    globalstore.globalLogger.info('End')
    return dStatus

def checkdB(dSqlConf,substVars):
    globalstore.globalLogger.info('Start')
    sDescription=dSqlConf[CHECKDESCRIPTION]
    sdb=dSqlConf[DB]
    sQuery=dSqlConf[VALIDATSQL]
    globalstore.globalLogger.info(CHECKDESCRIPTION+': ' + sDescription)
    globalstore.globalLogger.info(DB+': ' + sdb)
    globalstore.globalLogger.info(VALIDATSQL+': ' + sQuery)
    dStatus={INTERFACE:sDescription,DETAIL:sdb,RESULT:FAILED,COLORCODE_TAG:LIGHT_ORANGE,BSTATUS:False}
    try:
        siteresult = getResult(sQuery,sdb)
        if (siteresult.empty == False):
            dStatus[RESULT] = SUCCESS
            dStatus[COLORCODE_TAG] = GREEN_CODE
            dStatus[BSTATUS] = True
    except :
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        dStatus[RESULT] = FAILED
    globalstore.globalLogger.info('End')
    return dStatus

def checkPort(dSqlConf,substVars):
    globalstore.globalLogger.info('Start')
    sDescription=dSqlConf[CHECKDESCRIPTION]
    sServer=dSqlConf[SERVER]
    sPort = dSqlConf[SPORT]
    globalstore.globalLogger.info(CHECKDESCRIPTION+': ' + sDescription)
    globalstore.globalLogger.info(SERVER+': ' + sServer)
    globalstore.globalLogger.info(SPORT+': ' + str(sPort))
    dStatus = {INTERFACE: sDescription, DETAIL: sServer, RESULT: FAILED, COLORCODE_TAG: LIGHT_ORANGE,
               BSTATUS: False}
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        siteresult = sock.connect_ex((sServer, sPort))
        if siteresult == 0:
            dStatus[RESULT] = SUCCESS
            dStatus[COLORCODE_TAG] = GREEN_CODE
            dStatus[BSTATUS] = True
    except :
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        dStatus[RESULT] = FAILED
    globalstore.globalLogger.info('End')
    return dStatus
