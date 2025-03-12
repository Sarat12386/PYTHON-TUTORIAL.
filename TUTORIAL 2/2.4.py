def replace_spaces(input_string):
    if ' ' in input_string:
        return input_string.replace(" ", "*")
    else:
        return input_string

input_string = input("Enter a string: ")

output_string = replace_spaces(input_string)
print(f"Modified string: {output_string}")
