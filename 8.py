list = []
i = 0
num = int(input("Enter total number of elements in your list: "))

while i<num :
    list.append(input(f"Enter your DATA {i+1} = "))
    i += 1

temp = list.copy()
temp.reverse()

if list == temp :
    print("Your List is a PALINDROME")
else :
    print("Your List is not a PALINDROME")