path="C:\\Users\\shubhav\\textFile1.txt"

#if we use this, we need not manually close the file

#Read the file , store the list and then reverse and print
with open(path,'r') as reader:
    L=reader.readlines()
    print(L)
    RL=L[::-1]
    print(RL)
    #we can also use reversed func reversed(L)

    with open(path,'w') as writer:
        for line in RL:
            writer.write(line)

