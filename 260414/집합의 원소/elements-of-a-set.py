n, m = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(m)]

# Please write your code here.
parents = list(range(n + 1))

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    
    return parents[x]

def union(a, b):
    fa = find(a)
    fb = find(b)

    if fa == fb:
        return

    if fa < fb:
        parents[fb] = fa
    else:
        parents[fa] = fb

for cmd, a, b in queries:
    if cmd == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print(1)
        else:
            print(0)