n, m = map(int, input().split())
type_arr = input().split()
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
total, cnt = 0, 0
for u, v, w in edges:
    if type_arr[u - 1] == type_arr[v - 1]:
        continue

    if union(u, v):
        total += w
        cnt += 1

        if cnt == n - 1:
            break

if cnt == n - 1:
    print(total)
else:
    print(-1)