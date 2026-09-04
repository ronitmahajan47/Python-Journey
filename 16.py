a,b,c = map(float , input("\nEnter three different numbers seperated by ',' : ").split(",")) 

if b < a > c :
    print(a," is the greatest")
elif b > c :
    print(b," is the greatest")
else :
    print(c," is the greatest")