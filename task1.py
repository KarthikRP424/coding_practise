# Reverse a number without converting to string
def reverse_num(n):
    reverse = 0
    while n>0:
        digit = n%10
        reverse = reverse * 10 + digit
        n = n//10
        
    return reverse

n = int(input("enter the number"))
print(reverse_num(n))