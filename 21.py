#fibonacci series

a = 0
b = 1
length = int(input("\nEnter the length of the Fibonacci series : "))

for i in range(length) :
    print(a,end="  ")
    c = a + b
    a = b
    b = c