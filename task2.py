# reverse the number using string
num = input("enter the number: ")
reverse = num[::-1]

print("the reverse number is",reverse)

# reverse the number without using the string

def reverse_num(n):
    reverse = 0
    if n==0:
        return 0
    while n>0:
        digit = n%10
        reverse = reverse * 10 + digit
        n = n//10
        
    return reverse

n = int(input("enter the number:"))
print("the reversed number is ",reverse_num(n))