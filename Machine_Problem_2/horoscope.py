month = int(input("Please enter your month of birth as a number: "))
day = int(input("Please enter your day of birth as a number: "))

if 1 <= month <= 12 and 1 <= day <= 31:

    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        zodiac_sign = "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        zodiac_sign = "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        zodiac_sign = "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        zodiac_sign = "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        zodiac_sign = "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        zodiac_sign = "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        zodiac_sign = "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        zodiac_sign = "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        zodiac_sign = "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        zodiac_sign = "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        zodiac_sign = "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        zodiac_sign = "Capricorn"
    else:
        zodiac_sign = "Invalid date"

    if zodiac_sign != "Invalid date":
        print(f"You are a {zodiac_sign}")
    else:
        print("The date entered is not valid.")
else:
    print("The date entered is not valid.")
