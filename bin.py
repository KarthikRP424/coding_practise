def binary_search(arr, key, n): #binary search method
    left = 0
    right = n - 1

    while left <= right:
        mid = (left + right) // 2

        if key > arr[mid]:
            left = mid + 1
        elif key < arr[mid]:
            right = mid - 1
        else:
            return mid

    return -1


arr = [11, 12, 22, 33, 44]   # sorted array
key = 22
n = len(arr)

result = binary_search(arr, key, n)

if result != -1:
    print("the key value found at index", result)
else:
    print("not found")