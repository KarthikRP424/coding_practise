def palindrome(n):
    if n == 0:
        return 0
    original = n
    reverse = 0
    
    while n > 0:
        digit = n %10
        reverse = reverse * 10 + digit
        n = n//10
    if original == reverse:
        print("the number is palindrome")
    else:
        print("not a palindrome")

n = int(input("enter the number"))
print(palindrome(n))
