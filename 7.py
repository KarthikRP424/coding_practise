def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
    
a = int(input("enter the a value"))
b = int(input("enter the b value"))
c = int(input("enter the c value"))
print(f"the greatest value is {greatest(a,b,c)}")