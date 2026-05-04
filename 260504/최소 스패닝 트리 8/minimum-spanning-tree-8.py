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

edges.sort(key = lambda x: x[2])

answer = 0
cnt = 0

for u, v, w in edges:
    if union(u, v):
        answer += w
        cnt += 1

        if cnt == n - 1:
            break

print(answer)

