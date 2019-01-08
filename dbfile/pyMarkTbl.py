import pandas as pd
from pyDataMgmt import *
import globalstore
from pyQuerygen import *
import io
from pyDataMgmt import *
import sys
import re
from pyChatBotConstants import *

def ColorTbldf(objDFTable,clrLabel):
    globalstore.globalLogger.info('Start')
    try:
        globalstore.globalLogger.info(LABEL+': ' + clrLabel)
        if not (objDFTable is None):
                   objDFTable[COLORCODE_TAG] =WHITE_FORMAT
                   for dfrow in objDFTable.iterrows():
                       for icol in range(dfrow[1].__len__()):
                           rColor=Colormatch(dfrow[1], clrLabel)
                           dfrow[1][COLORCODE_TAG]=rColor
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        objDFTable=None
    globalstore.globalLogger.info('End')
    return objDFTable

def Colormatch(objDFrow,clrLabel):
    globalstore.globalLogger.info('Start')
    lMatchexpr={APPLICATION_FAULT,SYSTEMFAULT}
    rColormatch=WHITE_FORMAT
    try:
        if not(objDFrow is None):
           for icol in range(objDFrow.__len__()):
              for rMatch in lMatchexpr.__iter__():
                  if ((objDFrow[icol] is not None) and re.match(rMatch , objDFrow[icol])):
                      rColormatch=ORANGEBROWN
    except:
        globalstore.globalLogger.error('Exception Information:',exc_info=1)
        rColormatch=None
    globalstore.globalLogger.info('End')
    return rColormatch
