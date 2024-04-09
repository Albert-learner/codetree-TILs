N = int(input())
students_input = [list(map(int, input().split()))for _ in range(N)]

students = []
for student_idx, (height, weight) in enumerate(students_input, 1):
    students.append([height, weight, student_idx])

students.sort(key = lambda x: (-x[0], -x[1], -x[2]))
for student in students:
    print(*student)