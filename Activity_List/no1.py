list2 = ["Mike", "", "Emma", "Michelle", "", "Jason"]
new_list2 = []

for name in list2:
    if name != "":
        new_list2.append(name)
        
print(f"The list : {list2}")
print(f"The new list : {new_list2}")
