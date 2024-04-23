N, B = map(int, input().split())
gifts_info = [list(map(int, input().split())) for _ in range(N)]
gifts_info.sort()

max_students = 0
for i in range(N):
    prices = gifts_info[i][1]
    for j in range(N):
        if i == j:
            prices += gifts_info[j][0] // 2
        else:
            prices += gifts_info[j][0]

        if prices <= B:
            max_students = max(max_students, j + 1)
        else:
            break

print(max_students)