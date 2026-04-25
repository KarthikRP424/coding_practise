# # Factorial (recursion)

# def factorial(n):
#     if n ==1:
#         return 1
#     return n * factorial(n-1)

# n = int(input("enter the number: "))
# print("the factorial number is ",factorial(n))

def fibonacci(n):
    a,b = 0,1
    
    for i in range(n):
        print(a,end="")
        next = a+b
        a = b
        b = next
        
n = int(input("enter the number: "))
fibonacci(n)
