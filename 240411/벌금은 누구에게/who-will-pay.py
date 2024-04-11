N, M, K = map(int, input().split())
students = [[n, 0] for n in range(1, N + 1)]
penalties = [int(input()) for _ in range(M)]

answer = -1
for penalty in penalties:
    if penalty in list(zip(*students))[0]:
        idx = list(zip(*students))[0].index(penalty)
        students[idx][1] += 1

    if students[idx][1] >= K:
        answer = students[idx][0]
        break

print(answer)