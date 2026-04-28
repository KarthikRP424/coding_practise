# sum of digit using loop 
def digit_sum(num):
    total = 0
    if num ==0:
        return 0
    while num>0:
        digit = num%10
        total += digit
        num = num//10
    return total

n = int(input("enter the number"))
print("the sum  digit is",digit_sum(n))