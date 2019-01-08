from pyIterator import *
from pyLDMeta import *
import time
import json

def initRunTimeSeq(SeqConfLabel,asubstVars):    
    SeqInnerBlock=LoadConfig(SeqConfLabel)
    for i in range(asubstVars.__len__()):
        SeqInnerBlock=dynreplacestatments(SeqInnerBlock,'$$'+str(i),asubstVars[i],0)
    seqValue=pd.DataFrame([[SeqConfLabel['SessionId'],SeqConfLabel['TicketNo'],SeqConfLabel['Label'],'SequenceDefn',SeqInnerBlock]],columns=['SessionId','TicketNo','Label','Type','innerBlock'])
    SaveMeta(seqValue)
    dictSeqValue=seqValue.iloc[0].to_dict()
    return dictSeqValue

def runSeq(seqConfLabel, substarr):
    aSeqstmt = initRunTimeSeq(seqConfLabel, substarr)    
    runstmts(aSeqstmt['innerBlock'])
    return True


if __name__ == "__main__":
    globalstore.init()
    ticketNum='T01'
    globalstore.globalSessionData={'SessionId':str(sys.argv[1]),'TicketNo':ticketNum}
    substVar=str(sys.argv[2])    
    seqConfLabel=GenConflbl(str(sys.argv[1]),ticketNum,str(sys.argv[2]),'SequenceDefn')
    seqDeflLabel = GenConflbl(str(sys.argv[1]), ticketNum, str(sys.argv[2]), 'SequenceDefl')
    substarr=sys.argv[1:2]
    substarr.extend(sys.argv[3:])   
    runSeq(seqConfLabel, substarr)    
    SaveResultCollection(seqConfLabel,'Sequence')    
    objCollection=NewLoadResultCollection(substVar)
    if not(objCollection is None):
        jsonData=json_util.dumps(objCollection,indent=5)
    else:
        jsonData=globalstore.globalResponseJson
    #sys.stdout.write(jsonData)
    #FileName = substVar + '_output.json'   
    #with open(FileName, 'w') as outfile:
    #    outfile.write(jsonData)

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
