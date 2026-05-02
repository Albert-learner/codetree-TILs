n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
px = sorted([(points[i][0], i) for i in range(n)])
py = sorted([(points[i][1], i) for i in range(n)])
pz = sorted([(points[i][2], i) for i in range(n)])

# Please write your code here.
edges = []

for arr in (px, py, pz):
    for i in range(n - 1):
        cost = abs(arr[i][0] - arr[i + 1][0])
        u = arr[i][1]
        v = arr[i + 1][1]
        edges.append((cost, u, v))

edges.sort()

parent = list(range(n))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(a, b):
    fa, fb = find(a), find(b)

    if fa == fb:
        return False

    parent[fb] = fa
    return True

answer = 0
cnt = 0

for cost, u, v in edges:
    if union(u, v):
        answer += cost
        cnt += 1
        if cnt == n - 1:
            break

print(answer)