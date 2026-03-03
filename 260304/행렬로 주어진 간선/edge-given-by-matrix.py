n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
reach = [row[:] for row in graph]

for i in range(n):
    reach[i][i] = 1

for k in range(n):
    for i in range(n):
        if reach[i][k] == 0:
            continue

        for j in range(n):
            if reach[k][j]:
                reach[i][j] = 1

for i in range(n):
    print(*reach[i])