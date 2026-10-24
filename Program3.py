# Student Course Analytics - Python Only

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = int(input("Enter Marks: "))

    students.append((id, name, course, marks))

print("\n--- Student Details ---")

students.sort(key=lambda x: x[3], reverse=True)

for row in students:
    print(row)

course = input("\nEnter course to search: ")

print("\n--- Course Students ---")

found = False

for row in students:
    if row[2].lower() == course.lower():
        print(row[1], row[2], row[3])
        found = True

if not found:
    print("No students found for this course.")