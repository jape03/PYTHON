def largestItem():
    numbers = input("Enter numbers: ")
    num_strings = numbers.split()
    num_list = []
    for num in num_strings:
        num_list.append(int(num))
    largest_num = max(num_list)
    print(f"The largest number is {largest_num}")

largestItem()
