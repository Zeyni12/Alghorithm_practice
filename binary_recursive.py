def binary_search(arr, target, low, high):
    if low > high:  # Base case: target not found
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, low, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, high)

# Example
data = [1, 3, 5, 7, 9, 11]
target = 7
result = binary_search(data, target, 0, len(data) - 1)

print(result)  # Output: 3 (index of 7)
