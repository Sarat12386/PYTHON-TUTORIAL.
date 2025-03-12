def remove_duplicates(lst):
    return list(set(lst))

user_input = input("Enter a list of numbers separated by space: ")
numbers = list(map(int, user_input.split()))

result = remove_duplicates(numbers)

print("List after removing duplicates:", result)
