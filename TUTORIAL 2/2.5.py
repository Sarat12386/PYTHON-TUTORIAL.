def slice_string(input_string):
    even_indices = input_string[::2]  # Characters at even indices (0, 2, 4, ...)
    odd_indices = input_string[1::2]  # Characters at odd indices (1, 3, 5, ...)
    
    return even_indices, odd_indices

input_string = input("Enter a string: ")

even_chars, odd_chars = slice_string(input_string)

print(f"Characters at even indices: {even_chars}")
print(f"Characters at odd indices: {odd_chars}")
