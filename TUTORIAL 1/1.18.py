def is_armstrong(number):
    num_str = str(number)
    n = len(num_str)      
    sum_of_powers = sum(int(digit) ** n for digit in num_str)
    
    return sum_of_powers == number

num = int(input("Enter a number: "))

if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
