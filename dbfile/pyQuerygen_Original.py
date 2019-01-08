import pandas as objPnd
import numpy as np
import globalstore
import pyodbc
from pyMarkTbl import *
from pyDataMgmt import *
from AESCipher import *
import re
from pyMasterDataFrameFunctions import *
from pyChatBotConstants import *

def runQuery(qryLabel,substVars):
    try:
        globalstore.globalLogger.info('Start')
        qryConfLabel=GenConflbl(np.NaN,np.NaN,qryLabel,QUERYGEN)
        qryConf=LoadConfig(qryConfLabel)
        qryConf=dynreplacehirarchystatments(qryConf,substVars,QUERY)
        execQuery(qryConf,True,substVars)
        globalstore.globalLogger.info('End')    
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)

def getResult(sQuery,sdbLabel):
    objDfResult=None
    try:
        globalstore.globalLogger.info('Start')
        ConnCol = LoadResource({LABEL:sdbLabel})
        ConnCol=ConnCol[0]
        sConn=ConnCol[CONNECTIONSTRING]+decryptstrpass(ConnCol[PASSWORD])
        bMalFormed = False
        if(re.search(r"\binsert\b",sQuery,re.IGNORECASE)):
		#if(re.search(r"\bupdate\b",sQuery,re.IGNORECASE) or re.search(r"\binsert\b",sQuery,re.IGNORECASE)):
            bMalFormed = True
        else:
            conn = pyodbc.connect(sConn)            
            try:
                objDfResult=objPnd.read_sql_query(sQuery,conn)
                lResultCol = list(objDfResult.columns.values)
                lFields = [XMLFILE,DATA_STORE_XML,RE_DATA_STORE_XML,DATAXML,BIGXML,PAYMENTDETAILSXML,RULESXML]
                for sFields in lFields:
                    if (sFields in lResultCol):
                        objDfResult[sFields] = objDfResult[sFields].apply(encryptstr)
            except:
                bMalFormed = True
        if(bMalFormed):
            objDFSkeleton=GetDataFrameSkeleton(MALFORMEDQUERY)
            objDfResult = objPnd.DataFrame([sQuery], columns=objDFSkeleton.columns)
        globalstore.globalLogger.info('End')
    except:
        objDfResult=None
        globalstore.globalLogger.error('Exception Information:',exc_info=1)    
    return objDfResult

def subsDynValue(sQuery):
    if not(sQuery is None):
        try:
            globalstore.globalLogger.info('Start')
            globalstore.globalLogger.info(QUERY+': ' + sQuery)
            sevals = re.findall('(<.*?>)', sQuery)
            for j in range(sevals.__len__()):
                seval = sevals[j]
                seval = seval.replace('<', '').replace('>', '')
                sevalval = str(eval(seval))
                sQuery = sQuery.replace(sevals[j], sevalval)
            globalstore.globalLogger.info('End')
        except:
            globalstore.globalLogger.error('Exception Information:',exc_info=1)
            sQuery=sQuery
    return sQuery

def execQuery(qryConf,bRunQry,sAttachpointroot):
    clrLabel=QMOVESWCLR
    try:
        globalstore.globalLogger.info('Start')
        for i in range(qryConf.__len__()):
            bBuildQry=True
            bRunQry=True
            sQuery=qryConf[i][QUERY]
            globalstore.globalLogger.info(QUERY+': ' + sQuery)
            if(RUNQUERY in  qryConf[i]):
                bRunQry=qryConf[i][RUNQUERY]
            try:
                sQuery=subsDynValue(sQuery)
                globalstore.globalLogger.info(QUERY+': ' + sQuery)
            except:
                bBuildQry=False
            qryConf[i][QUERY]=sQuery
            sAttachPoint=qryConf[i][ATTACHPOINT]
            globalstore.globalLogger.info(ATTACHPOINT+': ' + sAttachPoint)
            sdbConn=qryConf[i][DBCONN]
            globalstore.globalLogger.info(CONNECTIONSTRING+': ' + sdbConn)
            if(bBuildQry==True):
                if(bRunQry==True ):
                    dfResult=getResult(sQuery,sdbConn)
                    #dfResult=ColorTbldf(dfResult,clrLabel)
                    dfResult=dfResult.reset_index()
                else:
                    dfResult=pd.DataFrame([sQuery],columns=[sAttachPoint])
                    sAttachPoint=''
                if(dfResult.__len__()>0):
                    if (sAttachPoint != ''):
                        exec(sAttachpointroot + '.update({\'' + sAttachPoint + '\':dfResult.to_dict(orient=\'records\')})')
                    else:
                        exec(sAttachpointroot + '.update(dfResult.iloc[0])')
                    SaveGlobal(GetRootGlobal(sAttachpointroot))
        globalstore.globalLogger.info('End')
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)

def dynreplacehirarchystatments(qryConf,sReplaceHirarchy,sField):
    try:
        globalstore.globalLogger.info('Start')
        for i in range(qryConf.__len__()):
            sreplaceString=sReplaceHirarchy
            for j in range(5):
                sFindStr='$$'+'.'*j+'root'
                globalstore.globalLogger.info('Search String: ' + sFindStr)
                globalstore.globalLogger.info('Replace String: ' + sreplaceString)
                qryConf[i][sField]=qryConf[i][sField].replace(sFindStr,sreplaceString)
                sreplaceStringr=sreplaceString[::-1]
                sposition=sreplaceStringr.find('.')+1
                if(sposition>0):
                    sreplaceString=sreplaceStringr[sposition+1:][::-1]
                else:
                    break
        globalstore.globalLogger.info('End')
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        qryConf=None
    return qryConf
