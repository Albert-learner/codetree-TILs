n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
from_v, to_v, edge_type = zip(*edges)
from_v = list(from_v)
to_v = list(to_v)
edge_type = list(edge_type)

# Please write your code here.
def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(parent, a, b):
    fa, fb = find(parent, a), find(parent, b)

    if fa == fb:
        return False

    parent[fb] = fa
    return True

def get_zero_cnt(reverse = False):
    parent = list(range(n + 1))

    sorted_edges = sorted(edges, key = lambda x: x[2], reverse = reverse)

    zero_cnt = 0
    edge_cnt = 0

    for u, v, t in sorted_edges:
        if union(parent, u, v):
            if t == 0:
                zero_cnt += 1
            
            edge_cnt += 1

            if edge_cnt == n - 1:
                break

    return zero_cnt

min_zero = get_zero_cnt(reverse = False)
max_zero = get_zero_cnt(reverse = True)

answer = int(abs(max_zero ** 2 - min_zero ** 2))
print(answer)