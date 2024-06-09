N = int(input())
students = [list(map(int, input().split())) for _ in range(N)]

pass_students = 0
for student in students:
    avg = sum(student) // len(student)

    if avg >= 60:
        print("pass")
        pass_students += 1
    else:
        print("fail")
        print(pass_students)