length = int(input("Enter the length of the pattern : "))

for i in range(length+1):
    for j in range(1,i+1):
        print(j,end="") 
    print("\n")