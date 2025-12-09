n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
def dist(i, j):
    return int(abs(x[i] - x[j]) + abs(y[i] - y[j]))

L = [0] * n
for i in range(1, n):
    L[i] = L[i - 1] + dist(i - 1, i)

R = [0] * n
for i in range(n - 2, -1, -1):
    R[i] = R[i + 1] + dist(i, i + 1)

INF = 10 ** 18
min_dists = INF

for i in range(1, n - 1):
    dists = L[i - 1] + dist(i - 1, i + 1) + R[i + 1]
    if dists < min_dists:
        min_dists = dists

print(min_dists)
