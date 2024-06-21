numbers = [30, 7, 30, 2, 88, 44, 60, 40, 1, 53, 100, 72, 86, 64, 40, 85, 3, 19, 63, 84, 17, 31, 95, 84, 99, 60, 85, 74, 65, 38, 43, 80, 39, 70, 8, 21, 32, 68, 64, 55, 88, 84, 49, 68, 70, 98, 21, 51, 3, 97]

def replace(numbers):
    replaced = 0
    not_replaced = 0
    new_list = []
    for num in numbers:
        if num > 10:
            new_list.append(666)
            replaced += 1
        else:
            new_list.append(num)
            not_replaced += 1
    return new_list, replaced, not_replaced

print(f"List: {numbers} \n")

new_list, replaced, not_replaced = replace(numbers)

print(f"New list: {new_list} \n")
print(f"Number of entries replaced: {replaced}")
print(f"Number of entries not replaced: {not_replaced}")
