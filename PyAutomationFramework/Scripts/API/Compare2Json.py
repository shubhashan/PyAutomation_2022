import json

#parse content from json file
#load function used to parse json from file

with open("C:\\Users\\shubhav\\PycharmProjects\\APITesting\\JsonFile.json", 'r') as f:
    jP = json.load(f)

with open("C:\\Users\\shubhav\\PycharmProjects\\APITesting\\JsonFile1.json", 'r') as fi:
    jP1 = json.load(fi)

#compare these 2 dictionaries
print("P---1")
print(jP)
print("P---2")
print(jP1)
assert jP==jP1


