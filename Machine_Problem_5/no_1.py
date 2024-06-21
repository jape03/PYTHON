numbers = [63, 52, 10, 42, 32, 17, 60, 45, 47, 39, 71, 55, 41, 95, 70, 48, 42, 32, 13, 35]

def print_list(numbers):
    return numbers

def print_average(numbers):
    return sum(numbers) / len(numbers)

def print_largest_smallest(numbers):
    return max(numbers), min(numbers)

def print_second_largest_smallest(numbers):
    sorted_numbers = sorted(set(numbers))
    return sorted_numbers[-2], sorted_numbers[1]

def print_even(numbers):
    return sum(1 for num in numbers if num % 2 == 0)

def print_odd(numbers):
    return sum(1 for num in numbers if num % 2 != 0)

list = print_list(numbers)
print(f"List: {list}")

average = print_average(numbers)
print(f"Average: {average:.2f}")

largest, smallest = print_largest_smallest(numbers)
print(f"Largest: {largest}")
print(f"Smallest: {smallest}")

second_largest, second_smallest = print_second_largest_smallest(numbers)
print(f"Second Largest: {second_largest}")
print(f"Second Smallest: {second_smallest}")

even = print_even(numbers)
print(f"Number of even numbers: {even}")

odd = print_odd(numbers)
print(f"Number of odd numbers: {odd}")
