# Find the second largest element in an array.
# Example:
# Input: [10, 20, 4, 45, 99]
# Output: 45
arr = list(map(int,input("enter the number of eliments")))
largest = arr[0]
second_largest = arr[0]
for i in arr:
    if i > largest:
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        second_largest = i
print("the second largest value is",second_largest)