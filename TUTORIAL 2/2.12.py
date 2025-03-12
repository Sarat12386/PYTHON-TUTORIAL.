def decimal_to_binary(decimal_number):
    if decimal_number < 0:
        return "Please enter a non-negative integer."
    
    binary_number = bin(decimal_number)[2:]
    return binary_number

decimal_number = int(input("Enter a decimal number: "))

binary_number = decimal_to_binary(decimal_number)

print(f"The binary equivalent of {decimal_number} is {binary_number}.")
