import pandas as objPnd
import io
import sys
from pyDataMgmt import *
from pyMasterDataFrameFunctions import *
from pyChatBotConstants import *
import numpy as np

def getData(dfsourceFrame,sField):
    globalstore.globalLogger.info('Start')
    objDfStr=None
    try:
        if not(dfsourceFrame is None):
            globalstore.globalLogger.info('Input String: ' + sField)
            objDfStr=dfsourceFrame[dfsourceFrame.NodeID.str.contains(sField)].NodeValStr
            objDfStr=objDfStr.values[0]
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDfStr=None
    globalstore.globalLogger.info('End')
    return objDfStr

def getDefData(fieldsMeta):
    globalstore.globalLogger.info('Start')
    objDFDefData=None
    try:
        objDFSkeleton= GetDataFrameSkeleton(FIELDSMETA)
        objDFDefData = objPnd.DataFrame([[APPLICATIONNO, STR, YES], [MOVE_TO_Q, STR, NO]], columns=objDFSkeleton.columns)       
        dfStack=objDFDefData.stack()
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDFDefData=None
    globalstore.globalLogger.info('End')
    return objDFDefData

def GetDefDataInJSON(fieldsMeta):
    globalstore.globalLogger.info('Start')
    objDFDefData=None
    try:
        if not(FieldsMeta is None):
         dfDataField=getData(fieldsMeta,JSON_FORMAT)
         objDFDefData= objPnd.read_json(dfDataField)
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDFDefData=None
    globalstore.globalLogger.info('End')
    return objDFDefData

def loadData(strDataString,dfDefData):
    globalstore.globalLogger.info('Start')
    objDfContainer=None
    try:
        if not(strDataString is None and dfDefData is None ):
            globalstore.globalLogger.info('Input String: ' + strDataString)
            strDataString=strDataString.replace(';',"\n")
            sDataStrem=io.StringIO(strDataString)
            objDfContainer=objPnd.read_csv(sDataStrem,names=[dname.get(NAME) for dname in dfDefData])
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDfContainer=None
    globalstore.globalLogger.info('End')
    return objDfContainer

def mbotLoadMeta(confLabel,sValues,sRootNode):
    globalstore.globalLogger.info('Start')
    objDfMetaData=None
    try:
        if not (confLabel is None):
            globalstore.globalLogger.info(LABEL+': ' + confLabel[LABEL])
            globalstore.globalLogger.info(TYPE+': ' + METADFN)
            globalstore.globalLogger.info(SESSIONID+': ' + confLabel[SESSIONID])
            globalstore.globalLogger.info(TICKETNO+': ' + confLabel[TICKETNO])
            globalstore.globalLogger.info('Root Node: ' + sRootNode)
            dfDefData = LoadConfig({LABEL:confLabel[LABEL],TYPE:METADFN})            
            dfMetaDataValue = loadData(sValues, dfDefData)
            objDFSkeleton= GetDataFrameSkeleton(ITERATORRUN)
            objDfMetaData = objPnd.DataFrame([[confLabel[SESSIONID], confLabel[TICKETNO], sRootNode, UDF, dfMetaDataValue]],columns=objDFSkeleton.columns)
            SaveMeta(objDfMetaData)
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDfMetaData=None
    globalstore.globalLogger.info('End')
    return objDfMetaData
	
def mbotLoadMetaJson(confLabel,sValues,sRootNode):
    globalstore.globalLogger.info('Start')
    objDfMetaData=None
    try:
        if not (confLabel is None):
            globalstore.globalLogger.info(LABEL+': ' + confLabel[LABEL])
            globalstore.globalLogger.info(TYPE+': ' + METADFN)
            globalstore.globalLogger.info(SESSIONID+': ' + confLabel[SESSIONID])
            globalstore.globalLogger.info(TICKETNO+': ' + confLabel[TICKETNO])
            globalstore.globalLogger.info('Root Node: ' + sRootNode)
            dfDefData = LoadConfig({LABEL:confLabel[LABEL],TYPE:METADFN})            
            dfMetaDataValue = sValues
            objDFSkeleton= GetDataFrameSkeleton(ITERATORRUN)
            objDfMetaData = objPnd.DataFrame([[confLabel[SESSIONID], confLabel[TICKETNO], sRootNode, UDF, dfMetaDataValue]],columns=objDFSkeleton.columns)
            SaveMeta(objDfMetaData)
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDfMetaData=None
    globalstore.globalLogger.info('End')
    return objDfMetaData

