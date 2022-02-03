# -------------- All the packages/modules to be imported ----------------
import inspect
import logging
import time
from configparser import ConfigParser
import mysql.connector
from mysql.connector import Error
import pytest
import json
import requests
import pytest
import re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from PageObject.Cutomers import Customers
from PageObject.LoginPage import LoginPage
from PageObject.searchCustomer import searchCustomers
from PageObject.HomePage import HomePage
from PageObject.EditCustomerInfo import editCustomerInfo
# --------Global Variables used -------




LogFilePath = "..//..//Logs"
ConfigIniFilePath = "..//..//utilities//config.ini"

class UtilClassOne():
    def sendMySQLQuery(self,connectionOBJ,query):
        conn = connectionOBJ
        #self.log.info("Connecting to the SQL server")
        if conn.is_connected:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            return result

    def getConfig(self, testcaseID="DEFAULT", key=None):
        file = ConfigIniFilePath
        #self.log.info("Fetching details from the config INI file from path %s " % ConfigIniFilePath)
        config = ConfigParser()
        config.read(file)
        configValue = config.get(testcaseID, key)
        return configValue

    def setConfig(self, log, testcaseID="DEFAULT", key=None, value=None):
        file = ConfigIniFilePath
        config = ConfigParser()
        config.read(file)
        self.configValue = config.set(testcaseID, key, value)
        with open(file, 'w') as configFile:
            config.write(configFile)
        return self.configValue


