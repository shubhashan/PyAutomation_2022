path="C:\\Users\\shubhav\\textFile.txt"
file=open(path)
#read line at a time
print(file.readline())
#read entire file contents
print(file.read())

#read n no of characters
print(file.read(3))

file.close()


def readLine():
    path = "C:\\Users\\shubhav\\textFile.txt"
    file = open(path)
    #Read the first line
    line = file.readline()
    while line != "":
        print(line)
        #Read the next line
        line = file.readline()

readLine()


path="C:\\Users\\shubhav\\textFile1.txt"
file=open(path)
#same as readline but stores in list
s=file.readlines()
for i in s:
    print(i)