radius_input = input("Enter the radius of the circle:")

class Circle:
    def area_perimeter(radius):
        try:
            radius = int(radius)
            if radius <= 0:
                print("The radius is not a positive number.")
            else:
                area = 3.14159 * radius * radius 
                perimeter = 2 * 3.14159 * radius
                print(f"The Area of the Circle is: {area:.2f}")
                print(f"The Perimeter of the Circle is: {perimeter:.2f}")
        except ValueError:
            try:
                float(radius) 
                print("The radius must be a whole number.")
            except ValueError:
                print("The input must be a Positive number:")

Circle.area_perimeter(radius_input)
