number = int(input("Enter number: "))

def digital_root(n):
    if n == 0:
        return 0
    else:
        return 1 + (n - 1) % 9

result = digital_root(number)

print(f"The digital root of {number} is {result}")
