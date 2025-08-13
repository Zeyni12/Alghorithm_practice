def my_max(arr):
    if len(arr) == 1:  # Base case: only one element
        return arr[0]
    else:
        sub_max = my_max(arr[1:])  # Max of the rest
        return arr[0] if arr[0] > sub_max else sub_max

d = [2, 4, 5]
print(my_max(d))  # Output: 5
