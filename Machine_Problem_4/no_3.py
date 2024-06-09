class Converter:
    def __init__(self):
        self.guide = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000,
            'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900
        }
        self.roman_guide = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
        ]

    def int_to_roman(self, value):
        if not 1 <= value <= 5000:
            return "Max Value is 5000."
        roman = ""
        for integer_value, roman_symbol in self.roman_guide:
            while value >= integer_value:
                roman += roman_symbol
                value -= integer_value
        return roman

    def roman_to_int(self, roman):
        roman = roman.upper()
        i, total = 0, 0
        while i < len(roman):
            if i + 1 < len(roman) and roman[i:i+2] in self.guide:
                total += self.guide[roman[i:i+2]]
                i += 2
            elif roman[i] in self.guide:
                total += self.guide[roman[i]]
                i += 1
            else:
                return "Invalid Roman Numeral."
        return total


while True:
    print("1. Integer to a Roman Numeral\n2. Roman Numeral to Integer\n3. Exit")
    choice = input("Enter choice: ")
    if choice == '1':
        try:
            number = int(input("Enter Integer: "))
            result = Converter.int_to_roman(number)
            print(f"Roman Numeral: {result}")
        except ValueError:
            print("Invalid integer.")
    elif choice == '2':
        roman = input("Enter Roman Numeral: ")
        result = Converter.roman_to_int(roman)
        print(f"Integer: {result}")
    elif choice == '3':
        print("Bye")
        break
    else:
        print("Invalid choice.")
