def reverse_number(number):
    reversed_number = 0
    while number > 0:
        digit = number % 10  
        reversed_number = reversed_number * 10 + digit 
        number = number // 10  
    return reversed_number

num = int(input("Enter a number: "))

reversed_num = reverse_number(num)
print(f"The reversed number is: {reversed_num}")
