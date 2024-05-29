def convert_number(number):
    decimal = str(number)

    octal = oct(number)
    
    hexadecimal = hex(number).upper().replace("X","x")
    
    binary = bin(number)

    return decimal,octal,hexadecimal,binary



if __name__=="__main__":
    decimal,octal,hexadecimal,binary = convert_number(334)

    print(decimal)
    print(octal)
    print(hexadecimal)
    print(binary)
