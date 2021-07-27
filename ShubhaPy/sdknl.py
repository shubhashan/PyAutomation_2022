import inspect
import time
print(time.asctime())
import logging
import re

class BaseClass1:
    #Logging class
    def loggerC(self):
        # logger will automatically capture the file name when yu give __name__
        logName = inspect.stack()[1][3]
        logObj = logging.getLogger(logName)
        filePath="logs/fileLogAPItests.log"
        LogHandle = logging.FileHandler(filePath)
        logFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # format for log file message
        LogHandle.setFormatter(logFormat)
        # add the file details where the file logging must be done
        logObj.addHandler(LogHandle)
        #print(debugLevel)
        logObj.setLevel(logging.DEBUG)
        return logObj

class B(BaseClass1):
    pass



