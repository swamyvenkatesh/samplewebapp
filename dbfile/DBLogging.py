import sys,string, time, logging
import pyodbc

class DBHandler(logging.Handler):
    def __init__(self, dsn, uid='', pwd=''):
        logging.Handler.__init__(self)
        self.dsn = dsn
        self.uid = uid
        self.pwd = pwd
        self.conn =  pyodbc.connect('DRIVER={SQL Server};SERVER=CTSC01233881801\SQLEXPRESS;DATABASE=DIGEST;UID=sa1;PWD=password-3',autocommit=True)
        self.SQL = """INSERT INTO [TBL_MICROBOT_LOGGING] (
                        Name,
                        LogLevel,
                        LevelText,
                        Filename,
                        Pathname,
                        [Lineno],
                        MSG,
                        Exception,
                        Thread
                   )
                   VALUES (
                        '%(name)s',
                        %(levelno)d,
                        '%(levelname)s',
                        '%(filename)s',
                        '%(pathname)s',
                        %(lineno)d,
                        '%(message)s',
                        '%(exc_text)s',
                        '%(thread)s'
                   );
                   """
        self.cursor = self.conn.cursor()

    def emit(self, record):
        try:
            #use default formatting
            self.format(record)
            if record.exc_info:
                exceptionText=logging._defaultFormatter.formatException(record.exc_info)
                truncateString=str(exceptionText).replace("'","")
                record.exc_text = truncateString
            else:
                record.exc_text = ""
            sql = self.SQL % record.__dict__
            self.cursor.execute(sql)
            self.conn.commit()
        except:
            import traceback
            ei = sys.exc_info()
            traceback.print_exception(ei[0], ei[1], ei[2], None, sys.stderr)
            del ei

    def close(self):
        self.cursor.close()
        self.conn.close()
        logging.Handler.close(self)

