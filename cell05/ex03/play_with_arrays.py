original_array = [2, 8, 9, 48, 8, 22, -12, 2]


new_array = []
for x in original_array:
    if x > 5 and (x + 2) not in new_array:
        new_array.append(x + 2)


print("Original array:", original_array)
print("New array with 2 added to values greater than 5 and no duplicates:", new_array)