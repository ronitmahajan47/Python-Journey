print("Swapping 2 variables =>")
a = int(input("Enter the 1st variable: "))
b = int(input("Enter the 2nd variable: "))
print("BEFORE SWAPPING:\na = ",a,"b = ",b)

a, b = b, a

print("AFTER SWAPPING:\na = ",a,"b = ",b)