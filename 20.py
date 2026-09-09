count = 0
num = int(input("Enter a number : "))

for i in range(1 ,num + 1) :
    if num % i == 0 :
        count += 1

if count == 2 :
    print(num,"is a Prime Number.")
else :
    print(num,"is not a Prime Number.")