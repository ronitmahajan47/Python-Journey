#Linear Searching -

myList = []
position = []
count = 0

size = int(input("\nEnter the size of list : "))

for i in range(size) :
    myList.append(int(input(f"Enter DATA {i + 1} = ")))

key = int(input("Enter your key to search : "))

for num in myList :
    if key == num :
        position.append(count + 1)
        count +=1
    else :
        count += 1

if position:
        print("Key found at position = ", position)
else :
        print("Key not found!")