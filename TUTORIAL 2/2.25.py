def remove_duplicates():
    user_input = input("Enter the elements separated by spaces: ")
    
    elements = user_input.split()
    
    unique_elements = list(set(elements))
    
    print("List without duplicates:", unique_elements)

remove_duplicates()
