for i in range(20):
    name = input("Enter student name: ")
    marks = int(input("Enter marks: "))

    if marks >= 90:
        grade = "Distinction"
    elif marks >= 75:
        grade = "First Division"
    elif marks >= 60:
        grade = "Second Division"
    elif marks >= 35:
        grade = "Third Division"
    else:
        grade = "Fail"

    print(name, "got", grade)
