import inspect
import logging
from configparser import ConfigParser

import openpyxl

    '''''
    # Logging class
    def loggerC(self,ID="TC"):
        # logger will automatically capture the file name when yu give __name__
        logName = inspect.stack()[1][3]
        logObj = logging.getLogger(logName)
        file = time.asctime()
        file = str(file)
        file = file.replace(" ", "_")
        file = file.replace(".", "_")
        timeStamp = file.replace(":", "_")
        logPath = LogFilePath + "\\Log_"+ ID + "_" + timeStamp + ".log"
        LogHandle = logging.FileHandler(logPath)
        logFormat = logging.Formatter(
            "%(name)s : %(asctime)s : %(levelname)s : %(message)s")  # format for log file message
        LogHandle.setFormatter(logFormat)
        # add the file details where the file logging must be done
        logObj.addHandler(LogHandle)
        # print(debugLevel)
        logObj.setLevel(logging.DEBUG)
        return logObj
'''''



def readFromExcel(file):
    print("Reading from excel")
    book = openpyxl.load_workbook(file)
    total=book.sheetnames
    print(total)
    sheet = book.active
    print(sheet)
    if sheet !='Sheet2':

        book.move_sheet('Sheet1')
    sheet = book.active
    print(sheet)

readFromExcel("C:\\Users\\shubhav\\PycharmProjects\\PyAutomationFramework\\utilities\\PythonXLS.xlsx")



class MySQLclass:
    def connectMYSQLserver(self, log, host, database, username, pwd):
        log.info("Trying to connect to the MYSQL server ")
        try:
            conn = mysql.connector.connect(host=host, database=database, user=username,
                                           password=pwd)
            if conn.is_connected():
                log.info("connection to Database successful")
                return conn
        except Error as e:
            log.error(e)

    def getMYSQLQuery(self, query):
        #Connection = connectMYSQLserver(self, host, database, username, pwd)
        cursor = Connection.cursor()
        cursor.execute(query)
        result=cursor.fetchall()
        return result








