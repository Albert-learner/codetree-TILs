n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
bigger = [[False] * (n + 1) for _ in range(n + 1)]

for a, b in edges:
    bigger[a][b] = True

for k in range(1, n + 1):
    for i in range(1, n + 1):
        if not bigger[i][k]:
            continue

        for j in range(1, n + 1):
            if bigger[k][j]:
                bigger[i][j] = True

for i in range(1, n + 1):
    cnts = 0
    for j in range(1, n + 1):
        if i == j:
            continue

        if not bigger[i][j] and not bigger[j][i]:
            cnts += 1

    print(cnts)