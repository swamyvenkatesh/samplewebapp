import pandas as pd
from pyDataMgmt import *
import globalstore
from pyQuerygen import *
import io
from pyDataMgmt import *
from pyLDMeta import *
from pyRules import *
from pyHealthcheck import *
from pyWebsrvCon import *
from Testweb import *
import sys
import re
import time

def GenConflbl(SessionId,TicketNo,Label,Type):
    return {'SessionId':SessionId,'TicketNo':TicketNo,'Label':Label,'Type':Type}

def initRunTimeItr(itrConfLabel,substVars):
    itrInnerBlock=LoadConfig(itrConfLabel)
    srootvar = GetRoot(itrConfLabel, substVars)
    rootvar=LoadRoot(itrConfLabel,srootvar)
    #print(globalstore.globalList[srootvar])
    maxitrval=globalstore.globalList[srootvar].__len__()
    itrval=0
    itrsubststr=substVars+'[$$index]'
    itrValue=pd.DataFrame([[itrConfLabel['Label'],substVars,itrval,maxitrval,itrInnerBlock,itrsubststr]],columns=['Label','itrVar','itrVal','maxval','innerBlock','subststr'])
    itrRun=pd.DataFrame([[itrConfLabel['SessionId'],itrConfLabel['TicketNo'],itrConfLabel['Label'],itrConfLabel['Type'],itrValue]],columns=['SessionId','TicketNo','Label','Type','Value'])
    SaveMeta(itrRun)
    dictItrValue=itrValue.iloc[0].to_dict()
    return dictItrValue

def initRunTimeItrInner(itrConfLabel,substVars):
    substVars=substVars.replace("'",'"')
    itrInnerBlock=itrConfLabel['innerBlock']
    maxitrval=0
    itrval=0
    itrsubststr=substVars+'[$$index]'
    #print(substRootVars(substVars)+'.__len__()')	
    try:
        maxitrval=eval(substRootVars(substVars)+'.__len__()')
    except:
        maxitrval = 0
        srootvar = GetRoot(itrConfLabel, substVars)
        rootvar = LoadRoot(itrConfLabel, srootvar)
        maxitrval = globalstore.globalList[srootvar].__len__()
    itrValue = pd.DataFrame([[itrConfLabel['Label'], substVars, itrval, maxitrval, itrInnerBlock, itrsubststr]],
                            columns=['Label', 'itrVar', 'itrVal', 'maxval', 'innerBlock', 'subststr'])
    #itrRun=pd.DataFrame([[itrConfLabel['SessionId'],itrConfLabel['TicketNo'],itrConfLabel['Label'],itrConfLabel['Type'],itrValue]],columns=['SessionId','TicketNo','Label','Type','Value'])
    #SaveMeta(itrRun)
    dictItrValue=itrValue.iloc[0].to_dict()
    return dictItrValue

def runItrator(sSessionID,sLabel,substVars):
    ticketNum='T01'
    globalstore.globalSessionData={'SessionId':sSessionID,'TicketNo':ticketNum}
    itrConfLabel=GenConflbl(sSessionID,ticketNum,sLabel,'Iterator')
    runItr(itrConfLabel, substVars)
    return True

def runItr(itrConfLabel, substVars):
    itrValue = initRunTimeItr(itrConfLabel,substVars)
    for i in range(itrValue['maxval']):
        sSubststmt=dynreplacestatments(itrValue['innerBlock'][:],'$$'+itrValue['Label'],itrValue['subststr'],i)
        runstmts(sSubststmt)
    return True

def runItrInner(itrConfLabel, substVars):
    itrValue = initRunTimeItrInner(itrConfLabel,substVars)
    for i in range(itrValue['maxval']):
        sSubststmt=dynreplacestatments(itrValue['innerBlock'][:],'$$'+itrValue['Label'],itrValue['subststr'],i)
        runstmts(sSubststmt)
    return True


def dynreplacestatments(aSrouceStmt,sFindStr,sreplaceString,iIndex):
    sreplaceString=sreplaceString.replace('$$index',str(iIndex))
    for i in range(aSrouceStmt.__len__()):
        aSrouceStmt[i]=aSrouceStmt[i].replace(sFindStr,sreplaceString)
    return aSrouceStmt

def runstmts(sStmts):
    bInnerLoop = False
    for i in range(sStmts.__len__()):
        if (bInnerLoop):
            if (re.match(endItr, sStmts[i])):
                bInnerLoop = False
                dfInnferLoop['innerBlock'] = itrInnerBlock
                runItrInner(dfInnferLoop, dfInnferLoop['itrVar'])
            else:
                itrInnerBlock.append(sStmts[i])
            continue
        if(re.match('(StartItr\s*)(.*?\s)(.*)',sStmts[i])):
            innerLoopconf=re.findall('(StartItr\s*)(.*?\s)(.*)',sStmts[i])
            innerLoopconf=innerLoopconf[0]
            dfInnferLoop={'SessionId':globalstore.globalSessionData['SessionId'],'TicketNo':globalstore.globalSessionData['TicketNo'],'Label':innerLoopconf[1].strip(),'itrVar':innerLoopconf[2].strip(),'innerBlock':object()}
            itrInnerBlock=[]
            endItr='EndItr '+dfInnferLoop['Label']            
            bInnerLoop=True
            continue
        if(bInnerLoop==False):
            sStmts[i] = substRootVars(sStmts[i])
            #webConfs=dynreplacehirarchystatments(webConfs,substVar,'Parameters')			
            #sStmts[i] = subsDynValue(sStmts[i])
            #print(sStmts[i])
            exec(sStmts[i])


if __name__ == "__main__":
    globalstore.init()
    ticketNum='T01'
    globalstore.globalSessionData={'SessionId':str(sys.argv[1]),'TicketNo':ticketNum}
    substVar=str(sys.argv[2])
    itrConfLabel=GenConflbl(str(sys.argv[1]),ticketNum,str(sys.argv[3]),'Iterator')
    runItr(itrConfLabel, substVar)
