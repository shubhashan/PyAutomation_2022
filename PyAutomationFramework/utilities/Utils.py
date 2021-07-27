import inspect
import logging
import time
from configparser import ConfigParser



#--------Global Variables used -------
LogFilePath = "C:\\Users\\shubhav\\PycharmProjects\\PyAutomationFramework\Logs"
ConfigIniFilePath = "C:\\Users\\shubhav\\PycharmProjects\\PyAutomationFramework\\utilities\\config.ini"

class UtilClassOne:
    #Logging class
    def loggerC(self,testcaseID='TC'):
        # logger will automatically capture the file name when yu give __name__
        logName = inspect.stack()[1][3]
        logObj = logging.getLogger(logName)
        file = time.asctime()
        file = str(file)
        file = file.replace(" ", "_")
        file = file.replace(".", "_")
        timeStamp = file.replace(":", "_")
        logPath=LogFilePath+"\\"+testcaseID+"_"+timeStamp+".log"
        print(logPath)

        LogHandle = logging.FileHandler(logPath)
        logFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # format for log file message
        LogHandle.setFormatter(logFormat)
        # add the file details where the file logging must be done
        logObj.addHandler(LogHandle)
        #print(debugLevel)
        logObj.setLevel(logging.DEBUG)
        return logObj

    def getConfig(self,testcaseID="DEFAULT",key=None):
        file = ConfigIniFilePath
        config = ConfigParser()
        config.read(file)
        #print(config.read(file)) ---- > path of the ini file
        configValue = config.get(testcaseID,key)
        return configValue

    def setConfig(self,testcaseID="DEFAULT",key=None,value=None):
        file = ConfigIniFilePath
        config = ConfigParser()
        config.read(file)
        self.configValue=config.set(testcaseID,key,value)
        with open(file, 'w') as configFile:
            config.write(configFile)
        return self.configValue








