def nextPrimeList():
    while True:
        try:
            n = input("Enter a positive number: ")
            n = float(n)
            if n.is_integer():
                n = int(n)
            else:
                print("The number should be a whole value.")
                continue

            if n < 0:
                print("The number is not a positive integer.")
                continue

            current_number = n + 1
            while True:
                if current_number > 1:
                    if current_number <= 3:
                        print(f"The first prime greater than the number entered is: {current_number}")
                        return
                    if current_number % 2 == 0 or current_number % 3 == 0:
                        current_number += 1
                        continue
                    i = 5
                    while i * i <= current_number:
                        if current_number % i == 0 or current_number % (i + 2) == 0:
                            break
                        i += 6
                    else:
                        print(f"The first prime greater than the number entered is: {current_number}")
                        return
                current_number += 1

        except ValueError:
            print("Please enter a valid number.")

nextPrimeList()
