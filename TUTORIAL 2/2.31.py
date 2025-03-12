from collections import Counter

def remove_duplicates(lst):
    element_count = Counter(lst)
    
    result = [elem for elem in lst if element_count[elem] == 1]
    
    return result

user_input = input("Enter a list of numbers separated by space: ")
numbers = list(map(int, user_input.split()))

result = remove_duplicates(numbers)

print("List after removing all duplicates (no copies kept):", result)
