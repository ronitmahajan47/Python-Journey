#Insertion sorting

myList = []
size = int(input("\nEnter the size of list : "))

for i in range(size) :
    myList.append(int(input(f"Enter DATA {i + 1} = ")))

print("\nList before sorting : ",myList)

for i in range(1 , size):
    key = myList[i]
    j = i-1

    while j>0 :
        if key < myList[j] :
            myList[j] , myList[key] = myList[key] , myList[j]
        j -= 1

print("List after sorting : ",myList)