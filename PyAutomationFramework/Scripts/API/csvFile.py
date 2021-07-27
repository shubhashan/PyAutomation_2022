# package for reading & writing CSV
import csv

file = 'C:\\Users\\shubhav\\PycharmProjects\\APITesting\\Utils\\text.csv'
# file open in read mode
with open(file, 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(csvReader)
    name = []
    status = []

    # convert into list...
    # print(list(csvReader))
    for row in csvReader:
        print(row)
        name.append(row[0])
        status.append(row[1])

    print(name)
    print(status)

    index = name.index('c')
    print(status[index])

    # write back to CSV file
    # Open in append mode, if yu use write mode , it will scrap the entire contents
with open(file, 'a') as WFile:
    write = csv.writer(WFile)
    # Provide the data as a list ( be in read or write modes)
    write.writerow(['e', 'Rejected'])
    write.writerow(['f', 'Approved'])





