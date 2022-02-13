import sys

def ArmNo():
    #take input from std in
    str=input("Enter number to check whether is Armstrong no or not: ")
    #calculate ho many digits are there in the number enetered
    l=len(str)
    #convert the input string to integer
    num=int(str)
    sum=0
    while num > 0:
         #to get the remainder ie digits starting from the units place etc
        rem=num % 10
        #print(rem)

# you need to calculate by adding individual digits to the power of number   ex: 153 = 3 digts so sum= (1*1*1 + 5*5*5 + 3*3*3)
         #  ** is used to do power of
        sum=sum + (rem**l)
        #print(sum)
        num=num // 10

    if sum==int(str) :
        strmsg = "Entered number %s is armstrong" % str
    else:
        strmsg= "Entered number %s is not armstrong" % str
    #write the output to std out
    sys.stdout.write(strmsg)

ArmNo()