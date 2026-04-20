def fibonacci(n):
    if n < 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    if n ==13:
        print("the number is in fibonacci")
    else: print("there is no value")
        
n = int(input("enter the number"))
print(fibonacci(n))