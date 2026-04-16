n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
parent = list(range(n + 1))

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
for i, (u, v) in enumerate(edges, start = 1):
    if not union(u, v):
        answer = i
        break

if answer == 0:
    print("happy")
else:
    print(answer)
        