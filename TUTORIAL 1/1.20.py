def is_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False

string = input("Enter a string: ")

if is_palindrome(string):
    print(f"'{string}' is a palindrome.")
else:
    print(f"'{string}' is not a palindrome.")
