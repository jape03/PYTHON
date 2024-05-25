count = 0

for num in range(1500, 3001):
    if num % 7 == 0 and num % 5 == 0:
        print(num, " ", end="")
        count += 1  

print("\n\nTotal numbers divisible by 7 and multiples of 5:", count)
