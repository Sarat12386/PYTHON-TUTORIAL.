def remove_odd_index_characters(input_string):
    result = ''.join([input_string[i] for i in range(len(input_string)) if i % 2 == 0])
    return result

input_string = input("Enter a string: ")

output_string = remove_odd_index_characters(input_string)

print(f"String after removing characters at odd indices: {output_string}")
