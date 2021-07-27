import inspect
import logging

from configparser import ConfigParser

class Config1():
    def getConfig(self,testcase,value):
        file = "config.ini"
        config = ConfigParser()
        config.read(file)
        print(config.read(file))
        configValue = config[testcase][value]
        return configValue

    def setConfig(self,testcase,key,value):
        file = "config.ini"
        config = ConfigParser()
        config.read(file)
        self.configValue=config.set(testcase,key,value)
        with open(file, 'w') as configFile:
            config.write(configFile)
        return self.configValue


c1=Config1()
#print(c1.getConfig("deleteReqP2","url"))

class Hel(Config1):
    def hel(self):
        print("hello")
        #print(self.getConfig("deleteReqP1","url"))


c2=Hel()
print(c2.getConfig("deleteReqP2","url"))


class BaseClassOne:
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








