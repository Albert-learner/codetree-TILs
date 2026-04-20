n, m, k = map(int, input().split())

# Note: Adding 0 at start to match 1-based indexing of C++
vertex = [0] + list(map(int, input().split()))

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
        return

    if size[fa] < size[fb]:
        fa, fb = fb, fa

    parent[fb] = fa
    size[fa] += size[fb]

for a, b in edges:
    union(a, b)

comp_min = {}
for i in range(1, n + 1):
    r = find(i)
    if r not in comp_min:
        comp_min[r] = vertex[i]
    else:
        comp_min[r] = min(comp_min[r], vertex[i])

mins = list(comp_min.values())
if len(mins) == 1:
    answer = 0
else:
    min_val = min(mins)
    answer = sum(mins) + (len(mins) - 2) * min_val

if answer <= k:
    print(answer)
else:
    print("NO")