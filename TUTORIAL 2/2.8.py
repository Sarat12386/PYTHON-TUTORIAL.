def replace_substring(input_string, old_substring, new_substring):

    return input_string.replace(old_substring, new_substring)

input_string = input("Enter a string: ")
old_substring = input("Enter the substring to replace: ")
new_substring = input("Enter the new substring to replace with: ")

result_string = replace_substring(input_string, old_substring, new_substring)

print(f"String after replacement: {result_string}")
