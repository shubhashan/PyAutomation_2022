import requests

url="https://reqres.in/api/register"
data1={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }



res = requests.post(url, data=data1)
print(res)
jRes = res.json()
print(jRes)
print(jRes['token'])