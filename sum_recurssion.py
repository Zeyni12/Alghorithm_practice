def sum(arr):

    if arr == []:
        return 0
    else:
        return arr[0] + sum(arr[1:])
d=[2,4,5]    
print(sum(d))