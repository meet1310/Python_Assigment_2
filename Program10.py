import matplotlib.pyplot as plt

n = int(input("Enter number of students: "))

names = []
marks = []

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))

    names.append(name)
    marks.append(mark)

plt.bar(names, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.savefig("dashboard.png")

plt.show()

print("Dashboard saved successfully as dashboard.png")

import matplotlib.pyplot as plt

n = int(input("Enter number of students: "))

names = []
marks = []

for i in range(n):
    name = input("Enter student name: ")
    mark = int(input("Enter marks: "))

    names.append(name)
    marks.append(mark)

plt.bar(names, marks)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.savefig("dashboard.png")

plt.show()

print("Dashboard saved successfully as dashboard.png")