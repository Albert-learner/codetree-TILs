n, m = map(int, input().split())
points = [0] + list(map(int, input().split()))
x = list(map(int, input().split())) if m > 0 else []

# Please write your code here.
forbidden = [False] * (n + 1)
for pos in x:
    forbidden[pos] = True

INF = 10 ** 18

dpA = [INF] * (n + 1)
dpB = [INF] * (n + 1)

dpA[0] = 0
if not forbidden[1]:
    dpB[0] = 0

for i in range(2, n + 1):
    newA = [INF] * (n + 1)
    newB = [INF] * (n + 1)

    for j in range(i):
        if dpA[j] != INF:
            newA[j] = min(newA[j], dpA[j] + abs(points[i] - points[i - 1]))


            if not forbidden[i]:
                add = 0 if j == 0 else abs(points[i] - points[j])
                newB[i - 1] = min(newB[i - 1], dpA[j] + add)

        if dpB[j] != INF:
            add = 0 if j == 0 else abs(points[i] - points[j])
            newA[i - 1] = min(newA[i - 1], dpB[j] + add)

            if not forbidden[i]:
                newB[j] = min(newB[j], dpB[j] + abs(points[i] - points[i - 1]))

    dpA, dpB = newA, newB

print(min(min(dpA), min(dpB)))