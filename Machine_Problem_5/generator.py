numbers = [63, 52, 10, 42, 32, 17, 60, 45, 47,
           39, 71, 55, 41, 95, 70, 48, 42, 32, 13, 35]


def print_even(numbers):
    return sum(1 for num in numbers if num % 2 == 0)

def print_odd(numbers):
    count = 0
    for num in numbers:
        if num % 2 != 0:
            count += 1
    return count


even = print_even(numbers)
print(f"Number of even numbers: {even}")

odd = print_odd(numbers)
print(f"Number of odd numbers: {odd}")
