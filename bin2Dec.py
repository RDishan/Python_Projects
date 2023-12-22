while True:
    UserValue = input("Enter a binary number to convert to decimal: ")
    
    if len(UserValue) <= 8:
        if all(bit in ('0', '1') for bit in UserValue):
            break
        else:
            print(f"Invalid entry. Please only enter 0s and 1s.")
    else:
        print("Invalid number entered. Please re-enter a valid binary number with 8 or fewer digits")

BinaryNum =  list(UserValue) 
BinaryNum.reverse()

length = len(UserValue)
sum = 0

for index in range(length):
     sum = sum + 2**index *int(BinaryNum[index])

print (f"Decimal equivalent of the given binary number is : {sum}")

