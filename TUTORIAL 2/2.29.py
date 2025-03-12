def set_operations():
    set1 = set(map(int, input("Enter elements of the first set separated by space: ").split()))
    set2 = set(map(int, input("Enter elements of the second set separated by space: ").split()))
    
    print("\nSet 1:", set1)
    print("Set 2:", set2)

    union_result = set1.union(set2)
    print("\nUnion of Set 1 and Set 2:", union_result)

    intersection_result = set1.intersection(set2)
    print("Intersection of Set 1 and Set 2:", intersection_result)

    difference_result = set1.difference(set2)
    print("Difference (Set 1 - Set 2):", difference_result)

    symmetric_difference_result = set1.symmetric_difference(set2)
    print("Symmetric Difference between Set 1 and Set 2:", symmetric_difference_result)

set_operations()
