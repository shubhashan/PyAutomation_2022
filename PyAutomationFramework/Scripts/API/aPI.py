
import json

with open("C:\\Users\\shubhav\\PycharmProjects\\PyAutomationFramework\\Scripts\\API\\JsonFile.json", 'r') as f:
    jP = json.load(f)
    #print(jP)
    print(jP['partitions'])
    print(len(jP['partitions']))
    leng=len(jP['partitions'])
    for i in range(0,leng):
        UUID = "105F8E0F-BAAB-4978-B172-FAA2E8BA89D3"
        if jP['partitions'][i]['partitionGuid'] == str(UUID):
            print(jP['partitions'][i]['partitionGuid'])
            print(jP['partitions'][i]['partitionId'])


    #print(jP['partitions'][0])
    #print(jP['partitions'][0]['partitionId'])


    #print(jP['partitions'][str(UUID)]['partitionId'])
    #print(jP['partitions'][1])
#print(dict)
#print(dict['partitions'])
