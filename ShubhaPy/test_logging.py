import pytest
import logging

#in pytest everything must be in functions
def test_logger():
#logger will automatically capture the file name when yu give __name__
    logS=logging.getLogger(__name__)
    LogH=logging.FileHandler("fileLog.log")
    logF=logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s") #format for log file message
    LogH.setFormatter(logF)

#add the file details where the file logging must be done
    logS.addHandler(LogH)
    logS.setLevel(logging.DEBUG)

    logS.debug("Debug statement")
    logS.warning("Warning statement")
    logS.info("Info statement")


