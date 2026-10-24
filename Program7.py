import json
def process_students(data):
    for student in data:
        if student["marks"] >= 40:
            student["status"] = "PASS"
        else:
            student["status"] = "FAIL"

        yield student

text = input("Enter student JSON: ")

students = json.loads(text)

print("\nProcessed Students:")

for student in process_students(students):
    print(student)