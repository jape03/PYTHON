length_input = input("Enter length value:")
width_input = input("Enter the width of the rectangle:")


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        try:
            length = int(self.length)
            width = int(self.width)
            if length <= 0 or width <= 0:
                print("The number is not a positive integer.")
            else:
                print(f"The Area of the Rectangle is: {length * width}")
        except ValueError:
            print("The input must be a whole number.")


rectangle = Rectangle(length_input, width_input)
rectangle.area()
