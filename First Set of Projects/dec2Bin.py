Uservalue = int(input("Enter a decimal number to convert to binary: "))

#Ask the user for input and convert it into an integer.

decimal_number = Uservalue 
binary_list = []
index = 0

while Uservalue >= 1: 
    bit = Uservalue%2
    binary_list.append(bit)
    index +=1
    Uservalue = Uservalue//2

binary_list.reverse()

binary_string = ''.join(map(str,binary_list))
print(f"\nThe binary number of decimal {decimal_number} is equal to :{binary_string}\n")    



