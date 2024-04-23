N, B = map(int, input().split())
gifts_info = [list(map(int, input().split())) for _ in range(N)]

max_students = 0
total_prices = 0
possible_students = 0
for i in range(N):
    half_student = gifts_info[i]
    total_prices += half_student[0] // 2 + half_student[1]
    possible_students += 1
    for j in range(N):
        if i == j:
            continue

        total_prices += (gifts_info[j][0] + gifts_info[j][1])
        possible_students += 1
        if total_prices <= B:
            max_students = max(max_students, possible_students)

print(max_students)