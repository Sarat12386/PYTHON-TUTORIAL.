def is_palindrome(input_string):
    input_string = input_string.replace(" ", "").lower()
    
    left = 0
    right = len(input_string) - 1
    
    while left < right:
        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1
    
    return True

input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print(f"'{input_string}' is a palindrome.")
else:
    print(f"'{input_string}' is not a palindrome.")
