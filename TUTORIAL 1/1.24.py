def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

for num in range(100, 1000):
    if sum_of_digits(num) % 9 == 0:
        print(num, end=" ")
