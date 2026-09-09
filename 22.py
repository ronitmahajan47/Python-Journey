#Palindrome

temp = num = int(input("\nEnter a number : "))
result = 0

while temp!= 0:
    r = temp % 10
    result = (result * 10) + r
    temp //= 10

if result == num :
    print("Your number is a Palindrome number.")
else :
    print("Your number is not a Palindrome number.")