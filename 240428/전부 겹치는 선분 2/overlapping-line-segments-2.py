N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

total_line = [0] * 101
for x, y in lines:
    for i in range(x, y + 1):
        total_line[i] += 1

cnts = 0
for i in range(101):
    if total_line[i] == N - 1:
        cnts += 1

if cnts > 0:
    print("Yes")
else:
    print("No")