# Level 1: Warm-up (must do)

# Problem:
# Given an array, find the second largest element without sorting.

# 👉 Example:
# [10, 5, 8, 20, 15] → Output: 15
def sec_lar(arr):
    largest_max = 0
    second_max = 0
    for i in range(0,len(arr)):
        if arr[i] > largest_max:
            second_max = largest_max
            largest_max = arr[i]
        elif arr[i] > second_max and arr[i] != largest_max:
            second_max = arr[i]
    return second_max

print(sec_lar([2,4,6,15,9]))
                