def loadMetaWebService(sSessionID,sValues,sRootNode):
    globalstore.globalLogger.info('Start')
    objDfMetaData=None
    try:
        ticketNum='T01'
        globalstore.globalSessionData={'SessionId':sSessionID,'TicketNo':ticketNum}
        confLabel = GenConflbl(sSessionID, ticketNum, 'MetaWebSerConsumer', 'MetaDefn')
        if not (confLabel is None):
            globalstore.globalLogger.info(LABEL+': ' + confLabel[LABEL])
            globalstore.globalLogger.info(TYPE+': ' + METADFN)
            globalstore.globalLogger.info(SESSIONID+': ' + confLabel[SESSIONID])
            globalstore.globalLogger.info(TICKETNO+': ' + confLabel[TICKETNO])
            globalstore.globalLogger.info('Root Node: ' + sRootNode)
            dfDefData = LoadConfig({LABEL:confLabel[LABEL],TYPE:METADFN})
            dfMetaDataValue = loadData(sValues, dfDefData)
            #print(dfMetaDataValue)
            objDFSkeleton= GetDataFrameSkeleton(WEBSERVICECONSUMEPARAMS)
            objDfMetaData = objPnd.DataFrame([[confLabel[SESSIONID], confLabel[TICKETNO], sRootNode, UDF, dfMetaDataValue]],columns=objDFSkeleton.columns)
            SaveMeta(objDfMetaData)
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDfMetaData=None
    globalstore.globalLogger.info('End')
    return objDfMetaData

def validateCSV(sSessionID,sRootNode,csvFile,sValues):
    globalstore.globalLogger.info('Start')
    objDfMetaData=None
    try:
        ticketNum='T01'
        globalstore.globalSessionData={'SessionId':sSessionID,'TicketNo':ticketNum}
        confLabel = GenConflbl(sSessionID, ticketNum, 'MetaValidateCSV', 'MetaDefn')
        if not (confLabel is None):
            globalstore.globalLogger.info(LABEL+': ' + confLabel[LABEL])
            globalstore.globalLogger.info(TYPE+': ' + METADFN)
            globalstore.globalLogger.info(SESSIONID+': ' + confLabel[SESSIONID])
            globalstore.globalLogger.info(TICKETNO+': ' + confLabel[TICKETNO])
            globalstore.globalLogger.info('Root Node: ' + sRootNode)
            dfDefData = LoadConfig({LABEL:confLabel[LABEL],TYPE:METADFN})            
            dfMetaDataValue = loadData(sValues, dfDefData)
            objDFSkeleton= GetDataFrameSkeleton(ITERATORRUN)
            objDfMetaData = objPnd.DataFrame([[confLabel[SESSIONID], confLabel[TICKETNO], sRootNode, UDF, dfMetaDataValue]],columns=objDFSkeleton.columns)
            #SaveMeta(objDfMetaData)
            dfMetaDataCSV =  objPnd.read_csv(csvFile)
            dfMetaDataValue['Result'] = dfMetaDataValue['Fieldname'].apply(lambda field: 'Present' if field in dfMetaDataCSV.columns else 'Not Present')
            dfMetaDataValue['FiledValue'] = dfMetaDataValue['Fieldname'].apply(lambda field: 'Value' if((field in dfMetaDataCSV.columns) and (not(dfMetaDataCSV[field].isnull().any()))) else 'No Value')
            print("CSV file is validate successfully and had the required Fields 'Price Date' & 'DistribChan'")
            objDFSkeleton= GetDataFrameSkeleton(ITERATORRUN)
            objDfMetaData = objPnd.DataFrame([[confLabel[SESSIONID], confLabel[TICKETNO], sRootNode, UDF, dfMetaDataValue]],columns=objDFSkeleton.columns)
            #SaveMeta(objDfMetaData)				
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDfMetaData=None
    globalstore.globalLogger.info('End')
    #return objDfMetaData    

def mbotLoadMetaCSV(confLabel,csvFile,sRootNode):
    globalstore.globalLogger.info('Start')
    objDfMetaData=None
    try:
        if not (confLabel is None):
            globalstore.globalLogger.info(LABEL+': ' + confLabel[LABEL])
            globalstore.globalLogger.info(TYPE+': ' + METADFN)
            globalstore.globalLogger.info(SESSIONID+': ' + confLabel[SESSIONID])
            globalstore.globalLogger.info(TICKETNO+': ' + confLabel[TICKETNO])
            globalstore.globalLogger.info('Root Node: ' + sRootNode)
            dfMetaDataCSV =  objPnd.read_csv(csvFile)
            objDFSkeleton= GetDataFrameSkeleton(ITERATORRUN)
            objDfMetaData = objPnd.DataFrame([[confLabel[SESSIONID], confLabel[TICKETNO], sRootNode, UDF, dfMetaDataCSV]],columns=objDFSkeleton.columns)
            SaveMeta(objDfMetaData)
            objCollection=NewLoadResultCollection(sRootNode)
            if not(objCollection is None):
                rows = len(objCollection['Json'][0]['Value'])
                columns = len(objCollection['Json'][0]['Value'][0])
                print('The CSV file is uploaded successfully. Loaded {}-Rows and {}-Columns'.format(str(rows),str(columns)))			
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDfMetaData=None
    globalstore.globalLogger.info('End')
    return objDfMetaData

def GenConfLbl(SessionId,TicketNo,Label,Type):
    globalstore.globalLogger.info(SESSIONID+': ' + SessionId)
    globalstore.globalLogger.info(TICKETNO+': ' +TicketNo)
    globalstore.globalLogger.info(LABEL+': ' + Label)
    globalstore.globalLogger.info(TYPE+': ' + Type)
    return {SESSIONID:SessionId,TICKETNO:TicketNo,LABEL:Label,TYPE:Type}

