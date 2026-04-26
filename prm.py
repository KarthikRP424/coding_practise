def prime_num(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i ==0:
            return False
    return True

n = int(input("enter the number"))

if prime_num(n):
    print("the number is prime")
else:
    print("the number is not a prime")