import os

from Utils.Utils import *


def GetScriptNAme():
    scriptName = os.path.basename(__file__)  # ScriptName.py
    scriptName = os.path.splitext(os.path.basename(__file__))[0]
    return scriptName


class B(Config):
    def t(self):
        print(self.getConfig("test_deleteReqP1", "url"))

print(B.t())





GetScriptNAme()




