#Program to find if the list is empty or not

myList = []
length = int(input("\nEnter the length of your List : "))

for i in range(length):
    myList.append(input(f"Enter DATA {i + 1} = "))

if len(myList) == 0 :
    print("\nYour list is Empty...")
else :
    print("\nYour list is a none empty list...")