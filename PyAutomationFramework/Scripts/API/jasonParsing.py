import json

# Ddict = "{'File Name': {0: 'IGNORE', 1: 'IGNORE', 2: 'IGNORE', 3: 'IGNORE', 4: 'IGNORE', 5: 'IGNORE', 6: 'IGNORE', 7: 'IGNORE', 8: 'IGNORE', 9: 'IGNORE'}, 'Row Number': {0: 2, 1: 3, 2: 4, 3: 5, 4: 37, 5: 38, 6: 62, 7: 63, 8: 64, 9: 65}, 'Date': {0: 'IGNORE', 1: 'IGNORE', 2: 'IGNORE', 3: 'IGNORE', 4: 'IGNORE', 5: 'IGNORE', 6: 'IGNORE', 7: 'IGNORE', 8: 'IGNORE', 9: 'IGNORE'}, 'User': {0: 'dataintegrity@VertexSMB.local', 1: 'dataintegrity@VertexSMB.local', 2: 'dataintegrity@VertexSMB.local', 3: 'dataintegrity@VertexSMB.local', 4: 'dataintegrity@VertexSMB.local', 5: 'dataintegrity@VertexSMB.local', 6: 'dataintegrity@VertexSMB.local', 7: 'dataintegrity@VertexSMB.local', 8: 'dataintegrity@VertexSMB.local', 9: 'dataintegrity@VertexSMB.local'}, 'Change Type': {0: 'Automatic', 1: 'Automatic', 2: 'Automatic', 3: 'Automatic', 4: 'Automatic', 5: 'Automatic', 6: 'Automatic', 7: 'Automatic', 8: 'Automatic', 9: 'Automatic'}, 'Action Type': {0: 'Update', 1: 'Update', 2: 'Update', 3: 'Update', 4: 'Update', 5: 'Update', 6: 'Update', 7: 'Update', 8: 'Update', 9: 'Update'}, 'Template': {0: 'VAT - EU Country Returns', 1: 'VAT - EU Country Returns', 2: 'VAT - EU Country Returns', 3: 'VAT - EU Country Returns', 4: 'VAT - EU Country Returns', 5: 'VAT - EU Country Returns', 6: 'VAT - EU Country Returns', 7: 'VAT - EU Country Returns', 8: 'VAT - EU Country Returns', 9: 'VAT - EU Country Returns'}, 'Column': {0: 'Quantity', 1: 'Quantity', 2: 'Quantity', 3: 'Quantity', 4: 'Quantity', 5: 'Quantity', 6: 'Quantity', 7: 'Quantity', 8: 'Quantity', 9: 'Quantity'}, 'Old Value': {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}, 'New Value': {0: 5, 1: 5, 2: 5, 3: 5, 4: 5, 5: 5, 6: 5, 7: 5, 8: 5, 9: 5}, 'Rule': {0: 'IGNORE', 1: 'IGNORE', 2: 'IGNORE', 3: 'IGNORE', 4: 'IGNORE', 5: 'IGNORE', 6: 'IGNORE', 7: 'IGNORE', 8: 'IGNORE', 9: 'IGNORE'}, 'RuleSet': {0: 'IGNORE', 1: 'IGNORE', 2: 'IGNORE', 3: 'IGNORE', 4: 'IGNORE', 5: 'IGNORE', 6: 'IGNORE', 7: 'IGNORE', 8: 'IGNORE', 9: 'IGNORE'}}"
# JDict=json.loads(Ddict)
# print(JDict)


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