# Second Problem

width = int(input("Please enter the width of the field in feet: "))
length = int(input("Please enter the length of the field in feet: "))

sqFeetPerAcre = width * length / 43560

print(f"The area of the field in acres is {sqFeetPerAcre} acres.")