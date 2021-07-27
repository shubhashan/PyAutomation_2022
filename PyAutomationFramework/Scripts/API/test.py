from datetime import datetime

#file=datetime.now()
#file=str(file)
#file=file.replace(" ","_")
#print(file)

import json
#====Send file attachment through API
import requests

url="http://httpbin.org/post"
files={'file': open('kkk.txt','rb')}
res=requests.post(url)
print(res.text)
print(files)
jRes1=res.json()
print(jRes1['files'])
res=requests.post(url,files=files)
jRes=res.json()
print(res.status_code)
print(res.text)
print(jRes['files'])
print(jRes1['files'] != jRes['files'])
