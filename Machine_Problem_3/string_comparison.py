string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

def xyz_diff(string1, string2):
    i = 0
    while i < len(string1) and i < len(string2):
        if string1[i] != string2[i]:
            return i + 1 
        i += 1
    
    if len(string1) != len(string2):
        return i + 1  
    
    return -1

result = xyz_diff(string1, string2)
print(result)
