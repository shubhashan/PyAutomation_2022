import requests
from bs4 import BeautifulSoup
import re

data = requests.get("https://www.imdb.com/find?q=thriller&ref_=nv_sr_sm")
soup = BeautifulSoup(data.content, 'html.parser')  # html parser helps in formatting raw data
print(soup.prettify())

'''''
data = requests.get("https://amazon.com")
soup = BeautifulSoup(data.content, 'html.parser') #here it will not work since uses javascript
print(soup.prettify())
'''''
#return only the first row
movieTable = soup.find('table', {'class': 'findList'})
print("==============")
print(movieTable.prettify())
#findall returns all the rows
s = movieTable.findAll('tr')
for row in s:
    print(row)
