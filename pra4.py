# Find the maximum number using Linear Search logic

def max_number(arr,length):
    max_num = arr[0]
    
    for i in range(1,length):
        if arr[i] > max_num:
            max_num = arr[i]
            
    return max_num

arr = [11,22,33,44,55,66]

length = len(arr)

maximum = max_number(arr,length)
print("the maximum number is",max_number(arr,length))