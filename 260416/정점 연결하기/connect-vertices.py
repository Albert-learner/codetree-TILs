n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 2)]

# Please write your code here.
parent = list(range(n + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(a, b):
    fa, fb = find(a), find(b)

    if fa != fb:
        if fa < fb:
            parent[fb] = fa
        else:
            parent[fa] = fb

for a, b in edges:
    union(a, b)

component_min = {}

for i in range(1, n + 1):
    r = find(i)
    if r not in component_min:
        component_min[r] = i
    else:
        component_min[r] = min(component_min[r], i)

mins = sorted(component_min.values())
print(mins[0], mins[1])