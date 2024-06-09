length_input = input("Enter length value:")
width_input = input("Enter the width of the rectangle:")

class Rectangle:
    def area(length, width):
        try:
            length = int(length)
            width = int(width)
            if length <= 0 or width <= 0:
                print("The number is not a positive integer.")
            else:
                print(f"The Area of the Rectangle is: {length * width}")
        except ValueError:
            print("The input must be a whole number.")
            
Rectangle.area(length_input, width_input)
