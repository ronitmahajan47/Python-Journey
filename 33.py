#Concatenation of 2 Lists

myList1 = []
myList2 = []

size = int(input("\nEnter the size of your 1st List : "))

for i in range(size) :
    myList1.append(int(input(f"Enter DATA {i + 1} = ")))

size = int(input("\nEnter the size of your 2nd List : "))

for i in range(size) :
    myList2.append(int(input(f"Enter DATA {i + 1} = ")))

print("\nBefore concatenating =>")
print("List 1 = ",myList1,"\nList 2 = ",myList2)

myList3 = myList1 + myList2
print("\nAfter concatenating =>")
print(myList3)
