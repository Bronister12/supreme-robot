# Bubble sort:
# A simple sorting alghorithm that repeatedly steps through
# the list, compares adjastment elements, and swaps them if 
# they are in the wrong order.
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # Swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print('Sorted array is: ', sorted_arr)