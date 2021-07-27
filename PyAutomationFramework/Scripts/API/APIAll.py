import requests
import pytest
import json


try:
    res = requests.get("https://httpbin.org/delay/3", timeout=2)
except requests.exceptions.Timeout as e:
        print(e)
        print("Time out occured")



#===========GET
res = requests.get('http://216.10.245.166/Library/GetBook.php',params={'AuthorName':'Rahul Shetty'})

Jres=res.json()
print(Jres)

print(Jres[0]['book_name'])
print(Jres[2]['isbn'])


#===================POST

res=requests.post("http://216.10.245.166/Library/Addbook.php",json={

"name":"Learn Appium Automation with Java",
"isbn":"11bcd151",
"aisle":"122712",
"author":"John foe"
}, headers={"Content-Type" : "application/json"},)

Jres=res.json()
print(Jres)
print(bookID)




res=requests.post("http://216.10.245.166/Library/Deletebook.php",json={

"ID":bookID
}, headers={"Content-Type" : "application/json"},)

print(res.status_code)
Jres=res.json()
print(Jres)

