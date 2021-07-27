import inspect

import pytest
import logging

class BaseClass:
    def test_loggerC(self):
        # logger will automatically capture the file name when yu give __name__
        logName=inspect.stack()[1][3]
        logObj = logging.getLogger(logName)
        LogHandle = logging.FileHandler("fileLog.log")
        logFormat = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")  # format for log file message
        LogHandle.setFormatter(logFormat)

        # add the file details where the file logging must be done
        logObj.addHandler(LogHandle)
        logObj.setLevel(logging.DEBUG)
        return logObj


