def letters(input):
    result = []
    for i, char in enumerate(input):
        repeated_char = char * (i + 1)
        result.append(repeated_char)
    return result

input = "abcdefghijklmnopqrstuvwxyz"
output = letters(input)

print(f"The input is {input} \n")
print(f"The output is {output}")
