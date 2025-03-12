def binary_to_decimal(binary_number):
    if not all(char in '01' for char in binary_number):
        return "Please enter a valid binary number."
    
    decimal_number = int(binary_number, 2)  # 2 is the base for binary
    return decimal_number

binary_number = input("Enter a binary number: ")

decimal_number = binary_to_decimal(binary_number)

print(f"The decimal equivalent of binary {binary_number} is {decimal_number}.")
