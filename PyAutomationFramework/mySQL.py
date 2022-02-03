import mysql.connector

# host
# DB name
# Authentication - username,pwd
'''''
conn = mysql.connector.connect(host='localhost', database='student', user='root',
                               password='freebsd')
print(conn.is_connected())
'''

conn = mysql.connector.connect(host='localhost', database='PythonAutomation', user='root',
                               password='freebsd')
print(conn.is_connected())

# cursor func creates a streamline wut the database
C = conn.cursor()
C.execute('select * from CustomerInfo')
'''''  #fetch the first record
row = C.fetchone()
print(row)
print(row[3])
'''''
res = C.fetchall()
print(res)
print("===== printing the list items=====")
sum = 0
for i in res:
    print(i)
    print(i[2])
    sum = sum + i[2]

print(sum)

query = "update CustomerInfo set Location = %s where CourseName =%s "
data = ('UK', 'Jmeter')
C.execute(query, data)
conn.commit()

C.execute('select * from CustomerInfo')
res = C.fetchall()
print(res)
print("======")

C.execute("delete from CustomerInfo where courseName = 'WebServices' ")
conn.commit()

C.execute('select * from CustomerInfo')
res = C.fetchall()
print(res)
