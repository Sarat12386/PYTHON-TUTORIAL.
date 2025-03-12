import re

def check_password_validity(password):
    if len(password) < 8:
        return False
    
    if not re.search("[a-z]", password):
        return False
    
    if not re.search("[A-Z]", password):
        return False
    
    if not re.search("[0-9]", password):
        return False
    
    if not re.search("[@#$%^&+=]", password):
        return False
    
    return True

password = input("Enter a password: ")

if check_password_validity(password):
    print("Password is valid.")
else:
    print("Password is invalid. It must contain:")
    print("- At least 8 characters.")
    print("- At least one lowercase letter.")
    print("- At least one uppercase letter.")
    print("- At least one digit.")
    print("- At least one special character (@, #, $, %, ^, &, +, =).")
