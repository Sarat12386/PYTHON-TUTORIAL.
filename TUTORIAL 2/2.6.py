def remove_substring(input_string, substring):
    return input_string.replace(substring, "")

input_string = input("Enter a string: ")
substring = input("Enter the substring to remove: ")

result_string = remove_substring(input_string, substring)

print(f"String after removing all occurrences of the substring: {result_string}")
