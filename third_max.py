def sec_lar(arr):
    largest_max = float('-inf')
    second_max = float('-inf')
    third_max = float('-inf')
    for i in range(0,len(arr)):
        if arr[i] > largest_max:
            second_max = largest_max
            largest_max = arr[i]
        elif arr[i] > second_max and arr[i] != largest_max:
            third_max = second_max
            second_max = arr[i]
        elif arr[i] > third_max and arr[i] != second_max:
            third_max = arr[i]
    return {
        'largest' : largest_max,
        'second' : second_max,
        'third' : third_max
    }

print(sec_lar([2,4,6,15,9]))
                