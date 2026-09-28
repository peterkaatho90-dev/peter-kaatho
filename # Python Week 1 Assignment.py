# Python Week 1 Assignment
# Simple Student Grade Calculator

print("===== Student Grade Calculator =====")

name = input("Enter your name: ")
marks = float(input("Enter your marks: "))

if marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "E"

print("\n===== Result =====")
print(f"Student Name: {name}")
print(f"Marks: {marks}")
print(f"Grade: {grade}")
print(f"Hello {name}, your grade is {grade}.")