import pytest
import logging
from BaseClass import BaseClass


class TestLogF(BaseClass):
    def testLogFunc(self):
        log=self.test_loggerC()
        log.debug("Debug statement")
        log.warning("Warning statement")
        log.info("Info statement")


