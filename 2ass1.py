# 4. Count Vowels and Consonants
# Problem:
# Given a string, count number of vowels and consonants.
# Example:
# Input: "hello"
# Output: Vowels: 2, Consonants: 3
text = input("enter the charecter:")
vowels = "aeiouAEIOU"
#consonants = "bcdfghjklmnpqrstvwxyz"
count1=0
count2=0
for ch in text:
    if ch in vowels:
        count1 +=1
    else:   
    # elif ch.isalpha():
        count2 +=1
print("the vowels is",count1)
print("the consonants",count2)
    