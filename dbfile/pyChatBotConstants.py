##pyDataMgmt Constants
SERVERNAME = '10.155.141.51'
PORTNUMBER = 27017
SESSIONID='SessionId'
TICKETNO='TicketNo'
LABEL='Label'
TYPE='Type'
RECORDS='records'
UDF='udf'
ID='_id'
CONFVAL='confVal'
Response_Get='Response.DataObjects.Information.Label'

##pyMarkTbl Constants
COLORCODE_TAG='ColorCode_Tag'
WHITE_FORMAT='#ffffff'
APPLICATION_FAULT='.*<applicationfault>.*'
SYSTEMFAULT='.*<systemfault>.*'
ORANGEBROWN='#f4b942'

##pyLDMeta Constants
APPLICATIONNO='Application_No'
STR='str'
YES='Y'
MOVE_TO_Q='Move_To_Q'
NO='N'
JSON_FORMAT='Container.Fields.Json'
NAME='Name'
METADFN='MetaDefn'

##DataFrame Skeleton Options pyMasterDataFrameFunctions
ATTACHPOINTQUERY=1
MALFORMEDQUERY=2
ATTACHPOINT=3
FIELDSMETA=4
ITERATORRUN=5
ITERATORVALUE=6
HEALTHCHECKRESULT=7
LABELCONFIG=8
SEQUENCEDEFN=9
ROWCOUNT=10
WEBSERVICECONSUMEPARAMS=11

##pyIterator Constants
INDEX='[$$index]'
INNERBLOCK='innerBlock'
SUBSTSTR='subststr'
MAXVAL='maxval'
APPEND_DOLLAR='$$'
REPLACEINDEX='$$index'
ITRVAR='itrVar'
ITERATOR='Iterator'
ENDITR='EndItr '

##pyRulesConstants
RULES='Rule'
RULE='rule'
FIELD='field'
VALUE='value'

##pyQueueMovement
QMoveApp='QMoveApp'
ITRPOLSW='ItrPolSW'

##pyQueryGen
CONNECTIONSTRING='connectionstring'
PASSWORD='password'
QMOVESWCLR='QMoveSWclr'
QUERY='query'
RUNQUERY='runQuery'
ATTACHPOINT='AttachPoint'
DBCONN='Dbconn'
XMLFILE='XMLFile'
DATA_STORE_XML='DATA_STORE_XML'
RE_DATA_STORE_XML='RE_DATA_STORE_XML'
DATAXML='DATAXML'
BIGXML='BIGXML'
PAYMENTDETAILSXML='PaymentDetailsXML'
RULESXML='RulesXML'
QUERYGEN='QueryGen'

##pyHealthCheck
CHECKOBJECT='checkobject'
HEALTHCHK='HealthChk'
GREEN_CODE='#86c425'
CHECKTYPE='checktype'
LEVEL='level'
EXTENDED='extended'
CHECKURL='CheckUrl'
CHECKSQL='CheckSql'
CHECKPORT='CheckPort'
BSTATUS='bStatus'
LIGHT_ORANGE='#f4b942'
CHECKDESCRIPTION='checkdescription'
URL='url'
VALIDATETEXT='validatetext'
INTERFACE='Interface'
DETAIL='Detail'
RESULT='Result'
FAILED='Failed'
SUCCESS='Success'
DB='db'
VALIDATSQL='validatsql'
SERVER='server'
SPORT='sPort'
JSON='JSON'
POST_VARS='postvars'

#pyBPC-WebServiceConsumer
WEBSERVICE = 'WebService'
GET='GET'
POST='POST'
SERCONSUMER='SerConsumer'
SERVICEMETHOD='ServiceMethod'
SERVICENAME='ServiceName'
PARAMETERS='Parameters'
URL='url'
CONTENT='content'
BUSINESSUNIT='business_unit'
CONTENTTYPE='content-type'
WEBSRVDEFN='WebsrvDefn'
RESOURCE='Resource'

##pySequence
SEQUENCE='SequenceDefn'
CHECKWEBREQ='CheckWebReq'
SEQUENCEDEFL='SequenceDefl'

##ChatBotLogger
LOG_FILE='ChatBotLogs/'
LOG_EXTENSION='.log'
#LOG_FORMAT='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
LOG_FORMAT='%(asctime)s - %(name)s - %(levelname)s - %(filename)s- %(funcName)20s()- %(message)s'
DB_LOGGING='DBLogging'
