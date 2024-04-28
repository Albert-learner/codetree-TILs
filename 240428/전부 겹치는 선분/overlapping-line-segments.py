N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

total_line = [0] * 101

for x, y in lines:
    for i in range(x, y + 1):
        total_line[i] += 1

if N in total_line:
    print("Yes")
else:
    print("No")