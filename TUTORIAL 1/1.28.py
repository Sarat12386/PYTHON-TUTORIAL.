def sum_of_odds(lower_limit, upper_limit):
    total_sum = 0
    
    for num in range(lower_limit, upper_limit + 1):
        if num % 2 != 0:  # Check if the number is odd
            total_sum += num
    
    return total_sum

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

result = sum_of_odds(lower_limit, upper_limit)

print(f"The sum of odd numbers between {lower_limit} and {upper_limit} is: {result}")
