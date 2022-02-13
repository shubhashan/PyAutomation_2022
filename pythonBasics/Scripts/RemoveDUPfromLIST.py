#Method 1 : Simple logic

test_list = [1, 3, 5, 6, 3, 5, 6, 1]
final_list=[]
for i in test_list:
    if i not in final_list: #Checking if the element is not already present in the list
        final_list.append(i)

    print(final_list)


#Method 2 : using set()

