numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even += 1  
    else:
        odd += 1  

print(f"Number of even numbers: {even}")
print(f"Number of odd numbers: {odd}")
