import pandas as pd
from pyDataMgmt import *
import globalstore
from pyQuerygen import *
import io
from pyDataMgmt import *
import sys
import re
from pyMasterDataFrameFunctions import *
from pyChatBotConstants import *

def runRule(ruleLabel,substVars):
    globalstore.globalLogger.info('Start')
    statusFlag=False
    try:
        ruleConfdetails=LoadConfig({LABEL:ruleLabel,TYPE:RULES})
        ruleConfdetails = dynreplacehirarchystatments(ruleConfdetails, substVars, RULE)
        ruleConfdetails = dynreplacehirarchystatments(ruleConfdetails, substVars, FIELD)
        ruleConfdetails = dynreplacehirarchystatments(ruleConfdetails, substVars, VALUE)
        bBuildRule=True
        for i in range(ruleConfdetails.__len__()):
            sRule=ruleConfdetails[i][RULE]
            sField = ruleConfdetails[i][FIELD]
            sValue = ruleConfdetails[i][VALUE]
            try:
                sRule=subsDynValue(sRule)
            except:
                bBuildRule=False
            ruleConfdetails[i][RULE]=sRule
            dictrule=eval(sRule)
            dictrule[SESSIONID]=globalstore.globalSessionData[SESSIONID]
            dictrule[TICKETNO] = globalstore.globalSessionData[TICKETNO]
            dictrule[LABEL] = GetRootGlobal(substVars)
            dictrule[TYPE] = UDF
            globalstore.globalLogger.info(SESSIONID+': ' + globalstore.globalSessionData[SESSIONID])
            globalstore.globalLogger.info(TICKETNO+': ' +globalstore.globalSessionData[TICKETNO])
            globalstore.globalLogger.info(RULE+': ' + sRule)
            globalstore.globalLogger.info(FIELD+': ' + sField)
            globalstore.globalLogger.info(VALUE+': ' + sValue)
            try:
                if(isDocumentavailable(dictrule)):
                    exec(sField+'='+"'"+sValue+",'")
            except:
                exec(sField + '=' + "'MalFormed Rule: " + sRule + ",'")
        SaveGlobal(GetRootGlobal(substVars))
        statusFlag=True        
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        statusFlag=False
    globalstore.globalLogger.info('End')
    return statusFlag

def clearRuleRes(ruleLabel,substVars):
    globalstore.globalLogger.info('Start')
    statusFlag=False
    try:
        ruleConfdetails=LoadConfig({LABEL:ruleLabel,TYPE:RULES})
        ruleConfdetails = dynreplacehirarchystatments(ruleConfdetails, substVars, RULE)
        ruleConfdetails = dynreplacehirarchystatments(ruleConfdetails, substVars, FIELD)
        bBuildRule=True
        for i in range(ruleConfdetails.__len__()):
            sRule=ruleConfdetails[i][RULE]
            sField = ruleConfdetails[i][FIELD]
            sValue = ruleConfdetails[i][VALUE]
            globalstore.globalLogger.info(RULE+': ' + sRule)
            globalstore.globalLogger.info(FIELD+': ' + sField)
            globalstore.globalLogger.info(VALUE+': ' + sValue)
            exec(sField+'='+"''")
        SaveGlobal(GetRootGlobal(substVars))        
        statusFlag=True
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        statusFlag=False
    globalstore.globalLogger.info('End')
    return statusFlag
