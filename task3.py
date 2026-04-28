# Count number of digits using loop (no len, no string)
def count_digit(num):
    count = 0
    
    if num == 0:
        return 0
    
    while num>0:
        num = num //10
        count +=1
    return count
num = int(input("enter the digit"))
print(count_digit(num))