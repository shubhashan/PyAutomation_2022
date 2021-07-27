import requests
import json


res = requests.get("https://api.github.com/user", auth=('githubUser2787','Ns@123$%^'))
print("1")
print(res)

res = requests.get("https://api.github.com/users", auth=('githubUser2787','Ns@123$%^'))
print("2")
print(res)
resJ=res.json()
print(resJ)

user="githubUser2787"
res = requests.get("https://api.github.com/"+user, auth=(user,'Ns@123$%^'))
print("======== 3 ========")
print(res)
resJ=res.json()
print(resJ)



res = requests.get("https://api.github.com/users/repos")
print("4")
print(res)
resJ=res.json()
print(resJ)

res = requests.get("https://api.github.com/users/repos",verify=False, auth=('githubUser2787','Ns@123$%^'))
print("5")
print(res)
resJ=res.json()
print("--------=== Session manager")
print(resJ)

#===== Session manager

sess = requests.session()
sess.auth = auth=('githubUser2787','Ns@123$%^')
res = sess.get("https://api.github.com/users/repos")
print(res.json())
print(sess.headers)


### cookies

se=requests.session()
se.cookies.update({'visisisi' : 'Sept'})



cookie = {'helloCookie0' : '20222'}
cookie1 = {'helloCookxcie0' : '20x222'}
res=requests.get("https://httpbin.org/cookies",cookies=cookie)
print(res.text)


cookie = {'helloCookie0' : '20222'}

### Cookies with session manager

res=requests.get("https://httpbin.org/cookies",cookies=cookie)
print(res.text)
res=se.get("https://httpbin.org/cookies",cookies=cookie)
print(res.text)

###=======Redirection 3XX codes...
cookie = {'visit' : 'Sept'}
url="https://google.com"
print("======REDIRECTION=====")
res=requests.get(url)
print(res.history)
print(res.status_code)

print("======REDIRECTION = FALSE =====")
res=requests.get(url, allow_redirects=False)
print(res.history)
print(res.status_code)



#Wait for response using timeout value
res = requests.get(url,timeout=5)
print(res.status_code)


#====Send file attachment through API
url="http://httpbin.org/post"
files={'file': open('kkk.txt','rb')}
res=requests.post(url)
print(res.text)
res=requests.post(url,files=files)
print(res.status_code)
print(res.text)


