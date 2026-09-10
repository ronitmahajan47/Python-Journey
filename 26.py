length = int(input("Enter the length of the pattern: "))

for i in range (length+1):
    for j in range(i):
        print("*",end="")
    print("\n")