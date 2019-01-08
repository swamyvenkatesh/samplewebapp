import pandas as objPnd
import logging as objLog
import os



def AttachPointQuery():
    #objLog.Logger()
    #print ("'query', 'Dbconn', 'AttachPoint'")
    return objPnd.DataFrame(columns=['query', 'Dbconn', 'AttachPoint'])
 
def MalFormedQuery():
    #print ("MalFormedQuery")
    return objPnd.DataFrame(columns=['MalFormedQuery'])
 
def AttachPoint():
    #print ("sAttachPoint")
    return objPnd.DataFrame(columns=['sAttachPoint'])
 
def FieldsMeta():
    #print ("'Name', 'Type', 'Mandatory'")
    return objPnd.DataFrame(columns=['Name', 'Type', 'Mandatory'])
 
def IteratorRun():
    #print ("'SessionId', 'TicketNo', 'Label', 'Type', 'Value'")
    return objPnd.DataFrame(columns=['SessionId', 'TicketNo', 'Label', 'Type', 'Value'])
 
def IteratorValue():
    #print ("'Label','itrVar','itrVal','maxval','innerBlock','subststr'")
    return objPnd.DataFrame(columns=['Label','itrVar','itrVal','maxval','innerBlock','subststr'])
 
def HealthCheckResult():
    #print ("'Interface', 'Detail', 'Result','ColorCode_Tag','bStatus'")
    return objPnd.DataFrame(columns=['Interface', 'Detail', 'Result','ColorCode_Tag','bStatus'])

def WebSerConsumeParams():
    #print ("'ServiceMethod', 'ServiceName','Parameters'")
    return objPnd.DataFrame(columns=['SessionId', 'TicketNo', 'Label', 'Type', 'Value'])
 
def LabelConfig():
    #print ("'Label','Type','Value'")
    return objPnd.DataFrame(columns=['Label','Type','Value'])

def SequenceDefn():
    return objPnd.DataFrame(columns=['SessionId','TicketNo','Label','Type','innerBlock'])
	
def RowCount():
    return objPnd.DataFrame(columns=['RowCount'])
 
 
def GetDataFrameSkeleton(argument):
    switcher = {
        1: AttachPointQuery,
        2: MalFormedQuery,
        3: AttachPoint,
        4: FieldsMeta,
        5: IteratorRun,
        6: IteratorValue,
        7: HealthCheckResult,
        8: LabelConfig,
        9: SequenceDefn,
        10:RowCount,
        11:WebSerConsumeParams
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: "Invalid Option")
    # Execute the function
    objDFSkeleton=func()
    return objDFSkeleton

#data=GetDataFrameSkeleton(1)
#data=data['1','2','3']
#data1=objPnd.DataFrame(None,columns=data.columns)
#print(data1)
