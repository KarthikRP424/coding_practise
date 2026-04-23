import random

'''
-1 = snake
1 = water
0 = gun
'''

computer = random.choice([-1, 1, 0])

youStr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

youDict = {"s": -1, "w": 1, "g": 0}
reverseDict = {-1: "snake", 1: "water", 0: "gun"}

if youStr not in youDict:
    print("Invalid input!")
    exit()

you = youDict[youStr]

print(f"Your choice: {reverseDict[you]}")
print(f"Computer choice: {reverseDict[computer]}")

if computer == you:
    print("Draw")
else:
    if computer == -1 and you == 1:
        print("You Lose")
    elif computer == -1 and you == 0:
        print("You Win!")
    elif computer == 1 and you == -1:
        print("You Win!")
    elif computer == 1 and you == 0:
        print("You Lose!")
    elif computer == 0 and you == -1:
        print("You Lose")
    elif computer == 0 and you == 1:
        print("You Win!")
    else:
        print("Something went wrong")