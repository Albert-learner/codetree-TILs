n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
INF = 10**18

u = [0] * (n + 1)
v = [0] * (n + 1)
p = [0] * (n + 1)
way = [0] * (n + 1)

for i in range(1, n + 1):
    p[0] = i
    j0 = 0
    minv = [INF] * (n + 1)
    used = [False] * (n + 1)

    while True:
        used[j0] = True
        i0 = p[j0]
        delta = INF
        j1 = 0

        for j in range(1, n + 1):
            if not used[j]:
                cur = -grid[i0 - 1][j - 1] - u[i0] - v[j]

                if cur < minv[j]:
                    minv[j] = cur
                    way[j] = j0

                if minv[j] < delta:
                    delta = minv[j]
                    j1 = j

        for j in range(n + 1):
            if used[j]:
                u[p[j]] += delta
                v[j] -= delta
            else:
                minv[j] -= delta

        j0 = j1

        if p[j0] == 0:
            break

    while True:
        j1 = way[j0]
        p[j0] = p[j1]
        j0 = j1

        if j0 == 0:
            break

answer = 0

for j in range(1, n + 1):
    row = p[j]
    col = j
    answer += grid[row - 1][col - 1]

print(answer)