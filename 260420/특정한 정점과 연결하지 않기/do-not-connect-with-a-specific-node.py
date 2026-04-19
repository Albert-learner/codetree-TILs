n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
A, B, k = map(int, input().split())

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

    parent[fb] = fa
    size[fa] += size[fb]

for a, b in edges:
    union(a, b)

rootA = find(A)
rootB = find(B)

roots = set()
for i in range(1, n + 1):
    roots.add(find(i))

candidates = []
for r in roots:
    if r == rootA or r == rootB:
        continue
    candidates.append(size[r])

candidates.sort(reverse = True)

answer = size[rootA]
for i in range(min(k, len(candidates))):
    answer += candidates[i]

print(answer)