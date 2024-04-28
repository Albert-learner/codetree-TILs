N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

total_line = [0] * 100
for x, y in lines:
    for i in range(x, y + 1):
        total_line[i] += 1

answer = "No"
for x, y in lines:
    for i in range(x, y + 1):
        total_line[i] -= 1

    if N - 1 in total_line:
        answer = "Yes"
        break

    for i in range(x, y + 1):
        total_line[i] += 1

print(answer)