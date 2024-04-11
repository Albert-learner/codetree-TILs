N, M, K = map(int, input().split())
students = {n: 0 for n in range(1, N + 1)}
penalties = [int(input()) for _ in range(M)]

for penalty in penalties:
    if penalty in students:
        students[penalty] += 1

answer = -1
for student, penalty in students.items():
    if penalty >= K:
        answer = student

print(answer)