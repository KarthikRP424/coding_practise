# ✅ Requirements:

# Given a list of integers, return:

# Sum of all elements
# Count of even numbers
# Count of odd numbers
# Largest number
# Second largest number (without using sort())
# Reverse the list (without using reverse() or slicing [::-1])

def kart(arr):
    total = 0
    even = 0
    odd = 0
    reversed_list = []
    largest = float('-inf')
    sec_largest = float('-inf')
    for num in arr:
        total +=num
        if num %2==0:
            even +=1
        else:
            odd +=1
        if num > largest:
            sec_largest = largest
            largest = num
        elif num > sec_largest and num != largest:
            sec_largest = num
            


    for num in arr:
        reversed_list.insert(0, num)
        
    return {
        'sum': total,
        'even': even,
        'odd': odd,
        'largest': largest,
        'sec__la': sec_largest ,
        'reverse': reversed_list
        
    }
        
arr = [5,24,35,40,60]
print(kart(arr))