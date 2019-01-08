from pyLDMeta import *
from pyIterator import *

globalstore.init()
globalstore.globalLogger.info('Start')
MetaLoadConfLabel=GenConflbl(str(sys.argv[1]),'T01',QMoveApp,METADFN)
#print("------------")
#print(sys.argv[0])
#print(sys.argv[1])
#print(sys.argv[2])
#print(sys.argv[3])
#print("------------")
#substVar='appbase'
#mbotLoadMeta(MetaLoadConfLabel, '192733517,PD;216733051,Req;216652664,Fnd', substVar)
substVar=str(sys.argv[2])
mbotLoadMeta(MetaLoadConfLabel, str(sys.argv[3]), substVar)
itrConfLabel=GenConflbl(str(sys.argv[1]),'T01',ITRPOLSW,ITERATOR)
runItr(itrConfLabel, substVar)
#sys.stdout.write(globalstore.globalResponseJson)
globalstore.globalLogger.info('End')
