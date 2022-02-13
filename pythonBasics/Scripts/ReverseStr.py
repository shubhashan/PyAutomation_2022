#Reverse a string

def reverseStr(str):
    if not str:
        print("String is empty")

    print ("String before reversal : %s " % str)
    print ("Total length of the string : %d" % len(str))
    return str[::-1]

str="India @ 123"
ret=reverseStr(str)
print("Reversed string :  %s" %ret)