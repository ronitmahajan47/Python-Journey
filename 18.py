#Bubble sorting

myList = []
size = int(input("\nEnter the size of list : "))

for i in range(size) :
    myList.append(int(input(f"Enter DATA {i + 1} = ")))

print("\nList before sorting : ",myList)

for i in range(size-1):
    for j in range(size-i-1):
        if myList[j+1] < myList[j] :
            myList[j+1] , myList[j] = myList[j] , myList[j+1]

print("List after sorting : ",myList)