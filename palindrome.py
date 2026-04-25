# Check whether a number is Palindrome or not
def palindrome(n):
    if n == reversed(n):
        return palindrome
    else:
        return not palindrome 
    
n = int(input("enter the numbers"))
print(palindrome(n))