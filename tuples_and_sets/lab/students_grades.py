n = int(input())

grades = {}

for _ in range(n):
    name, grade = input().split()

    if name not in grades.keys():
        grades[name] = []

    grades[name].append(float(grade))

for student, student_grades in grades.items():
    result = f"{student} -> {' '.join(f'{x:.2f}' for x in student_grades)} (avg: {sum(student_grades) / len(student_grades):.2f})"
    print(result)
