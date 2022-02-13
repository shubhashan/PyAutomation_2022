#Bubblesort

def bubblesort(a):
    print("The unsorted array is : %s"% a)
    length=len(a)
    #traversal of all elements, mainly 5 iterations
    for i in range(length):
        #this loop is for comparisons for the remaining items ex: iteration 1 all 5 elements
        # iteration 2 first 4 since the last element would reach the last position etc
        for j in range(0,length-1-i):
            a[j]=int(a[j])#Input type is str so need to ocnvert to int
            print("a[j] : %s" % a[j])
            a[j+1] = int(a[j+1])
            print("a[j+1] : %s" % a[j+1])
            if a[j] > a[j+1]:
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp
            print("After swapping it is : %s" % a)
    print("The sorted array is : %s" % a)

#a=[76,231,11,2,35]
a=[]
inp=input("Enter numbers to be sorted : ")
a=inp.split(',')

bubblesort(a)