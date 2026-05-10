n, m, k = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(a, b):
    fa, fb = find(a), find(b)

    if fa == fb:
        return False

    if size[fa] < size[fb]:
        fa, fb = fb, fa

    parent[fb] = fa
    size[fa] += size[fb]

    return True

edges.sort(key = lambda x: x[2])

mst_sum = 0
used = 0

for a, b, w in edges:
    if union(a, b):
        mst_sum += w
        used += 1

        if used == n - 1:
            break

extra = k * (n - 1) * (n - 2) // 2
print(mst_sum + extra)
