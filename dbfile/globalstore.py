import ChatBotLogger
from pyChatBotConstants import *

def init():
    global globalList
    global globalRefData
    global globalSessionData
    global globalLogger
    global globalResponseSavedData
    global globalCollectionData
    global globalResponseJson
    globalList = dict()
    globalRefData=dict()
    globalSessionData=dict()
    globalResponseSavedData=dict()
    globalResponseJson=dict()
    globalCollectionData=dict()
    globalLogger = ChatBotLogger.CreateLogFile()
