def max_number(arr, length):
    max_num = arr[0]
    second_max = arr[0]

    for i in range(1, length):
        if arr[i] > max_num:
            second_max = max_num   # old max becomes second max
            max_num = arr[i]
        elif arr[i] > second_max and arr[i] != max_num:
            second_max = arr[i]

    return second_max


arr = [11, 22, 33, 44, 55, 66]
length = len(arr)

second_maximum = max_number(arr, length)
print("The second maximum number is", second_maximum)