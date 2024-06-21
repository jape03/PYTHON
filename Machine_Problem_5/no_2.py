numbers = [18, 19, 20]

def set(numbers):
    numbers[1] = 17
    return numbers

def add(numbers):
    numbers.extend([4, 5, 6])
    return numbers

def remove(numbers):
    numbers.pop(0)
    return numbers

def sort(numbers):
    return sorted(numbers)

def double(numbers):
    return numbers * 2

def insert(numbers):
    numbers[3] = 25
    return numbers

print(f"Original list: {numbers}")

a = set(numbers.copy())
print(f"a : {a}")

b = add(a.copy())
print(f"b : {b}")

c = remove(b.copy())
print(f"c : {c}")

d = sort(c.copy())
print(f"d : {d}")

e = double(d.copy())
print(f"e : {e}")

f = insert(e.copy())
print(f"f : {f}")
