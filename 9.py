rem = []
hexa_alpha = {
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F",
}

while True:
    print("="*30)
    print("1. DECIMAL TO BINARY")
    print("2. DECIMAL TO OCTAL")
    print("3. DECIMAL TO HEXADECIMAL")
    print("4. Exit\n")
    
    temp = decimal = int(input("Enter a Whole Decimal Number: "))
    choise = int(input("Enter your Choice (1 to 4): "))

    if choise == 1 :
        while temp != 0:
            rem.append(temp % 2)
            temp //= 2

        rem.reverse()
        print("Binary Value = ", end="")
        for num in rem:
            print(num, end="")
        print("\n")
    elif choise == 2:
        while temp != 0:
            rem.append(temp % 8)
            temp //= 8
    
        rem.reverse()
        print("Octal Value = ",end="")
        for num in rem:
            print(num, end="")
        print("\n")
    elif choise == 3:
        while temp != 0:
            curr = temp % 16
            temp //= 16
            if curr >= 10:
                curr = hexa_alpha[curr]

            rem.append(curr)
        
        rem.reverse()
        print("Hexadecimal Value = ",end="")
        for num in rem:
            print(num, end="")
        print("\n")
    else:
        break