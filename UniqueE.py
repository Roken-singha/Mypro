original_list = [int(x) for x in input("Enter list elements separated by space: ").split()]
unique_list = list(set(original_list))
print("Unique elements:", unique_list)
