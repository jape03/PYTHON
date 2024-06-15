class Student:
    def __init__(self, name, course, marks):
        self.student_name = name
        self.student_course = course
        self.student_marks = marks

student = Student("John Paul L. Besagas", "BSCSSE", 95)

print("Original values:")
print(f"Name: {student.student_name}")
print(f"Course: {student.student_course}")
print(f"Marks: {student.student_marks} \n")

student.student_name = input("Enter new name: ")
student.student_course = input("Enter new course: ")
student.student_marks = int(input("Enter new marks: ")) 

print("\nModified values:")
print(f"Name: {student.student_name}")
print(f"Course: {student.student_course}")
print(f"Marks: {student.student_marks}")
