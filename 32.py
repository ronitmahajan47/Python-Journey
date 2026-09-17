#Program to slice a list

myList = []
length = int(input("\nEnter the length of your List : "))

for i in range(length):
    myList.append(input(f"Enter DATA {i + 1} = "))

slicePos = int(input("\nEnter the position of the list you wanna slice : "))

print(myList[:slicePos])