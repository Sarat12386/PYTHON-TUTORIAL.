
def reverse_halves(input_string):
    mid = len(input_string) // 2

    first_half = input_string[:mid]
    second_half = input_string[mid:]

    reversed_first_half = first_half[::-1]
    reversed_second_half = second_half[::-1]

    return reversed_first_half + reversed_second_half

input_string = input("Enter a string: ")

result_string = reverse_halves(input_string)

print(f"String after reversing the first and second halves separately: {result_string}")
