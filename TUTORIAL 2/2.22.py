def remove_words_from_string():
    input_string = input("Enter the string: ")
    
    words_to_remove = input("Enter words to remove (separated by space): ").split()
    
    words = input_string.split()
    
    result_words = [word for word in words if word not in words_to_remove]
    
    result_string = " ".join(result_words)
    
    print("String after removal:", result_string)

remove_words_from_string()
