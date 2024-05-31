def odd():
    odd_numbers = []
    for num in range(4, 31):
        if num % 2 != 0:
            odd_numbers.append(num)
    print(odd_numbers)

odd()
