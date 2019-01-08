import logging as objLog
import os
import datetime
from DBLogging import *
from pyChatBotConstants import *


def CreateLogFile():
   curDt=datetime.datetime.now().strftime('ChatBot_%m_%d_%Y_%H_%M')
   LOG_FILENAME = str(curDt)
   LOG_FILENAME=LOG_FILE+LOG_FILENAME+LOG_EXTENSION

   logger = objLog.getLogger("")
   logger.setLevel(objLog.DEBUG)
   # create file handler which logs even debug messages
   fh = logging.FileHandler(LOG_FILENAME)
   fh.setLevel(logging.DEBUG)
   # create console handler with a higher log level
  # ch = logging.StreamHandler()
  # ch.setLevel(logging.ERROR)

   #dh = DBHandler(DB_LOGGING)
   #dh.setLevel(logging.ERROR)
   #logger.addHandler(dh)

   # create formatter and add it to the handlers
   formatter = logging.Formatter(LOG_FORMAT)
   #ch.setFormatter(formatter)
   fh.setFormatter(formatter)
   #dh.setFormatter(formatter)

   #logger.addHandler(ch)
   logger.addHandler(fh)
   #logger.addHandler(dh)

   return objLog

