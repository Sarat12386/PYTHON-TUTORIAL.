def separate_data_types():
    user_input = input("Enter a list of elements (integers, floats, and strings) separated by spaces: ")
    
    elements = user_input.split()
    
    integers = []
    floats = []
    strings = []
    
    for element in elements:
        try:
            int_element = int(element)
            integers.append(int_element)
        except ValueError:
            try:
                float_element = float(element)
                floats.append(float_element)
            except ValueError:
                strings.append(element)
    
    print("Integers:", integers)
    print("Floats:", floats)
    print("Strings:", strings)

separate_data_types()
