import mysql.connector
from utilities.Utils import *

conn = mysql.connector.connect(host='localhost', database='Person', user='root',
                               password='freebsd')
print(conn.is_connected())