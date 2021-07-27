import requests
from requests.auth import HTTPBasicAuth
user = 'githubUser2787'
pwd = 'Ns@!@#456'
res = requests.get("https://api.github.com", auth=HTTPBasicAuth(username=user , password= pwd))
print(res.status_code)
print(res.headers)
resJ=res.json()
print(resJ)

token = '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'
headers = {'Authorization' : 'token' + token}

repos= "PrivateRepo"
login=requests.get("https://api.github.com", headers=headers)
print("----token------user---111111")
print(login.status_code)
print(login.json())

login=requests.get("https://api.github.com/user/repos", auth=(user,token))
#login=requests.get("https://api.github.com/user/repos", headers=headers)
print("----token------user")
print(login.status_code)
print(login.json())


login=requests.get("https://api.github.com/user/repos?name=PrivateRepo", headers=headers)
print("----token------Privaterepo-----")
print(login.status_code)
print(login.json())


login=requests.get("https://api.github.com/repos/" + user + "/" +repos , headers=headers)
print(login.status_code)
print(login.json())


login=requests.get("https://api.github.com/notifications", auth=(user,token))
print(login.status_code)
print(login.json())