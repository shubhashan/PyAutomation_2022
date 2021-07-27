import json

#parse content from json file
#load function used to parse json from file
with open("C:\\Users\\shubhav\\PycharmProjects\\APITesting\\JsonFile.json", 'r') as f:
    jP = json.load(f)
    print(jP)
    print(jP['total'])
    print(jP['page'])
    print(jP['data'][0])
    print(jP['data'][3])

    #store the dict data in a list so that you can extract the nested data
    l=jP['data']
    print("-----------------------------")
    print(l)
    print(len(l))
    print(l[2]['id'])

    for i in range (0,len(l)):
        print("-----------------------------")
        print(l[i]['id'])
        #Here you are trying to print thr name when id is 10
        if l[i]['id'] == 10:
            print("Here")
            print(l[i]['first_name'])