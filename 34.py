#Checking greatest of all number

myList = []

num = int(input("\nEnter total number of Data to compare : "))
for i in range(num):
    myList.append(float(input(f"Enter DATA {i+1} = ")))

if num == 0:
    print("\nYour list can't contain 0 elements.")
else:
    greatest = myList[0]

    for i in range(1, num):
        if greatest < myList[i]:
            greatest = myList[i]

    print("\nYour List = ", myList)
    print("Greatest Value = ", greatest)