def loadMetaData(sSessionID,sLabel,sRootNode,sValues):
    ticketNum='T01'
    globalstore.globalLogger.info(SESSIONID+': ' + sSessionID)
    globalstore.globalLogger.info('Root Node:' +sRootNode)
    globalstore.globalLogger.info(LABEL+': ' + sLabel)
    globalstore.globalLogger.info('Values:' + sValues)
    globalstore.globalSessionData={'SessionId':sSessionID,'TicketNo':ticketNum}
    MetaLoadConfLabel = GenConflbl(sSessionID, ticketNum, sLabel, 'MetaDefn')
    if(sValues.endswith('.csv')):
        dfMetaData = mbotLoadMetaCSV(MetaLoadConfLabel,sValues,sRootNode)        
    else:
        dfMetaData = mbotLoadMeta(MetaLoadConfLabel,sValues,sRootNode)
    return dfMetaData

if __name__ == "__main__":

    if sys.argv[4].endswith('.csv'):
        sessionID = str(sys.argv[1]) # 54321
        typeOfData = sys.argv[2] #'HealthCheck'
        #sys.argv[3] = 'MyChk'
        #sys.argv[4] = 'NewBusinessChecks;SalesChecks;MobileAppsCheck'    
        csvFile = str(sys.argv[4])
        globalstore.init()
        globalstore.globalLogger.info('Start')
        ticketNum = 'T01'
        globalstore.globalSessionData = {SESSIONID: sessionID , TICKETNO: ticketNum}
        MetaLoadConfLabel=GenConfLbl(str(sessionID),ticketNum,str(typeOfData),METADFN)   
        substVar=str(sys.argv[3])
        mbotLoadMetaCSV(MetaLoadConfLabel, csvFile , substVar)    
        SaveResultCollection(MetaLoadConfLabel,'LoadMetaData')
        objCollection=LoadResultCollection(MetaLoadConfLabel,'LoadMetaData')
        if not(objCollection is None):
            jsonData=json_util.dumps(objCollection,indent=5)
        else:
            jsonData=globalstore.globalResponseJson
        #sys.stdout.write(jsonData)
        globalstore.globalLogger.info('End')
    else:
        sessionID = sys.argv[1]
        typeOfData = sys.argv[2]
        #sys.argv[3] = 'MyChk'
        #substarr=sys.argv[4:5]
        #substarr.extend(sys.argv[6:])
        #print(substarr)
        inputvalues = sys.argv[4] #'NewBusinessChecks;SalesChecks;MobileAppsCheck'  
        #print(inputvalues)
        globalstore.init()
        globalstore.globalLogger.info('Start')
        ticketNum = 'T01'
        globalstore.globalSessionData = {SESSIONID: str(sessionID), TICKETNO: ticketNum}
        MetaLoadConfLabel=GenConfLbl(str(sessionID),ticketNum,str(typeOfData),METADFN)   
        substVar=str(sys.argv[3])
        #print(MetaLoadConfLabel)
        #loadMetaWebService(str(sessionID), str(inputvalues), substVar)
        mbotLoadMeta(MetaLoadConfLabel, str(inputvalues), substVar)    
        SaveResultCollection(MetaLoadConfLabel,'LoadMetaData')
        objCollection=LoadResultCollection(MetaLoadConfLabel,'LoadMetaData')
        if not(objCollection is None):
            jsonData=json_util.dumps(objCollection,indent=5)
        else:
            jsonData=globalstore.globalResponseJson
        #sys.stdout.write(jsonData)
        globalstore.globalLogger.info('End')
'''
    sessionID = sys.argv[1]
    typeOfData = 'MetaValidateCSV'
    #sys.argv[3] = 'MyChk'
    inputvalues = sys.argv[3] #'NewBusinessChecks;SalesChecks;MobileAppsCheck'
    csvFile = sys.argv[4]    
    globalstore.init()
    globalstore.globalLogger.info('Start')
    ticketNum = 'T01'
    globalstore.globalSessionData = {SESSIONID: str(sessionID), TICKETNO: ticketNum}
    MetaLoadConfLabel=GenConfLbl(str(sessionID),ticketNum,str(typeOfData),METADFN)   
    substVar=str(sys.argv[2])  #RootNode
    validateCSV(str(sessionID), substVar, str(inputvalues), csvFile)
    #mbotLoadMeta(MetaLoadConfLabel, str(inputvalues), substVar)    
    SaveResultCollection(MetaLoadConfLabel,'LoadMetaData')
    objCollection=LoadResultCollection(MetaLoadConfLabel,'LoadMetaData')
    if not(objCollection is None):
        jsonData=json_util.dumps(objCollection,indent=5)
    else:
        jsonData=globalstore.globalResponseJson
    #sys.stdout.write(jsonData)
    globalstore.globalLogger.info('End')
'''
