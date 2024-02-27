# Binary Search 
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

# Example usage 
arr = [11, 12, 22, 25, 34, 64, 90]
x = 22
result = binary_search(arr, x)
print('Element found at index: ', result)