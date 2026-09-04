#Checking Armstrong number

temp = num = int(input("\nEnter a number : "))
result = 0

while temp!= 0:
    r = temp % 10
    result += (r ** len(str(num)))
    temp //= 10

if result == num :
    print("Your number is an Armstrong number.")
else :
    print("Your number is not an Armstrong number.")