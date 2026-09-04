#Binary Searching -
#Note - This program can only find the FIRST OCCURENCE.

myList = []
position = []

def binarySearch(key , myList):
    low = 0
    high = size - 1

    while low <= high :
        mid = low + (high - low)//2

        if key == myList[mid] :
            position.append(mid + 1)
            return

        elif key < myList[mid] :
            high = mid - 1
        else :
            low = mid + 1


size = int(input("\nEnter the size of list : "))

for i in range(size) :
    myList.append(int(input(f"Enter DATA {i + 1} = ")))

myList.sort()

print("\nList after sorting : ")
print(myList)

key = int(input("\nEnter your key to search : "))
binarySearch(key , myList)


if position:
    print("\nKey found at position = ", position)
else :
    print("\nKey not found!")