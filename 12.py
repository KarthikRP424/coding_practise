def linear_search(arr,length,item):
    for i in range(0,length):
        if arr[i]== item:
            return i
    return -1
arr = [12,34,55,40,66,77]
item = int(input("enter the value what you want"))
length =len(arr)
result = linear_search(arr,length,item)

if result == -1:
    print("the {} is not found".format(item))
else:
    print("the {} is found at {} index".format(item, result))