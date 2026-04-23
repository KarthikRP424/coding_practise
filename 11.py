# Write a python function to print multiplication table of a given number.
def multiplication(n):
    if n==0:
        return 
    for i in range(1,11):
        print(n ,"*", i,"=",n*i)
n = int(input("enter the number"))
print(multiplication(n))
