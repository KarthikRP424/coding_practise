def factorial(n):
    if n==1 or n==0:
        return 1
    return (n-1)+(n-2)
n = int(input("enter the number is:"))
print(f"the factorial is ",factorial(n))