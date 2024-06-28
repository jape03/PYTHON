list1 = [5, 20, 15, 20, 25, 50, 20]
new_list1 = []

for num in list1:
    if num != 15:
        new_list1.append(num)
        
print(f"The list : {list1}")
print(f"The new list : {new_list1}")
