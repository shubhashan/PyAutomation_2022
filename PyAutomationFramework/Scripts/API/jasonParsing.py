import json


JsonStr= '{"name": "ABC","Languages" :["Java","Python","C++"]}'

#loads methos parse json string and will return dictionary

dict=json.loads(JsonStr)
print(type(dict))
print(dict)

print(dict['name'])
print(dict['Languages'])
l=dict['Languages']
print(dict['Languages'][1])
print(type(l))
print(l[2])