letter = input("Enter grade: ")

if letter == "A+":
    grade_points = 4.0
elif letter == "A":
    grade_points = 4.0
elif letter == "A-":
    grade_points = 3.7
elif letter == "B+":
    grade_points = 3.3
elif letter == "B":
    grade_points = 3.0
elif letter == "B-":
    grade_points = 2.7
elif letter == "C+":
    grade_points = 2.3
elif letter == "C":
    grade_points = 2.0
elif letter == "C-":
    grade_points = 1.7
elif letter == "D+":
    grade_points = 1.3
elif letter == "D":
    grade_points = 1.0
elif letter == "F":
    grade_points = 0.0
else:
    grade_points = None

if grade_points is not None:
    print(f"For this grade,you will receive a grade points of {grade_points}")
else:
    print("Invalid letter grade entered.")
