import random
userVal = -1

ranVal = random.randint(1 , 100)

print("\nGUESS THE RANDOM NUMBER BETWEEN 1 TO 100 =>")

while userVal != ranVal:
    userVal = int(input("\nEnter a number : "))

    if userVal == ranVal :
        print("Congratulations you WON the game!")
    elif userVal < ranVal :
        print("Your number is Smaller...")
    else: 
        print("Your number is Greater...")