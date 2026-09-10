#Factorial using recursive function

num = int (input("\nEnter a number : "))

def factorial(num) :
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

fact = factorial(num)
print("Factorial = ",fact)