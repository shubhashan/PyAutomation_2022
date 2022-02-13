#Prime number

def prime(num, di = None):
    if num == 0:
        return 2
    if num == 1 or num == 2:
        return 1
    if di == None :
        di = num-1
        while (di >= 2):
            for i in range (2 ,di):
                if num % i == 0:
                    return 0
                else:
                    prime(num,i-1)
            return 1

#num = 49
#Taking user input
num=input("Enter number to check whether is Armstrong no or not: ")
#Default input type in str, so convert to int
num=int(num)
ret = prime(num)

if ret == 1:
    print("Number is prime")
elif ret == 2:
    print("Number is either prime nor composite")
else:
    print('Number is not prime')
