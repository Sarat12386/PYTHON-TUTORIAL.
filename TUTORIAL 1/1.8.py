def sum_of_digits(number):
    total = 0
    
    while number > 0:
        total += number % 10  
        number = number // 10  
    
    return total

num = int(input("Enter a number: "))

result = sum_of_digits(num)
print(f"The sum of the digits of {num} is {result}.")
