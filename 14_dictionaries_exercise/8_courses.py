courses = {}

while True:
    command = input()
    if command == "end":
        break
    course_name, student = command.split(' : ')

    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append((student))

for course_name, registered_students in courses.items():
    print(f"{course_name}: {len(registered_students)}")

    for student_name in registered_students:
        print(f"-- {student_name}")
