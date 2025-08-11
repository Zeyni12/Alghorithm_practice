def binary_search(arr,item):
    low = 0
    high = len(arr)-1

    while low <= high :
        mid = (low + high) // 2
        gusse = arr[mid]

        if gusse == item :
            return mid 

        elif gusse > item :  
            high =  mid-1
        else:
            low = mid + 1

    return None

my_list = [1,4,6,8,9,11]
print(binary_search(my_list,9))