# find the largest number using loop

def largest_digit(n):
    largest = 0
    
    while n >0:
        digit = n%10
        if digit > largest:
            largest = digit
            
        n = n//10
    return largest
n = int(input("Enter number: "))
print("Largest digit is:", largest_digit(n))